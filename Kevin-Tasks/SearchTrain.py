from tkinter import *
from tkinter.ttk import *
import pymysql
import urllib.request
import base64
from tkinter import messagebox
import datetime

class GUI:
    def __init__(self, rootWinSearch):
        self.rootWinSearch = Toplevel()
        self.rootWinSearch.title("Make a Reservation")
        #self.rootWinCF.withdraw()

        #pic = Label(self.rootWinSearch, image=self.image)
        #pic.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=W)

        self.allReservation = [()]

        s = Label(self.rootWinSearch, text="Search Train", font=("Calibri", 15, "bold"))#, fg="gold")
        s.grid(row=1, column=0, columnspan=2, pady=5)

        tNum = Label(self.rootWinSearch, text="Departs From")
        tNum.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        # populate with possible starting cities
        cities = self.searchCities()

        self.departsFrom = StringVar()
        pulldownD = OptionMenu(self.rootWinSearch, self.departsFrom, *cities)
        pulldownD.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        r = Label(self.rootWinSearch, text="Arrives At")
        r.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        self.arrivesAt = StringVar()
        pulldownA = OptionMenu(self.rootWinSearch, self.arrivesAt, *cities)
        pulldownA.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        c = Label(self.rootWinSearch, text="Departure Date (YYYY-MM-DD)")
        c.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        self.departDatesv = StringVar()
        self.departDateE = Entry(self.rootWinSearch, textvariable=self.departDatesv, width=20)
        self.departDateE.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        submit = Button(self.rootWinSearch, text="Find Trains", command=self.selectDepart)
        submit.grid(row=5, column=1, padx=10, pady=15, sticky=E)

    def selectDepart(self):
        departsFrom = self.departsFrom.get()
        departsFrom = departsFrom[departsFrom.index("(") + 1:departsFrom.rindex(")")]
        arrivesAt = self.arrivesAt.get()
        arrivesAt = arrivesAt[arrivesAt.index("(") + 1:arrivesAt.rindex(")")]
        departDate = self.departDateE.get()
        print(departsFrom)
        print(arrivesAt)
        print(departDate)

        self.rootWinSelectD = Toplevel()
        self.rootWinSelectD.title("Select Departure")
        self.rootWinSearch.withdraw()

        frame = Frame(self.rootWinSelectD)
        frame.pack(side=LEFT)
        frame2 = Frame(self.rootWinSelectD)
        frame2.pack(side=BOTTOM)

        #tree = self.departTree(frame)

        sql = "select TrainNumber,Concat(Depart,'-',Arrival,' (',Duration, ')') as Time, 1stClassPrice, 2ndClassPrice from (select TrainNumber, IFNULL(Timediff(Max(ArrivalTime),Min(y.DepartureTime)),0) as Duration, Max(y.ArrivalTime) as Arrival, Min(y.DepartureTime) as Depart, y.1stClassPrice, y.2ndClassPrice\
                    From (SELECT Stop.*,1stClassPrice,2ndClassPrice From Stop\
                    JOIN TrainRoute ON TrainRoute.TrainNumber = Stop.TrainNumber)\
                    as y\
                    Where y.Name = '%s' OR y.Name = '%s'\
                    Group By y.TrainNumber) as x\
                    where x.duration>0;" % (departsFrom, arrivesAt)

        #print('Getting all rooms associated with city: %s' % (sql))
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        if not results:
            r = messagebox.showerror("Error!", "No Train's Follow Criteria.")
        i = 0

        self.widgets = {}
        dc = Label(frame, text="Train Number", font=("Calibri", 12, "bold"))
        dc.grid(row=1, column=0, sticky='W')
        dc2 = Label(frame, text="Time (Duration)", font=("Calibri", 12, "bold"))
        dc2.grid(row=1, column=1, padx=30, pady=10, sticky='W')
        dc3 = Label(frame, text="1st Class Price", font=("Calibri", 12, "bold"))
        dc3.grid(row=1, column=2, padx=30, pady=10, sticky='W')
        dc4 = Label(frame, text="2nd Class Price", font=("Calibri", 12, "bold"))
        dc4.grid(row=1, column=4, padx=30, pady=10, sticky='W')
        self.train = StringVar()
        self.Price1 = IntVar()
        self.price2 = IntVar()
        row = 1
        for TrainNum, Dur, Arrivalt, DepartT in (results):
            row += 1
            self.widgets[TrainNum] = {
                "Train Number": Radiobutton(frame, text=TrainNum,variable=self.train,value=TrainNum),
                "Dur": Label(frame, text=Dur)
                #"Arrival Time": Radiobutton(frame, text = str(Arrivalt), variable = self.price,value = Arrivalt),
                #"Depart Time": Radiobutton(frame,text = str(DepartT), variable = self.price, value = DepartT)
            }

            self.widgets[TrainNum]["Train Number"].grid(row=row, column=0, sticky="nsew")
            self.widgets[TrainNum]["Dur"].grid(row=row, column=1, sticky="nsew")
            pr1=Radiobutton(frame, text=str(Arrivalt), variable=self.Price1, value=Arrivalt)
            pr1.grid(row=row,column=2,sticky="nsew")
            pr2 = Radiobutton(frame,text = str(DepartT), variable = self.price2, value=DepartT)
            pr2.grid(row=row,column=3,sticky="nsew")
            #self.widgets[TrainNum]["Arrival Time"].grid(row=row, column=2, sticky="nsew")

            #self.widgets[TrainNum]["Depart Time"].grid(row=row, column=3, sticky="nsew")

        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        # invisible row after last row gets all extra space
        frame.grid_rowconfigure(row + 1, weight=1)


        b2=Button(frame2, text ="Next", command = self.passengerInfo)
        b2.pack(side=RIGHT)

    def passengerInfo(self):
        self.passengerInfoWin = Toplevel()
        self.rootWinSelectD.withdraw()
        self.passengerInfoWin.deiconify()
        self.passengerInfoWin.title("Travel Extras & Passenger Info")

        frame = Frame(self.passengerInfoWin)
        frame.pack(side=TOP)
        frame2 = Frame(self.passengerInfoWin)
        frame2.pack(side=TOP)
        frame3 = Frame(self.passengerInfoWin)
        frame3.pack(side=TOP)
        frame4 = Frame(self.passengerInfoWin)
        frame4.pack(side=TOP)

        baggage = Label(frame, text="Number of Baggage")
        baggage.pack(side=LEFT)
        self.bags = StringVar()
        choices = ["1", "2", "3", "4"]
        self.bags.set(choices[0])
        option = OptionMenu(frame, self.bags, choices[0], *choices)
        option.pack(side=RIGHT)
        disclamer = Label(frame2, text="Every passenger can bring upto 4 baggage. 2 free of charge, 2 for $30 per bag")
        disclamer.pack()

        #print(self.price1[0].get())
        print(self.train.get(),self.Price1.get(),self.price2.get())


        passName = Label(frame3, text="Passenger Name")
        passName.pack(side=LEFT)
        self.name = StringVar()
        nameEnt = Entry(frame3, textvariable=self.name, width=10)
        nameEnt.pack(side=RIGHT)

        b1 = Button(frame4, text="Back")
        b1.pack(side=LEFT)
        b2 = Button(frame4, text="Next", command=self.makeReservation)
        b2.pack(side=RIGHT)

    def makeReservation(self):
        self.reservationWin = Toplevel()
        self.reservationWin.title("Make Reservation")

        frame = Frame(self.reservationWin)
        frame.pack(side=TOP)
        frame2 = Frame(self.reservationWin)
        frame2.pack(side=TOP)
        frame3 = Frame(self.reservationWin)
        frame3.pack(side=TOP)
        frame4 = Frame(self.reservationWin)
        frame4.pack(side=TOP)
        frame5 = Frame(self.reservationWin)
        frame5.pack(side=TOP)

        selected = Label(frame, text="Currently Selected")
        selected.grid(row=1,column=0)
        departsFrom = self.departsFrom.get()
        departsFrom = departsFrom[departsFrom.index("(") + 1:departsFrom.rindex(")")]
        arrivesAt = self.arrivesAt.get()
        arrivesAt = arrivesAt[arrivesAt.index("(") + 1:arrivesAt.rindex(")")]
        sql = "select Concat(Depart,'-',Arrival,' (',Duration, ')') as Time from (select TrainNumber, IFNULL(Timediff(Max(ArrivalTime),Min(y.DepartureTime)),0) as Duration, Max(y.ArrivalTime) as Arrival, Min(y.DepartureTime) as Depart, y.1stClassPrice, y.2ndClassPrice\
                    From (SELECT Stop.*,1stClassPrice,2ndClassPrice From Stop\
                    JOIN TrainRoute ON TrainRoute.TrainNumber = Stop.TrainNumber)\
                    as y\
                    Where y.Name = '%s' OR y.Name = '%s'\
                    Group By y.TrainNumber) as x\
                    where x.duration>0 and x.TrainNumber = '%s';" % (departsFrom, arrivesAt,self.train.get())
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        self.dVar = cursor.fetchall()[0]
        self.classVar=StringVar()

        if not self.Price1.get():
            self.classVar = "2nd Class"
            sql="select 2ndClassPrice From TrainRoute where TrainNumber='%s'" % (self.train.get())
            db = self.connect()
            cursor=db.cursor()
            cursor.execute(sql)
            pr = [pri[0] for pri in cursor.fetchall()]
        else:
            self.classVar = "1st Class"
            sql="select 1stClassPrice From TrainRoute where TrainNumber='%s'" % (self.train.get())
            db = self.connect()
            cursor=db.cursor()
            cursor.execute(sql)
            pr = [pri[0] for pri in cursor.fetchall()]
        #sqlRes = Max
        #cursor.execute(sqlRes)
        if not cursor.fetchall():
            self.allReservation = [(self.train.get(),self.departDatesv.get(),self.dVar,departsFrom,arrivesAt,self.classVar,pr,self.bags.get(),self.name.get()),0]
        else:
            self.allReservation = self.allReservation + [(self.train.get(), self.departDatesv.get(), self.dVar, departsFrom, arrivesAt, self.classVar, pr, self.bags.get(), self.name.get(),0)]

        #selectVal = [self.train.get(),self.departDatesv.get(),self.dVar.get(),departsFrom,arrivesAt, classVar,pr,self.bags.get(),self.name.get()]
        # selectVal = [,arrivesAt, classVar,pr,self.bags.get(),self.name.get()]
        Label(frame, text=self.train.get()).grid(row=3,column=0,sticky="nsew")
        Label(frame, text=self.departDatesv.get()).grid(row=3,column=1,sticky="nsew")
        Label(frame, text=self.dVar).grid(row=3,column=2,sticky="nsew")
        Label(frame, text=departsFrom).grid(row=3,column=3,sticky="nsew")
        Label(frame, text=arrivesAt).grid(row=3,column=4,sticky="nsew")
        Label(frame, text=self.classVar).grid(row=3,column=5,sticky="nsew")
        Label(frame, text=pr).grid(row=3,column=6,sticky="nsew")
        Label(frame, text=self.bags.get()).grid(row=3,column=7,sticky="nsew")
        Label(frame, text=self.name.get()).grid(row=3,column=8,sticky="nsew")
        Label(frame, text="Train Number", font=("Calibri", 12, "bold")).grid(row=2,column=0,sticky='nsew')
        Label(frame, text="Date", font=("Calibri", 12, "bold")).grid(row=2, column=1, sticky='nsew')
        Label(frame, text="Time", font=("Calibri", 12, "bold")).grid(row=2, column=2, sticky='nsew')
        Label(frame, text="Departs From", font=("Calibri", 12, "bold")).grid(row=2, column=3, sticky='nsew')
        Label(frame, text="Arrives At", font=("Calibri", 12, "bold")).grid(row=2, column=4, sticky='nsew')
        Label(frame, text="Class", font=("Calibri", 12, "bold")).grid(row=2, column=5, sticky='nsew')
        Label(frame, text="Price", font=("Calibri", 12, "bold")).grid(row=2, column=6, sticky='nsew')
        Label(frame, text="#of Baggages", font=("Calibri", 12, "bold")).grid(row=2, column=7, sticky='nsew')
        Label(frame, text="Passenger Name", font=("Calibri", 12, "bold")).grid(row=2, column=8, sticky='nsew')
        Button(frame, text="Remove").grid(row=3,column=9,sticky='nsew')#,command=cancelRes)

        stuDis = Label(frame2, text="Student Discount Applied:", font=("Calibri",12,"bold"))
        stuDis.pack(side=LEFT)
        username = "kberman"
        sql = "select IsStudent from Customer where username = '%s'" % username
        cursor.execute(sql)
        if not cursor.fetchall():
            stu = 'No'
        else:
            stu = 'Yes'
        st = Label(frame2, text = stu)
        st.pack(side=RIGHT)

        totalC = Label(frame3, text="Total Cost:", font=("Calibri",12,"bold"))
        totalC.pack(side=LEFT)
        bagCost = 0
        self.tcNum=0
        print(self.allReservation)
        for result in (self.allReservation):
            print(result)
            if int(result[7])>2:
                bagCost = bagCost+(int(result[7])-2)*30
            if not cursor.fetchall():
                self.tcNum = self.tcNum+bagCost+int(result[6][0])
                self.result[9] = bagCost+int(result[6][0])
            else:
                self.tcNum = self.tcNum+(bagCost+int(result[6][0]))*0.8
                self.result[9] = (bagCost+int(result[6][0]))*0.8
        tc = Label(frame3,text=self.tcNum)
        tc.pack(side=RIGHT)

        useC = Label(frame4,text = "Use Card:", font = ("Calibri",12,"bold"))
        useC.pack(side=LEFT)
        db = self.connect()
        cursor = db.cursor()
        query = "SELECT RIGHT(CardNumber,4) FROM PaymentInfo WHERE Username='Mark_Berman'"
        cursor.execute(query)
        cards = [card[0] for card in cursor.fetchall()]  # get cards from database
        self.useCard = StringVar()
        pulldownDC = OptionMenu(frame4, self.useCard, *cards)
        pulldownDC.pack(side=RIGHT)

        Button(frame5,text='Submit',command = self.submitRes).pack(side=RIGHT)
        Button(frame5,text='Add a Ticket',command=self.goBackToIntialWin).pack(side=LEFT)

    def goBackToIntialWin(self):
        self.reservationWin.withdraw()
        self.rootWinSearch.deiconify()
    def submitRes(self):
        self.submitResWin = Toplevel()
        self.reservationWin.withdraw()
        self.submitResWin.deiconify()
        self.submitResWin.title("Confomation")
        sql = "select count(ReservationID) from Reserves"
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        resID = cursor.fetchall()[0]
        departsFrom = self.departsFrom.get()
        departsFrom = departsFrom[departsFrom.index("(") + 1:departsFrom.rindex(")")]
        arrivesAt = self.arrivesAt.get()
        arrivesAt = arrivesAt[arrivesAt.index("(") + 1:arrivesAt.rindex(")")]
        for result in (self.allReservation):
            sql = "INSERT INTO Reserves (ReservationID,TrainNumber,Class,DepartureDate,PassengerName,NumBags,DepartsFrom,ArrivesAt,TicketPrice)\
                    VALUES\
                    (%i,'%s','%s','%s','%s',%i,'%s','%s',%i);" % (int(resID[0])+1,result[0],result[5],result[1],result[8],int(result[7]),result[3],result[4])
            cursor.execute(sql)

            sql = "Select CardNumber from PaymentInfo where RIGHT(CardNumber,4) ='%s';" % self.useCard.get()
            cursor.execute(sql)
            wholeCard = cursor.fetchall()[0]

            sql = "INSERT INTO Reservation (ReservationID,isCancelled,CardNumber,Username)\
                    VALUES\
                    (%i, 0,'%s','Mark_Berman');" % (int(resID[0])+1,wholeCard[0])
            cursor.execute(sql)

        frame = Frame(self.submitResWin)
        frame.pack(side=TOP)
        Label(frame,text='Reservation ID is:',font = ("Calibri",12,"bold")).grid(row=0,column=0,padx=10)
        Label(frame,text='%s'%str(int(resID[0])+1),font=("Calibri",12,"bold")).grid(row=0,column=1,padx=10)

        frame2 = Frame(self.submitRes)
        frame2.pack(side=TOP)
        Button(frame2,text='Go Back to Choose Functionality')



    def departTree(self, frame):
        tree = Treeview(frame, selectmode='browse')
        tree.pack()

        tree["columns"] = ("train", "time", "1st", "2nd")
        tree.heading("train", text="Train (Train Number)")
        tree.heading("time", text="Time (Duration)")
        tree.heading("1st", text="1st Class Price")
        tree.heading("2nd", text="2nd Class Price")
        return tree

    def selectTree(self, frame):
        tree = Treeview(frame)
        tree.pack()

        tree["columns"] = ("train", "time", "dept", "arrv", "class", "pr", "bag", "name", "rem")
        tree.heading("train", text="Train (Train Number)")
        tree.heading("time", text="Time (Duration)")
        tree.heading("dept", text="Departs From")
        tree.heading("arrv", text="Arrives At")
        tree.heading("class", text="Class")
        tree.heading("pr", text="Price")
        tree.heading("bag", text="# of baggages")
        tree.heading("name", text="Passenger Name")
        tree.heading("rem", text="Remove")
        return tree

    def searchCities(self):
        db = self.connect()
        cursorN = db.cursor()
        cursorL = db.cursor()
        queryName = "SELECT * FROM Station"
        queryLoc = "SELECT * FROM Station"
        cursorN.execute(queryName)
        cursorL.execute(queryLoc)
        Names = [name[0] for name in cursorN.fetchall()]
        Locations = [location[1] for location in cursorL.fetchall()]
        cities = ["%s (%s)" % (Locations.pop(), Names.pop())]
        for i in range(1,6):
            new = "%s (%s)" % (Locations.pop(), Names.pop())
            cities.append(new)

        return(cities)
    def connect(self):
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu",
                             user="cs4400_Team_39",
                             passwd="HSaWNuO5",
                             db="cs4400_Team_39")
        return (db)

win = Tk()
app = GUI(win)
win.mainloop()
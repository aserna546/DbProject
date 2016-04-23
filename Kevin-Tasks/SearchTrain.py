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
        frame.pack(side=TOP)

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
        # for result in results:
        #     tree.insert('', i, text='', values=result)
        #     i += 1
        # print(results)
        self.widgets = {}
        dc = Label(frame, text="Train Number", font=("Calibri", 12, "bold"))
        dc.grid(row=1, column=0, sticky='W')
        dc2 = Label(frame, text="Time (Duration)", font=("Calibri", 12, "bold"))
        dc2.grid(row=1, column=1, padx=30, pady=10, sticky='W')
        dc3 = Label(frame, text="1st Class Price", font=("Calibri", 12, "bold"))
        dc3.grid(row=1, column=2, padx=30, pady=10, sticky='W')
        dc4 = Label(frame, text="2nd Class Price", font=("Calibri", 12, "bold"))
        dc4.grid(row=1, column=4, padx=30, pady=10, sticky='W')
        self.price = IntVar()
        row = 1
        for TrainNum, Dur, Arrivalt, DepartT in (results):
            row += 1
            self.widgets[TrainNum] = {
                "Train Number": Label(frame, text=TrainNum),
                "Dur": Label(frame, text=Dur),
                #"Arrival Time": Label(frame, text=Arrivalt),
                "Arrival Time": RADIOBUTTON(frame, text = str(Arrivalt), variable = self.price,value = Arrivalt),
                "Depart Time": RADIOBUTTON(frame,text = str(DepartT), variable = self.price, value = DepartT)

                #"start_time": tk.Label(table, text=start_time),
                #"end_time": tk.Label(table, text=start_time)
            }

            self.widgets[TrainNum]["Train Number"].grid(row=row, column=0, sticky="nsew")
            self.widgets[TrainNum]["Station"].grid(row=row, column=1, sticky="nsew")
            self.widgets[TrainNum]["Arrival Time"].grid(row=row, column=2, sticky="nsew")

            self.widgets[TrainNum]["Depart Time"].grid(row=row, column=3, sticky="nsew")

        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        # invisible row after last row gets all extra space
        frame.grid_rowconfigure(row + 1, weight=1)


        b2=Button(frame, text ="Next", command = self.passengerInfo)
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

        passName = Label(frame3, text="Passenger Name")
        passName.pack(side=LEFT)
        name = StringVar()
        nameEnt = Entry(frame3, textvariable=name, width=10)
        nameEnt.pack(side=RIGHT)

        b1 = Button(frame4, text="Back")
        b1.pack(side=LEFT)
        b2 = Button(frame4, text="Next", command=self.makeReservation)
        b2.pack(side=RIGHT)

    def makeReservation(self):
        self.passengerInfoWin = Toplevel()
        self.passengerInfoWin.withdraw()
        self.reservationWin.deiconify()
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
        frame5.pack(side=BOTTOM)

        selected = Label(frame, text="Currently Selected")
        selected.pack(side=LEFT)

        tree = self.selectTree(frame)


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
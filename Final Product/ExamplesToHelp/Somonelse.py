#Arthi Nithi, Anjani Agrawal, Alan Chiang, Alaap Murali

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import pymysql
import calendar
from datetime import datetime

class Phase_three:
    def __init__(self,primaryWin):
        self.primaryWin = primaryWin
        self.Login()

        self.totalCost = 0

        self.newUserWindow = Toplevel()
        self.Register()
        self.newUserWindow.title("New User Registration")
        self.newUserWindow.withdraw()

        self.primaryWindow = Toplevel()
        self.primaryWindow.title("Welcome "+self.username.get())
        self.primaryWindow.withdraw()

        self.schoolInfoWin= Toplevel()
        self.schoolInfoWin.title("Add School Info")
        self.schoolInfoWin.withdraw()

        self.trainSchWin= Toplevel()
        self.trainSchWin.title("View Train Schedule")
        self.trainSchWin.withdraw()

        self.scheduleWin= Toplevel()
        self.scheduleWin.title("View Train Schedule")
        self.scheduleWin.withdraw()

        self.findAvailWindow= Toplevel()
        self.findAvailWindow.title("Search Train")
        self.findAvailWindow.withdraw()

        self.departureWin = Toplevel()
        self.departureWin.title("Select Departure")
        self.departureWin.withdraw()

        self.passengerInfoWin = Toplevel()
        self.passengerInfoWin.title("Travel Extras & Passenger Info")
        self.passengerInfoWin.withdraw()

        self.reservationWin = Toplevel()
        self.reservationWin.title("Make Reservation")
        self.reservationWin.withdraw()

        self.paymentIWin = Toplevel()
        self.paymentIWin.title("Add Card")
        self.paymentIWin.withdraw()

        self.paymentIWin2 = Toplevel()
        self.paymentIWin2.title("Delete Card")
        self.paymentIWin2.withdraw()

        self.confirm = Toplevel()
        self.confirm.title("Confirmation")
        self.confirm.withdraw()

        self.updateWin = Toplevel()
        self.updateWin.title("Update Reservation")
        self.updateWin.withdraw()

        self.updateWin2 = Toplevel()
        self.updateWin2.title("Update Reservation")
        self.updateWin2.withdraw()

        self.updateWin3 = Toplevel()
        self.updateWin3.title("Update Reservation")
        self.updateWin3.withdraw()

        self.cancelWin = Toplevel()
        self.cancelWin.title("Cancel Reservation")
        self.cancelWin.withdraw()

        self.cancelWin2 = Toplevel()
        self.cancelWin2.title("Cancel Reservation")
        self.cancelWin2.withdraw()

        self.viewReviewWin = Toplevel()
        self.viewReviewWin.title("View review")
        self.viewReviewWin.withdraw()

        self.viewReviewWin2 = Toplevel()
        self.viewReviewWin2.title("View review")
        self.viewReviewWin2.withdraw()

        self.giveReviewWin = Toplevel()
        self.giveReviewWin.title("Give Review")
        self.giveReviewWin.withdraw()

        self.viewRevenueReport = Toplevel()
        self.viewRevenueReport.title("View Revenue Report")
        self.viewRevenueReport.withdraw()

        self.viewpopRRWin = Toplevel()
        self.viewpopRRWin.title("View Popular Route Report")
        self.viewpopRRWin.withdraw()

    def Connect(self):
        try:
            db = pymysql.connect(host="academic-mysql.cc.gatech.edu", passwd="dwet2rPC", user="cs4400_Team_48",db="cs4400_Team_48")
            return db
        except:
            messagebox.showerror("Error", "Check Internet Connection")

    def Login(self):
        self.primaryWin.title("Login")
        frame = Frame(self.primaryWin)
        frame.pack()
        frame2 = Frame(self.primaryWin)
        frame2.pack()

        label1 = Label(frame,text = "Username")
        label2 = Label(frame,text ="Password")
        label1.grid(row = 0, column = 0,sticky=E)
        label2.grid(row = 1, column = 0,sticky=E)
        self.username = StringVar()
        self.password = StringVar()
        entry1 = Entry(frame, textvariable = self.username, width = 30)
        entry1.grid(row = 0, column = 1)
        entry2 = Entry(frame, textvariable = self.password, width = 30)
        entry2.grid(row = 1, column = 1)

        b1=Button(frame2, text ="Login", command=self.loginCredentials)
        b1.pack(side=LEFT)
        b2=Button(frame2, text ="Register", command= self.switchToRegister)
        b2.pack(side=LEFT)

    def loginCredentials(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "Invalid input")
            return

        server = self.Connect()
        cursor = server.cursor()
        query = "SELECT Username FROM CUSTOMER \
               WHERE (CUSTOMER.Username = '%s' AND (SELECT Password FROM USER WHERE CUSTOMER.Username = USER.Username) = '%s')" % (self.username.get(), self.password.get())
        cursor.execute(query)
        result1 = cursor.fetchall()
        query = "SELECT Username FROM MANAGER \
               WHERE (MANAGER.Username = '%s' AND (SELECT Password FROM USER WHERE MANAGER.Username = USER.Username) = '%s')" % (self.username.get(), self.password.get())

        cursor.execute(query)
        result2 = cursor.fetchall()

        if len(result1) != 0:
            print("Customer")
            self.custOrManag = "customer"
            for row in result1:
                self.name = row[0]
            self.switchtoMainMenu()
        elif len(result2) != 0:
            self.custOrManag = "manager"
            for row in result2:
                self.name = row[0]
            self.switchtoMainMenu()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def mainMenu(self):
        self.primaryWindow.deiconify()
        self.primaryWindow.title("Choose Functionality ")
        buttonsFrame = Frame(self.primaryWindow)
        buttonsFrame.pack()
        if self.custOrManag == "customer":
            b1 = Button(buttonsFrame, text ="View Train Schedule", command = self.trainSchedule)
            b1.grid(row = 0, column = 0, columnspan = 2, sticky = EW)
            b2 = Button(buttonsFrame, text ="Make a new reservation", command = self.searchTrain)
            b2.grid(row = 1, column = 0, columnspan = 2, sticky = EW)
            b3 = Button(buttonsFrame, text ="Update a reservation", command = self.updateReservation)
            b3.grid(row = 2, column = 0, columnspan = 2, sticky = EW)
            b4 = Button(buttonsFrame, text ="Cancel a reservation", command = self.cancelRes)
            b4.grid(row = 3, column = 0, columnspan = 2, sticky = EW)
            b5 = Button(buttonsFrame, text ="Give review", command = self.giveReview)
            b5.grid(row = 4, column = 0, columnspan = 2, sticky = EW)
            b6 = Button(buttonsFrame, text ="Add school information (student discount)", command = self.schoolInfo)
            b6.grid(row = 5, column = 0, columnspan = 2, sticky = EW)
            b7 = Button(buttonsFrame, text ="Log out", command = self.logout)
            b7.grid(row = 6, column = 0, columnspan = 2, sticky = EW)
        elif self.custOrManag == "manager":
            b8 = Button(buttonsFrame, text ="View revenue report", command = self.viewRevenueRep)
            b8.grid(row = 0, column = 0, columnspan = 2, sticky = EW)
            b9 = Button(buttonsFrame, text ="View popular route report", command = self.viewpopRR)
            b9.grid(row = 1, column = 0, columnspan = 2, sticky = EW)
            b10=Button(buttonsFrame, text ="Log out")#, command = s
            b10.grid(row = 2, column = 0, columnspan = 2, sticky = EW)

    def switchToRegister(self):
        self.primaryWin.destroy()
        self.newUserWindow.deiconify()

    def switchToLogin(self):
        self.newUserWindow.withdraw()
        self.primaryWin.deiconify()

    def switchtoMainMenu(self):
        self.primaryWin.withdraw()
        #self.primaryWindow.deiconify()
        self.mainMenu()

    def Register(self):
        self.newUserWindow.title("New User Registration")
        frame=Frame(self.newUserWindow)
        frame.pack()
        frame2=Frame(self.newUserWindow)
        frame2.pack(side = BOTTOM)

        label1 = Label(frame,text = "Username", justify = LEFT)
        label1.grid(row = 0, column = 0, sticky = W)
        self.registeredUser = StringVar()
        self.uentry = Entry(frame, textvariable = self.registeredUser, width = 30, justify = RIGHT)
        self.uentry.grid(row = 0, column = 1, sticky = W)

        label2 = Label(frame,text ="Email Address", justify = LEFT)
        label2.grid(row = 1, column = 0, sticky = W)
        self.registeredPass = StringVar()
        self.password_entry = Entry(frame, textvariable = self.registeredPass, width = 30, justify = RIGHT)
        self.password_entry.grid(row = 1, column = 1, sticky = W)

        label3 = Label(frame,text = "Password", justify = LEFT)
        label3.grid(row = 2, column = 0, sticky = W)
        self.registeredPassConfirm = StringVar()
        self.confirm_password_entry = Entry(frame, textvariable = self.registeredPassConfirm, width = 30, justify = RIGHT)
        self.confirm_password_entry.grid(row = 2, column = 1, sticky = W)

        label4 = Label(frame,text ="Confirm Password", justify = LEFT)
        label4.grid(row = 3, column = 0, sticky = W)
        self.registerEmail = StringVar()
        self.email_entry = Entry(frame, textvariable = self.registerEmail, width = 30, justify = RIGHT)
        self.email_entry.grid(row = 3, column = 1, sticky = W)

        b_reg=Button(frame2, text ="Create", command = self.registerCredentials)
        b_reg.pack(side = BOTTOM)

    def registerCredentials(self):
        if self.registeredUser.get() == "" or self.registeredPass.get() == "" or self.registeredPassConfirm.get() == "" or self.registerEmail.get() == "":
            messagebox.showerror("Error", "Invalid input")
            return

        if self.registeredPass.get() != self.registeredPassConfirm.get():
            messagebox.showerror("Error", "Passwords must match")
            return

        server = self.Connect()
        cursor = server.cursor()
        query1 = "SELECT * FROM CUSTOMER, MANAGER \
               WHERE CUSTOMER.Username = '%s' OR MANAGER.Username = '%s'" % (self.registeredUser.get(), self.registeredUser.get())
        cursor.execute(query1)
        result1 = cursor.fetchall()
        cursor.execute(query1)
        if len(result1) != 0:
            messagebox.showerror("Error", "Username already in use")
            return

        query2 = "INSERT INTO CUSTOMER(Username, Password, Email) \
               VALUES ('%s', '%s', '%s')" % (self.registeredUser.get(), self.registeredPass.get(), self.registerEmail.get())
        cursor.execute(query2)
        result2 = cursor.fetchall()
        self.switchToLogin()

    def schoolInfo(self):
        self.primaryWindow.destroy()
        self.schoolInfoWin = Toplevel()
        self.schoolInfoWin.title("Add School Info")
        frame1 = Frame(self.schoolInfoWin)
        frame2 = Frame(self.schoolInfoWin)
        frame1.pack(side = TOP)
        frame2.pack(side = BOTTOM)
        self.emailaddress = StringVar()
        self.entry = Entry(frame1, textvariable = self.emailaddress, width = 30)
        self.entry.grid(row = 0, column = 1)
        label1 = Label(frame1,text = "School Email Address")
        label1.grid(row = 0, column = 0)
        label2 = Label(frame1,text = "Your school email adress ends with .edu")
        label2.grid(row = 1, column = 0)

        b1 = Button(frame2, text ="Back", command = self.sMAINMENU)
        b1.grid(row = 2, column = 0)
        b2 = Button(frame2, text ="Submit", command = self.writeToDB)
        b2.grid(row = 2, column = 1)

    def writeToDB(self):
        if self.emailaddress.get()[-4:] == ".edu":
            server = self.Connect()
            cursor = server.cursor()
            query = "UPDATE CUSTOMER SET Is_student = 1 WHERE Username = '%s'" % (self.registeredUser.get())
            cursor.execute(query)
            result = cursor.fetchall()
        self.schoolInfoWin.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

    def logout(self):
        self.primaryWindow.destroy()
        self.primaryWin = Toplevel()
        self.Login()

    def sMAINMENU(self):
        self.schoolInfoWin.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

    def trainSchedule(self):
        self.primaryWindow.destroy()
        self.trainSchWin = Toplevel()
        self.trainSchWin.title("View Train Schedule")
        frame1 = Frame(self.trainSchWin)
        frame2 = Frame(self.trainSchWin)
        frame1.pack(side = TOP)
        frame2.pack(side = BOTTOM)
        label1 = Label(frame1,text = "Train Number")
        label1.pack(side=LEFT)

        self.trainNumber = IntVar()
        self.entry = Entry(frame1, textvariable = self.trainNumber, width = 10)
        self.entry.pack(side=RIGHT)

        b1 = Button(frame2, text ="Search", command = self.schedule)
        b1.pack(side=LEFT)

    def getTrainTree(self, frame):
        tree=Treeview(frame)
        tree.pack()
        tree["show"] = "headings"
        tree["columns"]=("train","arrv","dept","stat")
        tree.heading("train", text= "Train (Train Number)")
        tree.heading("arrv", text= "Arrival Time")
        tree.heading("dept", text= "Departure Time")
        tree.heading("stat", text= "Station")
        return tree

    def schedule(self):
        self.trainSchWin.destroy()
        self.scheduleWin = Toplevel()
        self.scheduleWin.title("View Train Schedule")

        frame1 = Frame(self.scheduleWin)
        frame1.pack()

        tree = self.getTrainTree(frame1)
        server = self.Connect()
        cursor = server.cursor()

        trainNum = self.trainNumber.get()
        query1 = "SELECT * FROM STOP WHERE Train_Number = '%d'" % (trainNum)

        cursor.execute(query1)
        results = cursor.fetchall()
        i = 0
        for result in results:
            tree.insert('', i, text='', values=(result[2], result[0],result[1], result[3]))
            i += 1

        b1 = Button(frame1, text ="Back", command = self.switchToMainMenu)
        b1.pack(side= BOTTOM)

    def switchToMainMenu(self):
        self.scheduleWin.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

def searchTrain(self):
        self.primaryWindow.withdraw()
        self.findAvailWindow = Toplevel()

        self.findAvailWindow.title("Search Train")
        frame = Frame(self.findAvailWindow)
        frame.pack(side=TOP)
        frame1=Frame(self.findAvailWindow)
        frame1.pack(side=TOP)
        frame2=Frame(self.findAvailWindow)
        frame2.pack(side=TOP)
        frame3=Frame(self.findAvailWindow)
        frame3.pack(side=TOP)

        location= Label(frame,text = "Departs From")
        location.grid(row = 0, column = 0, sticky = E)
        self.city = StringVar()

        server = self.Connect()
        cursor = server.cursor()
        query = "SELECT Name FROM STATION"
        cursor.execute(query)
        results = cursor.fetchall()

        option=OptionMenu(frame, self.city, results[0], *results)
        option.grid(row = 0, column = 1, sticky = W)

        arriveAt= Label(frame1,text ="Arrive At")
        arriveAt.grid(row = 1, column = 0, sticky = E)
        self.arrv = StringVar()

        option=OptionMenu(frame1, self.arrv, results[0], *results)
        option.grid(row = 1, column = 1, sticky = W)

        depDate= Label(frame2,text ="Departure Date")
        depDate.grid(row = 2, column = 0, sticky = E)
        self.date = StringVar()
        start_date= Label(frame2,text ="Start Date (YYYY-MM-DD)")
        self.startDateEntry = Entry(frame2, textvariable = self.date, width = 10)
        self.startDateEntry.grid(row = 2, column = 1, sticky = W)

        b=Button(frame3, text ="Find Trains", command = self.departureInfo)
        b.pack(side=RIGHT)

    def departureInfo(self):
        start_date = datetime.strptime(self.startDateEntry.get(), '%Y-%m-%d')
        if start_date < datetime.now():
            messagebox.showerror("Error", "Invalid Date (Either in the past or start > end)")
        else:
            self.findAvailWindow.withdraw()
            self.departureWin = Toplevel()
            self.departureWin.title("Select Departure")

            frame = Frame(self.departureWin)
            frame.pack(side=TOP)

            chosenCity = self.city.get()
            chosenArrv = self.arrv.get()
            chosenDate = self.date.get()

##            server = self.Connect()
##            cursor = server.cursor()
##
##            stop1 = "CREATE VIEW Stop1 (Train_Number) AS SELECT Train_Number FROM STOP WHERE STOP.Name = '%s'" % (chosenCity)
##            stop2 = "CREATE VIEW Stop2 (Train_Number) AS SELECT Train_Number FROM STOP WHERE STOP.Name = '%s'" % (chosenArrv)
##            stops = "CREATE VIEW Stops (Train_Number) AS SELECT Train_Number FROM Stop2 NATURAL JOIN Stop1"
##
##            query = "SELECT (STOP.Train_Number, STOP.Depature_Time, STOP.Arrival_Time, TRAIN_ROUTE.First_Class_Price, TRAIN_ROUTE.Second_Class_Price) FROM (STOP, TRAIN_ROUTE) WHERE \
##                STOP.Train_Number =  Stops.Train_Number AND TRAIN_ROUTE.Train_Number = Stops.Train_Number)"
##
##            cursor.execute(query)
##            results = cursor.fetchall()

            results = [("d","d","d","d"),("d","d","d","d"),("d","d","d","d")]

            l1 = Label(frame,text = "Train(Train Number)").grid(row = 0, column = 0)
            l2 = Label(frame,text = "Time(Duration)").grid(row = 0, column = 2)
            l3 = Label(frame,text = "1st Class Price").grid(row = 0, column = 4)
            l4 = Label(frame,text = "2nd Class Price").grid(row = 0, column = 6)

            a = 1
            b = 1
            c = 2
            self.v = IntVar()
            for result in results:
                Label(frame, text = str(result[0]), anchor = "w").grid(row = a, column = 0, sticky = "ew")
                Label(frame, text = str(result[1]), anchor = "w").grid(row = a, column = 2, sticky = "ew")
                Radiobutton(frame, text = str(result[2]), variable = self.v, value = b).grid(row = a, column = 4, sticky = "ew")
                Radiobutton(frame, text = str(result[3]), variable = self.v, value = c).grid(row = a, column = 6, sticky = "ew")
                a += 1
                b += 2
                c += 2
            self.row = a
            self.value1 = b
            self.value2 = c

            b1=Button(frame, text ="Back", command = self.switchtoSearchTrain)
            b1.grid(row = a, column = 0)
            b2=Button(frame, text ="Next", command = self.passengerInfo)
            b2.grid(row = a, column = 1)

    def switchtoSearchTrain(self):
        self.departureWin.destroy()
        self.findAvailWindow.deiconify()

    def passengerInfo(self):
        self.departureWin.withdraw()
        self.passengerInfoWin = Toplevel()
        self.passengerInfoWin.title("Travel Extras & Passenger Info")

        frame = Frame(self.passengerInfoWin)
        frame.pack(side=TOP)
        frame2 = Frame(self.passengerInfoWin)
        frame2.pack(side=TOP)
        frame3 = Frame(self.passengerInfoWin)
        frame3.pack(side=TOP)
        frame4 = Frame(self.passengerInfoWin)
        frame4.pack(side=TOP)

        baggage= Label(frame,text = "Number of Baggage")
        baggage.pack(side=LEFT)
        self.bags = StringVar()
        choices = ["1", "2", "3", "4"]
        #self.bags.set(choices[0])
        option=OptionMenu(frame, self.bags, choices[0], *choices)
        option.pack(side=RIGHT)
        disclamer = Label(frame2,text = "Every passenger can bring upto 4 baggage. 2 free of charge, 2 for $30 per bag")
        disclamer.pack()

        passName= Label(frame3,text ="Passenger Name")
        passName.pack(side=LEFT)
        self.name = StringVar()
        nameEnt = Entry(frame3, textvariable = self.name, width = 10)
        nameEnt.pack(side = RIGHT)

        server = self.Connect()
        cursor = server.cursor()
        num = int(option)
        query = "UPDATE RESERVES SET Number_of_Bags='%d', Passenger_Name='%s' WHERE Username='%s'" % (num, nameEnt, self.registeredUser.get())

        cursor.execute(query)

        b1=Button(frame4, text ="Back", command = self.switchToDepartureInfo)
        b1.pack(side=LEFT)
        b2=Button(frame4, text ="Next", command=self.makeReservation)
        b2.pack(side=RIGHT)

    def switchToDepartureInfo(self):
        self.passengerInfoWin.destroy()
        self.departureWin.deiconify()

##    def selectTree(self, frame):
##        tree=Treeview(frame)
##        tree.grid(row =1, column = 0)
##        tree["show"] = "headings"
##        tree["columns"]=("train","time","dept","arrv", "class", "pr", "bag", "name", "rem")
##        tree.heading("train", text= "Train (Train Number)")
##        tree.heading("time", text= "Time (Duration)")
##        tree.heading("dept", text= "Departs From")
##        tree.heading("arrv", text= "Arrives At")
##        tree.heading("class", text= "Class")
##        tree.heading("pr", text= "Price")
##        tree.heading("bag", text= "# of baggages")
##        tree.heading("name", text= "Passenger Name")
##        tree.heading("rem", text= "Remove")
##        return tree

################## table values need to appear and teh total cost for the trip should appear in the entry and if you press submit the reservation needs to be added onto the DB#####################
    def makeReservation(self):
        self.passengerInfoWin.withdraw()
        self.reservationWin = Toplevel()
        self.reservationWin.title("Make Reservation")

        frame = Frame(self.reservationWin)
        frame.pack(side=TOP)
        frame2 = Frame(self.reservationWin)
        frame2.pack(side=TOP)

        selected = Label(frame,text = "Currently Selected")
        selected.grid(row = 0, column = 0)

        l1 = Label(frame,text = "Train(Train Number)").grid(row = 1, column = 0)
        l2 = Label(frame,text = "Time(Duration)").grid(row = 1, column = 1)
        l3 = Label(frame,text = "Departs From").grid(row = 1, column = 2)
        l4 = Label(frame,text = "Arrives At").grid(row = 1, column = 3)
        l5 = Label(frame,text = "Class").grid(row = 1, column = 4)
        l6 = Label(frame,text = "Price").grid(row = 1, column =5)
        l7 = Label(frame,text = "# of baggages").grid(row = 1, column = 6)
        l8 = Label(frame,text = "Passenger Name").grid(row = 1, column = 7)
        l9 = Label(frame,text = "Remove").grid(row = 1, column = 8)

        l1 = train number of self.v
        l2 =





        #self.v = 1 when selected
        #self.bags.get()
        #self.name.get()


        results = [("gjdgs", "fjdghvk","fvdfvfd","dfvdf"),("gjdgs", "fjdghvk","fvdfvfd","dfvdf"),("gjdgs", "fjdghvk","fvdfvfd","dfvdf")]
        a = 1
        b = 1
        c = 2
        self.w = IntVar()
        for result in results:
            l10 = Label(frame, text = str(result[0]), anchor = "w")
            l10.grid(row = a, column = 0, sticky = "ew")
            l11 = Label(frame, text = str(result[1]), anchor = "w")
            l11.grid(row = a, column = 1, sticky = "ew")
            l12 = Label(frame, text = str(result[2]), anchor = "w")
            l12.grid(row = a, column = 2, sticky = "ew")
            l13 = Label(frame, text = str(result[3]), anchor = "w")
            l13.grid(row = a, column = 3, sticky = "ew")
            l14 = Label(frame, text = str(result[4]), anchor = "w")
            l14.grid(row = a, column = 4, sticky = "ew")
            l15 =Label(frame, text = str(result[5]), anchor = "w")
            l15.grid(row = a, column = 5, sticky = "ew")
            l16 = Label(frame, text = str(result[6]), anchor = "w")
            l16.grid(row = a, column = 6, sticky = "ew")
            l17 = Label(frame, text = str(result[7]), anchor = "w")
            l17.grid(row = a, column = 7, sticky = "ew")
            b = Button(frame, text = "Remove", variable = self.w, anchor= "w")
            b.grid(row = a, column = 8 , stickey = "ew")
            a = a + 1


    #######################FIX THIS###################
##        chosenTrain = self.trainName.get()
##
##        chosenCity = self.city.get()
##        chosenArrv = self.arrv.get()
##        chosenDate = self.date.get()

##        sql = "SELECT * FROM ROOM WHERE LOCATION = '%s' AND NOT EXISTS \
##                (SELECT Room_Number \
##                FROM RESERVATION_HAS_ROOM NATURAL JOIN RESERVATION \
##            WHERE ROOM.Room_Number = RESERVATION_HAS_ROOM.Room_Number AND ROOM.LOCATION = RESERVATION_HAS_ROOM.LOCATION AND RESERVATION.Is_Cancelled = '0' AND (('%s' >= Start_Date \
##            AND '%s' <= End_Date) OR ('%s' >= Start_Date AND '%s' <= End_Date) OR ('%s' >= Start_Date AND '%s' <= End_Date)))" % (chosenCity, start_date, end_date, start_date, start_date, end_date, end_date)
##        print('Getting all rooms associated with city: %s' % (sql))
##        db = self.Connect()
##        cursor = db.cursor()
##        cursor.execute(sql)
##        results = cursor.fetchall()
##        i = 0
##        for result in results:
##            tree.insert('', i, text='', values=result)
##            i += 1

        stuDis= Label(frame2,text = "Student Discount Applied.")
        stuDis.grid(row = 2, column = 0)
        totalC= Label(frame2, text = "Total Cost")
        totalC.grid(row = 3, column = 0)
        cost = StringVar()
        costEnt = Entry(frame2, textvariable = cost, width = 10)
        costEnt.grid(row = 3, column = 1)

        useCard= Label(frame2, text = "Use Card")
        useCard.grid(row = 4, column = 0)

        query = "SELECT Card_Number FROM PAYMENT_INFO WHERE Username = '%s'" % (self.registeredUser.get())
        cursor.execute(query)
        results = cursor.fetchall()

        self.card.set(results[0])
        option=OptionMenu(frame2, self.card, results[0], *results)
        option.grid(row = 4, column = 1)

        b5=Button(frame2, text ="Delete Card", command = self.deleteCard)
        b5.grid(row = 4, column =2)
        b1=Button(frame2, text ="Add Card", command = self.addCard)
        b1.grid(row = 4, column =3)

        b2=Button(frame2, text ="Continue adding a train", command = self.switchToSearchTrain)
        b2.grid(row = 5, column = 0)

        b3=Button(frame2, text ="Back", command = self.switchToPassengerInfo)
        b3.grid(row = 6, column = 0)
        b4=Button(frame2, text ="Submit", command = self.confirmation)
        b4.grid(row =6, column = 1)
 #calculations line

        query = "INSERT INTO "



    def switchToSearchTrain(self):
        self.reservationWin.destroy()
        self.searchTrain()

    def switchToPassengerInfo(self):
        self.reservationWin. destroy()
        self.passengerInfoWin.deiconify()

##    def getCost(self):
##        total = 0
##        for button in self.checkButtonsInDetails:
##            if button.is_checked():
##                total += button.selectRoom()[5]
##            total += button.selectRoom()[2]
##        self.totalCost = total*self.numDays
##        totallabel5 = Label(self.checkDetailsFrame, text=str(self.totalCost))
##        self.totalCostVarLabel.pack(side=TOP)
##        totallabel5.pack(side=TOP)

    def addCard(self):
        self.reservationWin.withdraw()
        self.paymentIWin = Toplevel()
        self.paymentIWin.title("Add Card")

        frame = Frame(self.paymentIWin)
        frame.pack(side=TOP)
        frame2 = Frame(self.paymentIWin)
        frame2.pack(side=TOP)
        frame3 = Frame(self.paymentIWin)
        frame3.pack(side=TOP)
        frame4 = Frame(self.paymentIWin)
        frame4.pack(side=TOP)
        frame5 = Frame(self.paymentIWin)
        frame5.pack(side=TOP)

        l1= Label(frame,text = "Name on Card")
        l1.pack(side=LEFT)
        l2= Label(frame2,text = "Card Number")
        l2.pack(side=LEFT)
        l3= Label(frame3,text = "CVV")
        l3.pack(side=LEFT)
        l4= Label(frame4,text = "Expiration Date")
        l4.pack(side=LEFT)

        self.name = StringVar()
        cardName = Entry(frame, textvariable = self.name, width = 10)
        cardName.pack(side = RIGHT)

        self.num = StringVar()
        cardNum = Entry(frame2, textvariable = self.num, width = 10)
        cardNum.pack(side = RIGHT)

        self.CVVnum = StringVar()
        Cvv = Entry(frame3, textvariable = self.CVVnum, width = 10)
        Cvv.pack(side = RIGHT)

        self.date = StringVar()
        if self.date < datetime.now():
            messagebox.showerror("Error, your card is expired.")

        expdate = Entry(frame4, textvariable = self.date, width = 10)
        expdate.pack(side = RIGHT)

        server = self.Connect()
        curosr = server.cursor()
        query = "INSERT INTO PAYMENT_INFO VALUES ('%d', '%d', '%s', '%s', '%s')" % (self.num.get(), self.CVVnum.get()), self.date.get(), self.name.get(), self.registeredUser.get())
        cursor.execute(query)

        b4=Button(frame5, text ="Submit", command = self.switchToMakeReservation)
        b4.pack(side=LEFT)

    def addCardCheck(self):
        expDate = datetime.strptime(self.expDate.get(), '%Y/%m/%d')
        server = self.Connect()
        cursor = server.cursor()
        query = "SELECT * FROM PAYMENT_INFORMATION \
               WHERE Card_Number = '%s'" % (self.cardNumber.get())
        cursor.execute(query)
        results = cursor.fetchall()
        if len(results) != 0:
            messagebox.showerror("Error", "Card number already in use")
        elif self.expDate.get() == "" or self.cardName.get() == "" or self.cardNumber.get() == "" or self.cvv.get() == "":
            messagebox.showerror("Error", "Expiration Date, Name, Number, and CVV must be filled")
        elif len(self.cardNumber.get()) != 10:
            messagebox.showerror("Error", "Card Number must be 10 digits")
        elif len(self.cvv.get()) != 3:
            messagebox.showerror("Error", "CVV must be 3 digits")
        elif expDate < datetime.now():
            messagebox.showerror("Error", "Card has already expired")
        else:
            server = self.Connect()
            cursor = server.cursor()
            query = "INSERT INTO PAYMENT_INFORMATION(Card_Number, Name, Exp_Date, CVV, Username) \
            VALUES ('%s', '%s', '%s', '%s', '%s')" % (self.cardNumber.get(), self.cardName.get(), self.expDate.get(),self.cvv.get(), self.name)
            print(query)
            cursor.execute(query)
            self.switchToConfirm1()

    def deleteCard(self):
        self.reservationWin.withdraw()
        self.paymentIWin2= Toplevel()
        self.paymentIWin2.title("Delete Card")

        frame = Frame(self.paymentIWin2)
        frame.pack(side=TOP)
        frame2 = Frame(self.paymentIWin2)
        frame2.pack(side=BOTTOM)
        cardNum= Label(frame, text = "Card Number")
        cardNum.pack(side=LEFT)

        server = self.Connect()
        cursor = server.cursor()
        query1 = "SELECT Card_Number FROM PAYMENT_INFO WHERE Username = '%s'" % (self.registeredUser.get())
        cursor.execute(query1)
        results = cursor.fetchall()

        self.cardNum = StringVar()
        self.cardNum.set(results[0])
        option=OptionMenu(frame, self.cardNum, results[0], *results)
        option.pack(side=RIGHT)

        query2 = "DELETE FROM PAYMENT_INFO WHERE Card_Number = '%s'" % (self.cardNum.get())
        cursor.execute(query2)

        b1=Button(frame2, text ="Submit", command = self.switchToMakeReservation2)
        b1.pack(side=BOTTOM)

    def switchToMakeReservation(self):
        self.paymentIWin.destroy()
        self.makeReservation()
    def switchToMakeReservation2(self):
        self.paymentIWin2.destroy()
        self.makeReservation()

    def deleteCardCheck(self):
        server = self.Connect()
        cursor = server.cursor()
        cursor.execute("SELECT * FROM PAYMENT_INFO WHERE Card_Number ='%s'" % (self.cardChoice.get()))
        results = cursor.fetchall()
        for row in results:
            self.endDate = row[2]
            endDate = datetime.strptime(self.expDate.get(), '%Y/%m/%d')
            if endDate > datetime.now():
                messagebox.showerror("Error", "Card is being used for existing reservation")
        cursor = server.cursor()
        cursor.execute("DELETE FROM PAYMENT_INFORMATION WHERE Card_Number='%s'" % (self.cardChoice.get()))
        self.switchToConfirm2()

    def switchToConfirm1(self):
        self.paymentIWin.withdraw()
        self.confirmation()

    def switchToConfirm2(self):
        self.paymentIWin2.withdraw()
        self.confirmation()

    def backToMain(self):
        self.confirm.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

    def confirmation(self):
        self.reservationWin.destroy()
        self.confirm = Toplevel()
        self.confirm.title("Confirmation")

        frame = Frame(self.confirm)
        frame.pack()

        label1 = Label(frame, text="Reservation ID:")
        label1.grid(row = 0, column = 0,sticky=E)
        e1 = Entry(frame, text = "Some ID # goes here", width = 10)
        e1.grid(row = 0, column = 1)
        label3 = Label(frame, text="Thank you so much for your purchase! Please save the reservation ID for your records.")
        label3.grid(row = 2, column = 0, columnspan = 2)

        server = self.Connect()
        cursor = server.cursor()
        query = "SELECT ReservationID FROM RESERVATION WHERE Card_Number = '%d'" % (self.card.get())
        cursor.execute(query)
        results = cursor.fetchall()

        b=Button(frame, text ="Go back to choose functionality", command=self.backToMain)
        b.grid(row=3,column=1,sticky=E)

    def updateReservation(self):
        self.primaryWindow.destroy()
        self.updateWin = Toplevel()
        self.updateWin.title("Update Reservation")

        frame = Frame(self.updateWin)
        frame.pack()
        self.resID = IntVar()
        l1 = Label(frame, text = "Reservation ID")
        l1.grid(row = 0, column = 0, sticky = E)
        e1 = Entry(frame, textvariable = self.resID, width = 10)
        e1.grid(row = 0, column = 1)
        b1 = Button(frame, text = "Search", command = self.updateReservation2)
        b1.grid(row = 0, column = 2, sticky = E)
        b2 = Button(frame, text = "Back", command = self.switchMainMenu)
        b2.grid(row = 1, column = 1, sticky = E)

        server = self.Connect()
        cursor = server.cursor()
        query = "SELECT ReservationID FROM RESERVES WHERE Passenger_Name = '%s'" % (self.name.get())
        cursor.execute(query)
        results = cursor.fetchall()

        if self.resID not in results:
            messagebox.showerror("Error. No such reservation found.")


    def switchMainMenu(self):
        self.updateWin.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

##    def updateTree(self, frame):
##        tree=Treeview(frame)
##        tree.pack()
##        tree["show"] = "headings"
##        tree["columns"]=("select","train","time","dept", "arrv", "class", "pr", "bag", "name")
##        tree.heading("select", text= "Select")
##        tree.heading("train", text= "Train (Train Number)")
##        tree.heading("time", text= "Time (Duration)")
##        tree.heading("dept", text= "Departs From")
##        tree.heading("arrv", text= "Arrives At")
##        tree.heading("class", text= "Class")
##        tree.heading("pr", text= "Price")
##        tree.heading("bag", text= "# of Baggages")
##        tree.heading("name", text= "Passenger Name")
##        return tree

#####################table info, new dept date, change fee, updated cost,#################
    def updateReservation2(self):
        self.updateWin.withdraw()
        self.updateWin2 = Toplevel()
        self.updateWin2.title("Update Reservation")

        frame = Frame(self.updateWin2)
        frame.pack()
        frame2 = Frame(self.updateWin2)
        frame2.pack()

        l0 = Label(frame,text = "Select").grid(row = 1, column = 0)
        l1 = Label(frame,text = "Train(Train Number)").grid(row = 1, column = 1)
        l2 = Label(frame,text = "Time(Duration)").grid(row = 1, column = 2)
        l3 = Label(frame,text = "Departs From").grid(row = 1, column = 3)
        l4 = Label(frame,text = "Arrives At").grid(row = 1, column = 4)
        l5 = Label(frame,text = "Class").grid(row = 1, column = 5)
        l6 = Label(frame,text = "Price").grid(row = 1, column =6)
        l7 = Label(frame,text = "# of baggages").grid(row = 1, column = 7)
        l8 = Label(frame,text = "Passenger Name").grid(row = 1, column = 8)

        server = self.Connect()
        cursor = server.cursor()
        query = "SELECT * FROM RESERVES WHERE ReservationID = '%s'" % (self.resID.get())
        cursor.execute(query)
        results = cursor.fetchall()

        a = 1
        b = 1
        c = 2
        self.w = IntVar()
        for result in results:
            b = Radiobutton(frame, text = "Select", variable = self.w, anchor= "w")
            b.grid(row = a, column = 0 , stickey = "ew")
            l10 = Label(frame, text = str(result[0]), anchor = "w")
            l10.grid(row = a, column = 1, sticky = "ew")
            l11 = Label(frame, text = str(result[1]), anchor = "w")
            l11.grid(row = a, column = 2, sticky = "ew")
            l12 = Label(frame, text = str(result[2]), anchor = "w")
            l12.grid(row = a, column = 3, sticky = "ew")
            l13 = Label(frame, text = str(result[3]), anchor = "w")
            l13.grid(row = a, column = 4, sticky = "ew")
            l14 = Label(frame, text = str(result[4]), anchor = "w")
            l14.grid(row = a, column = 5, sticky = "ew")
            l15 =Label(frame, text = str(result[5]), anchor = "w")
            l15.grid(row = a, column = 6, sticky = "ew")
            l16 = Label(frame, text = str(result[6]), anchor = "w")
            l16.grid(row = a, column = 7, sticky = "ew")
            l17 = Label(frame, text = str(result[7]), anchor = "w")
            l17.grid(row = a, column = 8, sticky = "ew")
            a = a + 1

        b1 = Button(frame2, text = "Back", command = self.switchUpdateReservation)
        b1.pack(side = LEFT)
        b2 = Button(frame2, text = "Next", command = self.updateReservation3)
        b2.pack(side = RIGHT)

    def switchUpdateReservation(self):
        self.updateWin2.destroy()
        #self.updateWin = Toplevel()
        self.updateReservation()

    def switchUpdateReservation2(self):
        self.updateWin3.destroy()
        self.updateReservation2()

    def updateTree2(self, frame):
        tree=Treeview(frame)
        tree.grid(row = 2, column = 0)
        tree["show"] = "headings"
        tree["columns"]=("train","time","dept", "arrv", "class", "pr", "bag", "name")
        tree.heading("train", text= "Train (Train Number)")
        tree.heading("time", text= "Time (Duration)")
        tree.heading("dept", text= "Departs From")
        tree.heading("arrv", text= "Arrives At")
        tree.heading("class", text= "Class")
        tree.heading("pr", text= "Price")
        tree.heading("bag", text= "# of Baggages")
        tree.heading("name", text= "Passenger Name")
        return tree

    def updateTree3(self, frame):
        tree=Treeview(frame)
        tree.grid(row = 4, column = 0, sticky = E)
        tree["show"] = "headings"
        tree["columns"]=("train","time","dept", "arrv", "class", "pr", "bag", "name")
        tree.heading("train", text= "Train (Train Number)")
        tree.heading("time", text= "Time (Duration)")
        tree.heading("dept", text= "Departs From")
        tree.heading("arrv", text= "Arrives At")
        tree.heading("class", text= "Class")
        tree.heading("pr", text= "Price")
        tree.heading("bag", text= "# of Baggages")
        tree.heading("name", text= "Passenger Name")
        return tree

    def updateReservation3(self):
        self.updateWin2.withdraw()
        self.updateWin3 = Toplevel()
        self.updateWin3.title("Update Reservation")

        frame = Frame(self.updateWin3)
        frame.pack()
        frame2 = Frame(self.updateWin3)
        frame2.pack()
        frame3 = Frame(self.updateWin3)
        frame3.pack()
        frame4 = Frame(self.updateWin3)
        frame4.pack()
        frame5 = Frame(self.updateWin3)
        frame5.pack()

        l1 = Label(frame, text = "Current Train Ticket")
        l1.grid(row = 1, column = 1, sticky = E)

        tree = self.updateTree2(frame2)

        newdepDate= Label(frame3,text ="New Departure Date")
        newdepDate.grid(row = 0, column = 0, sticky = E)
        self.date = StringVar()
        e1= Entry(frame3,textvariable = self.date, width = 10)
        e1.grid(row = 0, column = 1, sticky = EW)
        b1 = Button(frame3, text = "Search avaibility", command = self.trainSchedule)
        b1.grid(row = 0, column = 2, sticky = EW)

        l2 = Label(frame3, text = "Updated Train Ticket")
        l2.grid(row = 1, column = 1, sticky = E)

        tree2 = self.updateTree3(frame4)

        changeFee = Label(frame5,text ="Change Fee")
        changeFee.grid(row = 0, column = 0, sticky = E)
        self.value = StringVar()
        e2 = Entry(frame5,textvariable = self.value, width = 10)
        e2.grid(row = 0, column = 1, sticky = E)
        updatedCost = Label(frame5,text ="Updated Total Cost")
        updatedCost.grid(row = 1, column = 0, sticky = E)
        e3 = Entry(frame5, textvariable = self.value, width = 10)
        e3.grid(row = 1, column = 1)

        b2=Button(frame5, text ="Back", command = self.switchUpdateReservation2)
        b2.grid(row =2, column = 0, sticky = E)
        b3=Button(frame5, text ="Submit", command = self.switchTOConfirmation)
        b3.grid(row =2, column = 1, sticky = E)

    def switchTOConfirmation(self):
        self.updateWin3.destroy()
        self.confirmation()

################## reservation id search, table/ total cost, date, amount to be refunded#######################
    def cancelRes(self):
        self.primaryWindow.withdraw()
        self.cancelWin = Toplevel()
        self.cancelWin.title("Cancel Reservation")

        frame = Frame(self.cancelWin)
        frame.pack()

        l1 = Label(frame, text = "Reservation ID")
        l1.grid(row = 0, column = 0, sticky = E)
        e1 = Entry(frame, width = 10)
        e1.grid(row = 0, column = 1)
        b1 = Button(frame, text = "Search", command = self.cancelRes2)
        b1.grid(row = 0, column = 2, sticky = E)
        b2 = Button(frame, text = "Back", command = self.switchToMain)
        b2.grid(row = 1, column = 1, sticky = E)
    def switchToMain(self):
        self.cancelWin.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

    def updateTree4(self, frame):
        tree=Treeview(frame)
        tree.grid(row = 0, column = 0, sticky = E)
        tree["show"] = "headings"
        tree["columns"]=("train","time","dept", "arrv", "class", "pr", "bag", "name")
        tree.heading("train", text= "Train (Train Number)")
        tree.heading("time", text= "Time (Duration)")
        tree.heading("dept", text= "Departs From")
        tree.heading("arrv", text= "Arrives At")
        tree.heading("class", text= "Class")
        tree.heading("pr", text= "Price")
        tree.heading("bag", text= "# of Baggages")
        tree.heading("name", text= "Passenger Name")
        return tree

    def cancelRes2(self):
        self.cancelWin.destroy()
        self.cancelWin2 = Toplevel()
        self.cancelWin2.title("Cancel Reservation")

        frame = Frame(self.cancelWin2)
        frame.pack()
        frame2 = Frame(self.cancelWin2)
        frame2.pack()
        frame3 = Frame(self.cancelWin2)
        frame3.pack()

        tree = self.updateTree4(frame)

        l1= Label(frame2,text ="Total Cost of Reservation")
        l1.grid(row = 1, column = 0, sticky = E)
        self.cost = StringVar()
        e1= Entry(frame2,textvariable = self.cost, width = 10)
        e1.grid(row = 1, column = 1, sticky = EW)

        l2 = Label(frame2, text = "Date of Cancellation")
        l2.grid(row = 2, column = 0, sticky = E)
        self.date = StringVar()
        e2= Entry(frame2,textvariable = self.date, width = 10)
        e2.grid(row = 2, column = 1, sticky = EW)

        l3 = Label(frame2, text = "Amount to be Refunded")
        l3.grid(row = 3, column = 0, sticky = E)
        self.amount = StringVar()
        e2= Entry(frame2,textvariable = self.amount, width = 10)
        e2.grid(row = 3, column = 1, sticky = EW)

        b2=Button(frame3, text ="Back", command = self.switchCancelRes1)
        b2.grid(row =4, column = 0, sticky = E)
        b3=Button(frame3, text ="Submit", command = self.switchTC)
        b3.grid(row =4, column = 1, sticky = E)
    def switchCancelRes1(self):
        self.cancelWin2.destroy()
        self.cancelRes()
    def switchTC(self):
        self.cancelWin2.destroy()
        self.confirmation()

############train number,table info
    def viewReview(self):
        self.primaryWindow.withdraw()
        self.viewReviewWin = Toplevel()
        self.viewReviewWin.title("View Review")

        frame = Frame(self.viewReviewWin)
        frame.pack()

        l1 = Label(frame, text = "Train Number")
        l1.grid(row = 0, column = 0, sticky = W)
        e1 = Entry(frame, width = 20)
        e1.grid(row = 0, column = 1)
        b1 = Button(frame, text = "Back", command = self.backMain)
        b1.grid(row = 1, column = 0)
        b2 = Button(frame, text = "Next", command = self.viewReview2)
        b2.grid(row = 1, column = 1)
    def backMain(self):
        self.viewReviewWin.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

    def viewTree(self, frame):
        tree=Treeview(frame)
        tree.pack()
        tree["show"] = "headings"
        tree["columns"]=("select","train","time","dept", "arrv", "class", "pr", "bag", "name")
        tree.heading("select", text= "Select")
        tree.heading("train", text= "Train (Train Number)")
        tree.heading("time", text= "Time (Duration)")
        tree.heading("dept", text= "Departs From")
        tree.heading("arrv", text= "Arrives At")
        tree.heading("class", text= "Class")
        tree.heading("pr", text= "Price")
        tree.heading("bag", text= "# of baggages")
        tree.heading("name", text= "Passenger Name")
        return tree

    def viewReview2(self):
        self.viewReviewWin.withdraw()
        self.viewReviewWin2 = Toplevel()
        self.viewReviewWin2.title("View Review")

        frame = Frame(self.viewReviewWin2)
        frame.pack()

        tree = self.viewTree(frame)

        b1 = Button(frame, text = "Back to Choose Functionality", command = self.switchMainMenu)
        b1.pack(side = BOTTOM)

    def switchMainMenu(self):
        self.viewReviewWin2.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

    def giveReview(self):
        self.primaryWindow.destroy()
        self.giveReviewWin = Toplevel()
        self.giveReviewWin.title("Give Review")

        frame = Frame(self.giveReviewWin)
        frame.pack()

        self.trainNo = StringVar()
        l1 = Label(frame, text = "Train Number")
        l1.grid(row = 0, column = 0, sticky = W)
        e1 = Entry(frame, text = self.trainNo, width = 20)
        e1.grid(row = 0, column = 1)

        l2 = Label(frame, text = "Rating")
        l2.grid(row = 1, column = 0, sticky = W)
        self.rating = StringVar()
        choices = ["Very Good", "Good", "Neutral", "Bad", "Very Bad"]
        self.rating.set(choices[0])
        option=OptionMenu(frame, self.rating, choices[0], *choices)
        option.grid(row = 1, column = 1)

        self.comment = StringVar()
        l3 = Label(frame, text = "Comment")
        l3.grid(row = 2, column = 0, sticky = W)
        e3 = Entry(frame, text = self.comment, width = 20)
        e3.grid(row = 2, column = 1)

        b1=Button(frame, text ="Submit", command = self.mainBack)
        b1.grid(row = 3, column = 1)
    ################ check to see if the train number is valid###############################
    def mainBack(self):
        if self.trainNo == "":
            messagebox.showerror("Error", "Enter a train number")
        ######elif ##train number isnt correct:
        else:
            self.giveReviewWin.destroy()
            self.primaryWindow = Toplevel()
            self.mainMenu()
            ###########write the rating to a DB#################


    def viewTree2(self, frame):
        tree=Treeview(frame)
        tree.pack()
        tree["show"] = "headings"
        tree["columns"]=("mon","rev")
        tree.heading("mon", text= "Month")
        tree.heading("rev", text= "Revenue")
        return tree

    def viewRevenueRep(self):
        self.primaryWindow.withdraw()
        self.viewRevenueReport = Toplevel()
        self.viewRevenueReport.title("View Revenue Report")

        frame = Frame(self.viewRevenueReport)
        frame.pack()

        tree = self.viewTree2(frame)
        b1 = Button(frame, text = "Back", command = self.switchMain)
        b1.pack(side = BOTTOM)

    def switchMain(self):
        self.viewRevenueReport.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

    def viewTree3(self, frame):
        tree=Treeview(frame)
        tree.pack()
        tree["show"] = "headings"
        tree["columns"]=("mon","num","rsv")
        tree.heading("mon", text= "Month")
        tree.heading("num", text= "Train number")
        tree.heading("rsv", text= "#of Reservations")
        return tree

    def viewpopRR(self):
        self.primaryWindow.withdraw()
        self.viewpopRRWin = Toplevel()
        self.viewpopRRWin.title("View Popular Route Report")
        frame = Frame(self.viewpopRRWin)
        frame.pack()

        tree = self.viewTree3(frame)

        b1 = Button(frame, text = "Back", command = self.swtMain)
        b1.pack(side = BOTTOM)

    def swtMain(self):
        self.viewpopRRWin.destroy()
        self.primaryWindow = Toplevel()
        self.mainMenu()

mw = Tk()
app = Phase_three(mw)
mw.mainloop()
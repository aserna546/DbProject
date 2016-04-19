#Arthi Nithi, Anjani Agrawal, Alan Chiang, Alaap Murali

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import pymysql
import calendar

class Phase_three:
    def __init__(self,primaryWin):
        self.primaryWin = primaryWin
        self.Login()

        self.newUserWindow = Toplevel()
        self.Register()
        self.newUserWindow.title("New User Registration")
        self.newUserWindow.withdraw()
#        self.newUserWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.primaryWindow = Toplevel()
        self.primaryWindow.title("Welcome "+self.username.get())
        self.primaryWindow.withdraw()
 #       self.primaryWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.schoolInfoWin= Toplevel()
        self.schoolInfoWin.title("Add School Info")
        self.schoolInfoWin.withdraw()
  #      self.schoolInfo.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.trainSchWin= Toplevel()
        self.trainSchWin.title("View Train Schedule")
        self.trainSchWin.withdraw()
   #     self.trainSchWin.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.scheduleWin= Toplevel()
        self.scheduleWin.title("View Train Schedule")
        self.scheduleWin.withdraw()
    #    self.scheduleWin.protocol("WM_DELETE_WINDOW", self.closeWindow)


        self.findAvailWindow= Toplevel()
        self.findAvailWindow.title("Search Train")
        self.findAvailWindow.withdraw()
     #   self.findAvailWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.departureWin = Toplevel()
        self.departureWin.title("Select Departure")
        self.departureWin.withdraw()
      #  self.departureWin.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.passengerInfoWin = Toplevel()
        self.passengerInfoWin.title("Travel Extras & Passenger Info")
        self.passengerInfoWin.withdraw()
       # self.passengerInfoWin.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.reservationWin = Toplevel()
        self.reservationWin.title("Make Reservation")
        self.reservationWin.withdraw()
        #self.reservationWin.protocol("WM_DELETE_WINDOW", self.closeWindow)

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

        b1=Button(frame2, text ="Login", command=self.switchtoMainMenu)
        b1.pack(side=LEFT)
        b2=Button(frame2, text ="Register", command= self.switchToRegister)
        b2.pack(side=LEFT)

    def loginCredentials(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "Invalid input")
            return

        server = self.Connect()
        cursor = server.cursor()
        query = "SELECT * FROM CUSTOMER \
               WHERE Username = '%s' AND Password = '%s'" % (self.username.get(), self.password.get())
        cursor.execute(query)
        result1 = cursor.fetchall()
        query = "SELECT * FROM MANAGER \
               WHERE Username = '%s' AND Password = '%s'" % (self.username.get(), self.password.get())

        cursor.execute(query)
        result2 = cursor.fetchall()

        if len(result1) != 0:
            print("Customer")
            self.custOrManag = "customer"
            for row in results:
                self.name = row[0]
            self.switchtoMainMenu()
        elif len(result2) != 0:
            self.custOrManag = "manager"
            for row in results1:
                self.name = row[0]
            self.switchtoMainMenu()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def mainMenu(self):
        self.primaryWindow.title("Choose Functionality ")
        buttonsFrame = Frame(self.primaryWindow)
        buttonsFrame.pack()
        #if self.custOrManag == "customer":
        ###""""
        b1 = Button(buttonsFrame, text ="View Train Schedule", command = self.trainSchedule)
        b1.grid(row = 0, column = 0, columnspan = 2, sticky = EW)
        b2 = Button(buttonsFrame, text ="Make a new reservation", command = self.searchTrain)
        b2.grid(row = 1, column = 0, columnspan = 2, sticky = EW)
        b3 = Button(buttonsFrame, text ="Update a reservation", command = self.updateReservation)
        b3.grid(row = 2, column = 0, columnspan = 2, sticky = EW)
        b4 = Button(buttonsFrame, text ="Cancel a reservation", command = self.cancelRes)
        b4.grid(row = 3, column = 0, columnspan = 2, sticky = EW)
        b5 = Button(buttonsFrame, text ="Give review", command = self.viewReview)
        b5.grid(row = 4, column = 0, columnspan = 2, sticky = EW)
        b6 = Button(buttonsFrame, text ="Add school information (student discount)", command = self.schoolInfo)
        b6.grid(row = 5, column = 0, columnspan = 2, sticky = EW)
        b7 = Button(buttonsFrame, text ="Log out")
        b7.grid(row = 6, column = 0, columnspan = 2, sticky = EW)
        
       ### elif self.custOrManag == "manager":
        """b8 = Button(buttonsFrame, text ="View revenue report", command = self.viewRevenueRep)
        b8.grid(row = 0, column = 0, columnspan = 2, sticky = EW)
        b9 = Button(buttonsFrame, text ="View popular route report", command = self.viewpopRR)
        b9.grid(row = 1, column = 0, columnspan = 2, sticky = EW)
        b10=Button(buttonsFrame, text ="Log out")#, command = s
        b10.grid(row = 2, column = 0, columnspan = 2, sticky = EW)"""

    def switchToRegister(self):
        self.primaryWin.withdraw()
        self.newUserWindow.deiconify()

    def switchToLogin(self):
        self.newUserWindow.withdraw()
        self.primaryWin.deiconify()

    def switchtoMainMenu(self):
        self.primaryWin.withdraw()
        self.primaryWindow.deiconify()
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

        b_reg=Button(frame2, text ="Create")
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
        print(query1)
        cursor.execute(query1)
        result1 = cursor.fetchall()
        print(result1)
        cursor.execute(query1)
        if len(result1) != 0:
            messagebox.showerror("Error", "Username already in use")
            return

        query2 = "INSERT INTO CUSTOMER(Username, Password, Email) \
               VALUES ('%s', '%s', '%s')" % (self.registeredUser.get(), self.registeredPass.get(), self.registerEmail.get())
        print(query2)
        cursor.execute(query2)
        result2 = cursor.fetchall()
        self.switchToLogin()

    def schoolInfo(self):
        self.primaryWindow.withdraw()
        self.schoolInfoWin.deiconify()
        self.schoolInfoWin.title("Add School Info")
        frame1 = Frame(self.schoolInfoWin)
        frame2 = Frame(self.schoolInfoWin)
        frame1.pack(side = TOP)
        frame2.pack(side = BOTTOM)
        self.emailaddress = StringVar()
        self.entry = Entry(frame1, textvariable = self.emailaddress, width = 30)
        self.entry.pack(side=RIGHT)
        label1 = Label(frame1,text = "School Email Address")
        label1.pack(side=TOP)
        label2 = Label(frame1,text = "Your school email adress ends with .edu")
        label2.pack(side=BOTTOM)

        b1 = Button(frame2, text ="Back")
        b1.pack(side=LEFT)
        b2 = Button(frame2, text ="Submit")
        b2.pack(side=RIGHT)

    def trainSchedule(self):
        self.primaryWindow.withdraw()
        self.trainSchWin.deiconify()
        self.trainSchWin.title("View Train Schedule")
        frame1 = Frame(self.trainSchWin)
        frame2 = Frame(self.trainSchWin)
        frame1.pack(side = TOP)
        frame2.pack(side = BOTTOM)
        label1 = Label(frame1,text = "Train Number")
        label1.pack(side=LEFT)

        self.trainName = StringVar()
        self.entry = Entry(frame1, textvariable = self.trainName , width = 10)
        self.entry.pack(side=RIGHT)

        b1 = Button(frame2, text ="Search", command = self.schedule)
        b1.pack(side=LEFT)


######################Remember to fix the back button functionality#############################################
        

    def getTrainTree(self, frame):
        tree=Treeview(frame)
        tree.pack()

        tree["columns"]=("train","arrv","dept","station")
        tree.heading("train", text= "Train (Train Number)")
        tree.heading("arrv", text= "Arrival Time")
        tree.heading("dept", text= "Departure Time")
        tree.heading("station", text= "Station")
        return tree

    def schedule(self):
        self.trainSchWin.withdraw()
        self.scheduleWin.deiconify()
        self.scheduleWin.title("View Train Schedule")

        frame1 = Frame(self.scheduleWin)
        frame1.pack()
        frame2 = Frame(self.scheduleWin)
        frame2.pack()

        tree = self.getTrainTree(frame1)
        chosenTrain = self.trainName.get()
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

        b1 = Button(frame1, text ="Back", command = self.switchtotrainSchedule)
        b1.pack(side= TOP)

    def switchtotrainSchedule(self):
        self.scheduleWin.withdraw()
        self.trainSchWin.deiconify()
        #self.mainMenu()

    def searchTrain(self):
        self.primaryWindow.withdraw()
        self.findAvailWindow.deiconify()

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
        location.pack(side=LEFT)
        self.city = StringVar()
        choices = ["Atlanta", "Charlotte", "Savannah", "Orlando", "Miami"]
        self.city.set(choices[0])
        option=OptionMenu(frame, self.city, choices[0], *choices)
        option.pack(side=RIGHT)

        arriveAt= Label(frame1,text ="Arrive At")
        arriveAt.pack(side=LEFT)
        self.arrv = StringVar()
        choices = ["Atlanta", "Charlotte", "Savannah", "Orlando", "Miami"]
        self.arrv.set(choices[0])
        option=OptionMenu(frame1, self.arrv, choices[0], *choices)
        option.pack(side=RIGHT)

        depDate= Label(frame2,text ="Departure Date")
        depDate.pack(side=LEFT)
        self.date = StringVar()
        start_date= Label(frame2,text ="Start Date (MM/DD/YYYY)")
        self.startDateEntry = Entry(frame2, textvariable = self.date, width = 10)
        self.startDateEntry.pack(side = RIGHT)
# add calendar

        b=Button(frame3, text ="Find Trains", command = self.departureInfo)
        b.pack(side=RIGHT)

    def departTree(self, frame):
        tree=Treeview(frame)
        tree.pack()

        tree["columns"]=("train","time","1st","2nd")
        tree.heading("train", text= "Train (Train Number)")
        tree.heading("time", text= "Time (Duration)")
        tree.heading("1st", text= "1st Class Price")
        tree.heading("2nd", text= "2nd Class Price")
        return tree

    def departureInfo(self):
        self.findAvailWindow.withdraw()
        self.departureWin.deiconify()
        self.departureWin.title("Select Departure")

        frame = Frame(self.departureWin)
        frame.pack(side=TOP)

        tree = self.departTree(frame)
        chosenCity = self.city.get()
        chosenArrv = self.arrv.get()
        chosenDate = self.date.get()
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

        b1=Button(frame, text ="Back")
        b1.pack(side=LEFT)
        b2=Button(frame, text ="Next", command = self.passengerInfo)
        b2.pack(side=RIGHT)

    def switchtoMain2(self):
        self.passengerInfoWin.withdraw()
        self.primaryWindow.deiconify()

    def passengerInfo(self):
        self.departureWin.withdraw()
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

        baggage= Label(frame,text = "Number of Baggage")
        baggage.pack(side=LEFT)
        self.city = StringVar()
        choices = ["1", "2", "3", "4"]
        self.city.set(choices[0])
        option=OptionMenu(frame, self.city, choices[0], *choices)
        option.pack(side=RIGHT)
        disclamer = Label(frame2,text = "Every passenger can bring upto 4 baggage. 2 free of charge, 2 for $30 per bag")
        disclamer.pack()

        passName= Label(frame3,text ="Passenger Name")
        passName.pack(side=LEFT)
        name = StringVar()
        nameEnt = Entry(frame3, textvariable = name, width = 10)
        nameEnt.pack(side = RIGHT)

        b1=Button(frame4, text ="Back")
        b1.pack(side=LEFT)
        b2=Button(frame4, text ="Next", command=self.makeReservation)
        b2.pack(side=RIGHT)

    def selectTree(self, frame):
        tree=Treeview(frame)
        tree.pack()

        tree["columns"]=("train","time","dept","arrv", "class", "pr", "bag", "name", "rem")
        tree.heading("train", text= "Train (Train Number)")
        tree.heading("time", text= "Time (Duration)")
        tree.heading("dept", text= "Departs From")
        tree.heading("arrv", text= "Arrives At")
        tree.heading("class", text= "Class")
        tree.heading("pr", text= "Price")
        tree.heading("bag", text= "# of baggages")
        tree.heading("name", text= "Passenger Name")
        tree.heading("rem", text= "Remove")
        return tree


    def makeReservation(self):
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
        frame4.pack(side= TOP)
        frame5 = Frame(self.reservationWin)
        frame5.pack(side=BOTTOM)

        selected= Label(frame,text = "Currently Selected")
        selected.pack(side=LEFT)

        tree = self.selectTree(frame)

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

        stuDis= Label(frame,text = "Student Discount Applied.")
        stuDis.pack(side= BOTTOM)
        totalC= Label(frame2, text = "Total Cost")
        totalC.pack(side=LEFT)
        cost = StringVar()
        costEnt = Entry(frame2, textvariable = cost, width = 10)
        costEnt.pack(side = RIGHT)

        useCard= Label(frame3, text = "Use Card")
        useCard.pack(side=LEFT)
        choices = ["1", "2", "3", "4"]
        self.city.set(choices[0])
        option=OptionMenu(frame3, self.city, choices[0], *choices)
        option.pack(side=LEFT)

        b5=Button(frame3, text ="Delete Card", command = self.deleteCard)
        b5.pack(side=RIGHT)
        b1=Button(frame3, text ="Add Card", command = self.addCard)
        b1.pack(side=RIGHT)

        b2=Button(frame4, text ="Continue adding a train")
        b2.pack(side=LEFT)

        b3=Button(frame5, text ="Back")
        b3.pack(side=LEFT)
        b4=Button(frame5, text ="Submit")
        b4.pack(side=RIGHT)
 #calculations line

    def addCard(self):
        self.reservationWin.withdraw()
        self.paymentIWin.deiconify()
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

        name = StringVar()
        cardName = Entry(frame, textvariable = name, width = 10)
        cardName.pack(side = RIGHT)

        num = StringVar()
        cardNum = Entry(frame2, textvariable = num, width = 10)
        cardNum.pack(side = RIGHT)

        CVVnum = StringVar()
        Cvv = Entry(frame3, textvariable = CVVnum, width = 10)
        Cvv.pack(side = RIGHT)

        date = StringVar()
        expdate = Entry(frame4, textvariable = date, width = 10)
        expdate.pack(side = RIGHT)

        b4=Button(frame5, text ="Submit", command = self.switchToConfirm1)
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
        self.paymentIWin2.deiconify()
        self.paymentIWin2.title("Delete Card")

        frame = Frame(self.paymentIWin2)
        frame.pack(side=TOP)
        frame2 = Frame(self.paymentIWin2)
        frame2.pack(side=BOTTOM)
        cardNum= Label(frame, text = "Card Number")
        cardNum.pack(side=LEFT)
        choices = ["1", "2", "3", "4"]
        self.cardNum = StringVar()
        self.cardNum.set(choices[0])
        option=OptionMenu(frame, self.cardNum, choices[0], *choices)
        option.pack(side=RIGHT)

        b1=Button(frame2, text ="Submit", command = self.switchToConfirm2)
        b1.pack(side=BOTTOM)
        
    def deleteCardCheck(self):
        server = self.Connect()
        cursor = server.cursor()
        cursor.execute("SELECT * FROM PAYMENT_INFO WHERE Card_Number ='%s'" %(self.cardChoice.get()))
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
        self.confirm.withdraw()
        self.primaryWindow.deiconify()

    def confirmation(self):
        self.confirm.deiconify()
        self.confirm.title("Confirmation")

        frame = Frame(self.confirm)
        frame.pack()

        label1 = Label(frame, text="Reservation ID:")
        label1.grid(row = 0, column = 0,sticky=E)
        e1 = Entry(frame, text = "Some ID # goes here", width = 10)
        e1.grid(row = 0, column = 1)
##        label2 = Label(frame, text=self.rid)
##        label2.grid(row = 1, column = 0,sticky=E)

        label3 = Label(frame, text="Thank you so much for your purchase! Please save the reservation ID for your records.")
        label3.grid(row = 2, column = 0, columnspan = 2)

        b=Button(frame, text ="Back", command=self.backToMain)
        b.grid(row=3,column=1,sticky=E)

    def updateReservation(self):
        self.primaryWindow.withdraw()
        self.updateWin.deiconify()
        self.updateWin.title("Update Reservation")

        frame = Frame(self.updateWin)
        frame.pack()

        l1 = Label(frame, text = "Reservation ID")
        l1.grid(row = 0, column = 0, sticky = E)
        e1 = Entry(frame, width = 10)
        e1.grid(row = 0, column = 1)
        b1 = Button(frame, text = "Search", command = self.updateReservation2)
        b1.grid(row = 0, column = 2, sticky = E)
        b2 = Button(frame, text = "Back")
        b2.grid(row = 1, column = 1, sticky = E)

    def updateTree(self, frame):
        tree=Treeview(frame)
        tree.pack()

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

    def updateReservation2(self):
        self.updateWin.withdraw()
        self.updateWin2.deiconify()
        self.updateWin2.title("Update Reservation")

        frame = Frame(self.updateWin2)
        frame.pack()
        frame2 = Frame(self.updateWin2)
        frame2.pack()

        tree = self.updateTree(frame)

        b1 = Button(frame2, text = "Back")
        b1.pack(side = LEFT)
        b2 = Button(frame2, text = "Next", command = self.updateReservation3)
        b2.pack(side = RIGHT)

    def updateReservation3(self):
        self.updateWin2.withdraw()
        self.updateWin3.deiconify()
        self.updateWin3.title("Update Reservation")

        frame = Frame(self.updateWin2)
        frame.pack()

        print("Update Res 3")
        

    def cancelRes(self):
        self.primaryWindow.withdraw()
        self.cancelWin.deiconify()
        self.cancelWin.title("Cancel Reservation")

        frame = Frame(self.cancelWin)
        frame.pack()

        l1 = Label(frame, text = "Reservation ID")
        l1.grid(row = 0, column = 0, sticky = E)
        e1 = Entry(frame, width = 10)
        e1.grid(row = 0, column = 1)
        b1 = Button(frame, text = "Search", command = self.cancelRes2)
        b1.grid(row = 0, column = 2, sticky = E)
        b2 = Button(frame, text = "Back")
        b2.grid(row = 1, column = 1, sticky = E)

        
    def cancelRes2(self):
        self.cancelWin.withdraw()
        self.cancelWin2.deiconify()
        self.cancelWin2.title("Cancel Reservation")

        frame = Frame(self.cancelWin2)
        frame.pack()

        print("Cancel Res 2")
        

    
    
    def viewReview(self):
        self.primaryWindow.withdraw()
        self.viewReviewWin.deiconify()
        self.viewReviewWin.title("View Review")

        frame = Frame(self.viewReviewWin)
        frame.pack()

        l1 = Label(frame, text = "Train Number")
        l1.grid(row = 0, column = 0, sticky = W)
        e1 = Entry(frame, width = 20)
        e1.grid(row = 0, column = 1)
        b1 = Button(frame, text = "Back")
        b1.grid(row = 1, column = 0)
        b2 = Button(frame, text = "Next", command = self.viewReview2)
        b2.grid(row = 1, column = 1)

    def viewTree(self, frame):
        tree=Treeview(frame)
        tree.pack()

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
        self.viewReviewWin2.deiconify()
        self.viewReviewWin2.title("View Review")

        frame = Frame(self.viewReviewWin2)
        frame.pack()

        tree = self.viewTree(frame)
        
        b1 = Button(frame, text = "Back to Choose Functionality")
        b1.pack(side = BOTTOM)

####new

    def giveReview(self):
        self.giveReviewWin.withdraw()
        self.giveReviewWin.deiconify()
        self.viewReviewWin.title("Give Review")

        frame = Frame(self.giveReviewWin)
        frame.pack()
        
        l1 = Label(frame, text = "Train Number")
        l1.grid(row = 0, column = 0, sticky = W)
        e1 = Entry(frame, width = 20)
        e1.grid(row = 0, column = 1)

        l2 = Label(frame, text = "Rating")
        l2.grid(row = 1, column = 0, sticky = W)
        self.rating = StringVar()
        choices = ["Very Good", "Good", "Neutral", "Bad", "Very Bad"]
        self.rating.set(choices[0])
        option=OptionMenu(frame, self.rating, choices[0], *choices)
        option.grid(row = 0, column = 1)
        
        l3 = Label(frame, text = "Comment")
        l3.grid(row = 2, column = 0, sticky = W)
        e3 = Entry(frame, width = 20)
        e3.grid(row = 2, column = 1)

        b1=Button(frame, text ="Submit")#, command = )
        b1.pack(side=BOTTOM)

    def viewTree2(self, frame):
        tree=Treeview(frame)
        tree.pack()

        tree["columns"]=("mon","rev")
        tree.heading("mon", text= "Month")
        tree.heading("rev", text= "Revenue")
        return tree
    
    def viewRevenueRep(self):
        self.primaryWindow.withdraw()
        self.viewRevenueReport.deiconify()
        self.viewRevenueReport.title("View Revenue Report")

        frame = Frame(self.viewRevenueReport)
        frame.pack()

        tree = self.viewTree2(frame)
        b1 = Button(frame, text = "Back")
        b1.pack(side = BOTTOM)

    def viewTree3(self, frame):
        tree=Treeview(frame)
        tree.pack()
        tree["columns"]=("mon","num","rsv")
        tree.heading("mon", text= "Month")
        tree.heading("num", text= "Train number")
        tree.heading("rsv", text= "#of Reservations")
        return tree

    def viewpopRR(self):
        self.primaryWindow.withdraw()
        self.viewpopRRWin.deiconify()
        self.viewpopRRWin.title("View Popular Route Report")
        frame = Frame(self.viewpopRRWin)
        frame.pack()

        tree = self.viewTree3(frame)                

        b1 = Button(frame, text = "Back")
        b1.pack(side = BOTTOM)

mw = Tk()
app = Phase_three(mw)
mw.mainloop()

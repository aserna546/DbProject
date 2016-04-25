from random import randrange
from re import findall
from tkinter import *
import urllib.request
import datetime
import pymysql
from tkinter import messagebox
import re

import review
import reportFinal
import makeReservation
import upDateReservation
import cancelReservation
import isStudentInfo
class Train:

    def __init__(self, window):
        self.usernameInput = StringVar()
        self.window = window
        self.loginScreen()
        #self.window.withdraw()
        self.register = Toplevel()
        self.register.minsize(400,400)
        # Register page
        self.registerPage()
        self.register.withdraw()
        # Train Schedule
        #main window
        self.mainFrame = Toplevel()
        self.mainFrame.minsize(400,400)
        self.mainPage()
        self.mainFrame.withdraw()
        #makeReservation.GUI()


    def loginScreen(self):
        # window setup
        self.window.title("Train Login")
        LabelFrame = Frame(self.window)
        LabelFrame.pack(fill = 'both', expand = 'yes')
        username = Label(LabelFrame, text = "Username :")
        loginTitle = Label(LabelFrame, text = "Login", font = ("Arial", 50))
        loginTitle.place(x = 140, y = 10)
        password = Label(LabelFrame, text = "Password :")
        password.place(x = 0, y = 140)
        username.place(x = 0, y = 100)
        self.passwordInput = StringVar()
        entryUser = Entry(LabelFrame, textvariable = self.usernameInput, width = 30)
        entryPass = Entry(LabelFrame, textvariable = self.passwordInput, width = 30)
        entryUser.place(x = 80, y = 100)
        entryPass.place(x = 80, y = 140)
        loginB = Button(LabelFrame, text = "login", command =self.checkLogin)
        registerB = Button(LabelFrame, text = "register", command = self.registerPageShow)
        loginB.place(x = 100, y = 180)
        registerB.place(x = 200, y = 180)

    def connect(self):
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu",
                             user="cs4400_Team_39",
                             passwd="HSaWNuO5",
                             db="cs4400_Team_39")
        return db

    def gotoCancelReservation(self):
        cancelPage = Toplevel()
        self.mainFrame.withdraw()
        cancelReservation.GUI(cancelPage, self.mainFrame)


    def gotoReviewsPage(self):
        reviewWindow = Toplevel()
        review.GUI(reviewWindow, self.usernameInput, self.mainFrame)
        self.mainFrame.withdraw()

    def gotoMakeReservation(self):
        self.mainFrame.withdraw()
        makeReservation.GUI(self.usernameInput)

    def goupDateReservation(self):
        self.mainFrame.withdraw()
        updateReservationWin = Toplevel()
        upDateReservation.GUI(updateReservationWin, self.mainFrame)

    def goToAddSchool(self):
        self.mainFrame.withdraw()
        addSchoolWin = Toplevel()
        isStudentInfo.GUI(addSchoolWin, self.usernameInput, self.mainFrame)
    def mainPage(self):
        self.mainFrame.title("Home Page")
        labelF = Frame(self.mainFrame)
        labelF.pack(fill = 'both', expand = 'yes')
        mainTitle = Label(labelF, text = "Choose Functionality", font = ("Arial", 40))
        viewTrains = Button(labelF, text="View Train Schedule", fg = 'blue',
                            underline = 1, font = ("Arial", 10), command=self.TrainNumberSearch)
        logout = Button(labelF, text="Log Out", fg='blue',
                            underline=1, command=self.goBackToLogin, font=("Arial", 10))
        giveReview = Button(labelF, text="Give Review", fg='blue',
                            underline=1, command=self.gotoReviewsPage, font=("Arial", 10))
        makeReservation = Button(labelF, text="Make Reservation", fg='blue',
                            underline=1, command=self.gotoMakeReservation, font=("Arial", 10))
        updaterev = Button(labelF, text="Update Reservation", fg='blue',
                                 underline=1, command=self.goupDateReservation, font=("Arial", 10))
        canelrev = Button(labelF, text="Cancel Reservation", fg='blue',
                           underline=1, command=self.gotoCancelReservation, font=("Arial", 10))
        addschool = Button(labelF, text="addSchool Info", fg='blue',
                          underline=1, command=self.goToAddSchool, font=("Arial", 10))

        mainTitle.place(x=20, y=10)
        viewTrains.place(x=140, y=100)
        giveReview.place(x=140, y=150)
        makeReservation.place(x=140, y=190)
        updaterev.place(x=140, y=230)
        canelrev.place(x=140, y=270)
        addschool.place(x=140, y=310)
        logout.place(x=140, y=370)


    def checkLogin(self):
        cursor = self.connect().cursor()
        sql = "SELECT * FROM User WHERE Username = '%s' \
              AND Password = '%s'" % (self.usernameInput.get(), self.passwordInput.get())
        sql2 = "SELECT Username FROM Customer WHERE Username= '%s'" % (self.usernameInput.get())
        validUser = cursor.execute(sql)
        validCustomer = cursor.execute(sql2)
        #
        if validUser == 1 and validCustomer == 1:
            messagebox.showinfo("Success", "Login Successful")
            self.window.withdraw()
            self.mainFrame.deiconify()
        elif validUser == 1:
            messagebox.showinfo("Success", "Manager Login")
            self.window.withdraw()
            reportWindow = Toplevel()
            reportFinal.GUI(reportWindow, self.window)

        else:
            messagebox.showerror("Error", "Username or password incorrect")

    def registerUser(self):
        cursor = self.connect().cursor()
        sql = "SELECT Username From User Where Username = '%s'" % (self.inputUser.get())
        usernameCheck = cursor.execute(sql)
        email1 = self.inputEmail.get()
        validateEmail = re.match(r'\w[\w\.-]*@\w[\w\.-]+\.\w+', email1)
        # passwords dont match
        if self.inputPass.get() != self.inputConfirmPass.get():
            messagebox.showerror("Error", "Passwords don't match")
        # checking if ursername valid
        elif usernameCheck != 0:
            messagebox.showerror("Error", "Username Already exists")
        # invalid email
        elif not validateEmail:
            messagebox.showerror("Error", "Invalid Email Address")
        # succesfull
        else:
            sqlus = "INSERT INTO User(Username, Password) \
                    VALUES ('%s', '%s')" % (self.inputUser.get(), self.inputPass.get())
            sql = "INSERT INTO Customer(Username, Email, IsStudent) " \
                  "VALUES ('%s', '%s', '0')" % (self.inputUser.get(), self.inputEmail.get())
            cursor.execute(sqlus)
            cursor.execute(sql)
            messagebox.showinfo("Success", "Registration Sucess")
            self.goBackToLogin()

    def registerPageShow(self):
        """
         Show THe Register
        """
        self.window.withdraw()
        self.register.deiconify()
    def goBackToLogin(self):
        """
        go back to login from the register
        :return:
        """
        self.register.withdraw()
        self.mainFrame.withdraw()
        self.window.deiconify()

    def goBackToMainPage(self):
        self.scheduleWin.withdraw()
        self.mainFrame.deiconify()
    def registerPage(self):
        self.register.title("Registration")
        frame = Frame(self.register)
        frame.pack(fill = 'both', expand = 'yes')

        # Labels for entries
        enterUser = Label(frame, text = "Enter Username :")
        enterPass = Label(frame, text ="Enter Passowrd :")
        registerLabel = Label(frame, text = "Registration Page", font = ("Arial", 40))
        enterEmail = Label(frame, text ="Enter Email :")
        confirmPass = Label(frame, text = "Confirm Password :")

        # String varriables to be input
        self.inputUser = StringVar()
        self.inputPass = StringVar()
        self.inputConfirmPass = StringVar()
        self.inputEmail = StringVar()

        # Entry varraibles
        entryUsr = Entry(frame, textvariable = self.inputUser, width = 25)
        entryPas = Entry(frame, textvariable=self.inputPass, width=25)
        entryConfirm = Entry(frame, textvariable=self.inputConfirmPass, width=25)
        entryEmail = Entry(frame, textvariable=self.inputEmail, width=25)

        # Button Variables
        cancelB = Button(frame, text="Cancel", command = self.goBackToLogin)
        registerB = Button(frame, text="Register", command = self.registerUser)
        # placing labels in the window
        registerLabel.place(x = 10, y = 10)
        enterUser.place(x=0, y=100)
        enterPass.place(x=0, y=140)
        enterEmail.place(x=0, y=180)
        confirmPass.place(x=0, y=220)

        # placing entry input in the window
        entryUsr.place(x=130, y=100)
        entryPas.place(x=130, y=140)
        entryEmail.place(x=130, y=180)
        entryConfirm.place(x=130, y=220)

        # place button in the window
        cancelB.place(x=100, y=260)
        registerB.place(x=200, y=260)

    def TrainNumberSearch(self):
        self.mainFrame.withdraw()
        self.trainSchWin = Toplevel()
        self.trainSchWin.title("View Train Schedule")
        frame1 = Frame(self.trainSchWin)
        frame2 = Frame(self.trainSchWin)
        frame1.pack(side=TOP)
        frame2.pack(side=BOTTOM)
        label1 = Label(frame1, text="Train Number")
        label1.pack(side=LEFT)

        self.trainName = StringVar()
        self.entry = Entry(frame1, textvariable=self.trainName, width=10)
        self.entry.pack(side=RIGHT)

        b1 = Button(frame2, text="Search", command=self.schedule)
        b1.pack(side=LEFT)

    def schedule(self):
        self.trainSchWin.withdraw()
        self.scheduleWin = Toplevel()
        self.scheduleWin.title("View Train Schedule")

        frame1 = Frame(self.scheduleWin)
        frame1.pack()
        frame2 = Frame(self.scheduleWin)
        frame2.pack()

        # tree = self.getTrainTree(frame1)
        # chosenTrain = self.trainName.get()
        sql = "SELECT * FROM Stop\
                WHERE TrainNumber='%s'\
                ORDER BY ArrivalTime" % self.trainName.get()
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        # trains = [train[0] for train in cursor.fetchall()]
        # stations = [station[0] for station in cursor.fetchall()]


        results = cursor.fetchall()
        if not results:
            r = messagebox.showerror("Error!", "No Train's Follow Criteria.")
        i = 0
        # for result in results:
        #     tree.insert('', i, text='', values=result)
        #     i += 1
        # print(results)
        self.widgets = {}
        dc = Label(frame1, text="Train Number", font=("Calibri", 12, "bold"))
        dc.grid(row=1, column=0, sticky='W')
        dc2 = Label(frame1, text="Station", font=("Calibri", 12, "bold"))
        dc2.grid(row=1, column=1, padx=30, pady=10, sticky='W')
        dc3 = Label(frame1, text="Arrival Time", font=("Calibri", 12, "bold"))
        dc3.grid(row=1, column=2, padx=30, pady=10, sticky='W')
        dc4 = Label(frame1, text="Departure Time", font=("Calibri", 12, "bold"))
        dc4.grid(row=1, column=4, padx=30, pady=10, sticky='W')

        row = 1
        for TrainNum, Station, Arrivalt, DepartT in (results):
            row += 1
            self.widgets[TrainNum] = {
                "Train Number": Label(frame1, text=TrainNum),
                "Station": Label(frame1, text=Station),
                "Arrival Time": Label(frame1, text=Arrivalt),
                "Depart Time": Label(frame1, text=DepartT),
            }

            self.widgets[TrainNum]["Train Number"].grid(row=row, column=0, sticky="nsew")
            self.widgets[TrainNum]["Station"].grid(row=row, column=1, sticky="nsew")
            self.widgets[TrainNum]["Arrival Time"].grid(row=row, column=2, sticky="nsew")
            self.widgets[TrainNum]["Depart Time"].grid(row=row, column=3, sticky="nsew")

        frame1.grid_columnconfigure(1, weight=1)
        frame1.grid_columnconfigure(2, weight=1)
        # invisible row after last row gets all extra space
        frame1.grid_rowconfigure(row + 1, weight=1)

        b1 = Button(frame2, text="Back", command=self.goBackToMainPage)
        b1.pack(side=BOTTOM)

    """
    # create the root window
    root = Tk()
    # optionally give it a title
    root.title("My Title")
    # set the root window's height, width and x,y position
    # x and y are the coordinates of the upper left corner
    w = 300
    h = 200
    x = 0
    y = 0
    # use width x height + x_offset + y_offset (no spaces!)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    # use a colorful frame
    frame = Frame(root, bg='green')
    frame.pack(fill='both', expand='yes')
    # position a label on the frame using place(x, y)
    # place(x=0, y=0) would be the upper left frame corner
    label = Label(frame, text="Hello Python Programmer!")
    label.place(x=100, y=30)
    # put the button below the label, change y coordinate
    button = Button(frame, text="Press me", bg='yellow')
    button.place(x=20, y=60)
    root.mainloop() """

mw = Tk()
mw.minsize(400,400)
app = Train(mw)
mw.mainloop()
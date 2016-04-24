from tkinter import *
from tkinter.ttk import *
import pymysql
from tkinter import messagebox
from datetime import datetime


class GUI:

    def __init__(self, updateWin):
        #self.primaryWindow.withdraw()
        self.updateWin = updateWin
        self.updateWin.title("Update Reservation")

        frame = Frame(self.updateWin)
        frame.pack()
        self.resIDUpdate = StringVar()

        l1 = Label(frame, text="Reservation ID")
        l1.grid(row=0, column=0, sticky=E)
        e1 = Entry(frame, width=10, textvariable = self.resIDUpdate)
        e1.grid(row=0, column=1)
        b1 = Button(frame, text="Search", command=self.updateReservation2)
        b1.grid(row=0, column=2, sticky=E)
        b2 = Button(frame, text="Back")
        b2.grid(row=1, column=1, sticky=E)

    def updateReservation2(self):
        self.updateWin.withdraw()
        self.updateWin2 = Toplevel()
        self.updateWin2.title("Select Reservation")
        frame1 = Frame(self.updateWin2)
        frame1.pack()
        frame2 = Frame(self.updateWin2)
        frame2.pack(side=BOTTOM)
        sql = "Select * From Reserves where ReservationID = %i" % int(self.resIDUpdate.get())
        db = self.connect();
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()

        self.widgets = {}
        dc = Label(frame1, text="TrainNumber", font=("Calibri", 12, "bold"))
        dc.grid(row=1, column=0, sticky='W')
        dc2 = Label(frame1, text="Class", font=("Calibri", 12, "bold"))
        dc2.grid(row=1, column=1, padx=30, pady=10, sticky='nsew')
        dc3 = Label(frame1, text="Departure Date", font=("Calibri", 12, "bold"))
        dc3.grid(row=1, column=2, padx=30, pady=10, sticky='W')
        dc4 = Label(frame1, text="Passenger Name", font=("Calibri", 12, "bold"))
        dc4.grid(row=1, column=3, padx=30, pady=10, sticky='W')
        Label(frame1, text = "Number of Bags",font=("Calibri",12,"bold")).grid(row=1,column=4,padx = 30,pady=10,sticky='W')
        Label(frame1, text="Departs From", font=("Calibri", 12, "bold")).grid(row=1, column=5, padx=30, pady=10, sticky='W')
        Label(frame1, text="Arrives At", font=("Calibri", 12, "bold")).grid(row=1, column=6, padx=30, pady=10, sticky='W')
        Label(frame1,text="Select",font=("Calibri",12,"bold")).grid(row=1,column=7,padx=30,pady=10)
        print(results)
        row = 1
        self.trainUpdate=StringVar()
        for Resd,TrainNum,Class, DepatD, PassName, NumB, DepaF,ArrA in (results):

            row += 1
            self.widgets[TrainNum] = {
                "Train Number": Label(frame1, text=TrainNum),
                "Station": Label(frame1, text=Class),
                "Arrival Time": Label(frame1, text=DepatD),
                "Depart Time": Label(frame1, text=PassName),
                "Num B": Label(frame1,text=str(NumB)),
                "DepaF": Label(frame1,text = DepaF),
                "ArrA": Label(frame1,text = ArrA)
            }

            self.widgets[TrainNum]["Train Number"].grid(row=row, column=0, sticky="nsew")
            self.widgets[TrainNum]["Station"].grid(row=row, column=1, sticky="nsew")
            self.widgets[TrainNum]["Arrival Time"].grid(row=row, column=2, sticky="nsew")
            self.widgets[TrainNum]["Depart Time"].grid(row=row, column=3, sticky="nsew")
            self.widgets[TrainNum]["Num B"].grid(row=row, column=4, sticky="nsew")
            self.widgets[TrainNum]["DepaF"].grid(row=row, column=5, sticky="nsew")
            self.widgets[TrainNum]["ArrA"].grid(row=row, column=6, sticky="nsew")
            Radiobutton(frame1, variable=self.trainUpdate, value=TrainNum).grid(row=row, column=7)

        frame1.grid_columnconfigure(1, weight=1)
        frame1.grid_columnconfigure(2, weight=1)
        # invisible row after last row gets all extra space
        frame1.grid_rowconfigure(row + 1, weight=1)
        b=Button(frame2,text='Next',command =self.upDateRes3)
        b.pack(side=RIGHT)

    def upDateRes3(self):
        self.updateWin2.withdraw()
        self.updateWin3 = Toplevel()
        self.updateWin3.title('Update Reservation 3')
        frame1 = Frame(self.updateWin3)
        frame1.pack(side=TOP)
        Label(frame1,text="Current Train Ticket", font=("Calibri", 12, "bold")).pack()
        frame2 = Frame(self.updateWin3)
        frame2.pack(side=TOP)
        frame3 = Frame(self.updateWin3)
        frame3.pack(side=TOP)
        self.newDate = StringVar()
        Label(frame3,text="New Departure Date (YYYY-MM-DD)",font=("Calibri",12,"bold")).grid(row=1,column=1,padx=30,pady=10)
        Entry(frame3, width=10, textvariable=self.newDate).grid(row=1,column=2,padx=30,pady=10)
        Button(frame3,text = 'Search Date',command=self.updateTrain).grid(row=1,column=3)
        print(self.trainUpdate.get())

        sql = sql = "Select * From Reserves where ReservationID = %i and TrainNumber='%s'" % (int(self.resIDUpdate.get()),self.trainUpdate.get())
        db = self.connect();
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()

        self.widgets = {}
        dc = Label(frame2, text="TrainNumber", font=("Calibri", 12, "bold"))
        dc.grid(row=1, column=0, sticky='W')
        dc2 = Label(frame2, text="Class", font=("Calibri", 12, "bold"))
        dc2.grid(row=1, column=1, padx=30, pady=10, sticky='nsew')
        dc3 = Label(frame2, text="Departure Date", font=("Calibri", 12, "bold"))
        dc3.grid(row=1, column=2, padx=30, pady=10, sticky='W')
        dc4 = Label(frame2, text="Passenger Name", font=("Calibri", 12, "bold"))
        dc4.grid(row=1, column=3, padx=30, pady=10, sticky='W')
        Label(frame2, text="Number of Bags", font=("Calibri", 12, "bold")).grid(row=1, column=4, padx=30, pady=10,sticky='W')
        Label(frame2, text="Departs From", font=("Calibri", 12, "bold")).grid(row=1, column=5, padx=30, pady=10, sticky='W')
        Label(frame2, text="Arrives At", font=("Calibri", 12, "bold")).grid(row=1, column=6, padx=30, pady=10, sticky='W')
        print(results)
        row = 1
        for Resd, TrainNum, Class, DepatD, PassName, NumB, DepaF, ArrA in (results):
            row += 1
            self.widgets[TrainNum] = {
                "Train Number": Label(frame2, text=TrainNum),
                "Station": Label(frame2, text=Class),
                "Arrival Time": Label(frame2, text=DepatD),
                "Depart Time": Label(frame2, text=PassName),
                "Num B": Label(frame2, text=str(NumB)),
                "DepaF": Label(frame2, text=DepaF),
                "ArrA": Label(frame2, text=ArrA)
            }

            self.widgets[TrainNum]["Train Number"].grid(row=row, column=0, sticky="nsew")
            self.widgets[TrainNum]["Station"].grid(row=row, column=1, sticky="nsew")
            self.widgets[TrainNum]["Arrival Time"].grid(row=row, column=2, sticky="nsew")
            self.widgets[TrainNum]["Depart Time"].grid(row=row, column=3, sticky="nsew")
            self.widgets[TrainNum]["Num B"].grid(row=row, column=4, sticky="nsew")
            self.widgets[TrainNum]["DepaF"].grid(row=row, column=5, sticky="nsew")
            self.widgets[TrainNum]["ArrA"].grid(row=row, column=6, sticky="nsew")

        frame2.grid_columnconfigure(1, weight=1)
        frame2.grid_columnconfigure(2, weight=1)
        # invisible row after last row gets all extra space
        frame2.grid_rowconfigure(row + 1, weight=1)

    def updateTrain(self):
        frame4 = Frame(self.updateWin3)
        frame4.pack(side=TOP)

        sql = sql = "Select * From Reserves where ReservationID = %i and TrainNumber='%s'" % (
        int(self.resIDUpdate.get()), self.trainUpdate.get())
        db = self.connect();
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()

        if datetime.strptime(self.newDate.get(),'%Y-%m-%d' ) <= results[0][3]:
            messagebox.showerror(message="Error! Date Must be 1 Day in Advance of Departure Date")
        else:
            Label(frame4, text="Updated Train Ticket:", font=("Calibri", 12, "bold")).grid(row=0, column=0, padx=30, pady=10,sticky='W')

            self.widgets = {}
            dc = Label(frame4, text="TrainNumber", font=("Calibri", 12, "bold"))
            dc.grid(row=2, column=0, sticky='W')
            dc2 = Label(frame4, text="Class", font=("Calibri", 12, "bold"))
            dc2.grid(row=2, column=1, padx=30, pady=10, sticky='nsew')
            dc3 = Label(frame4, text="Departure Date", font=("Calibri", 12, "bold"))
            dc3.grid(row=2, column=2, padx=30, pady=10, sticky='W')
            dc4 = Label(frame4, text="Passenger Name", font=("Calibri", 12, "bold"))
            dc4.grid(row=2, column=3, padx=30, pady=10, sticky='W')
            Label(frame4, text="Number of Bags", font=("Calibri", 12, "bold")).grid(row=2, column=4, padx=30, pady=10,
                                                                                    sticky='W')
            Label(frame4, text="Departs From", font=("Calibri", 12, "bold")).grid(row=2, column=5, padx=30, pady=10, sticky='W')
            Label(frame4, text="Arrives At", font=("Calibri", 12, "bold")).grid(row=2, column=6, padx=30, pady=10, sticky='W')
            print(results)
            row = 2
            for Resd, TrainNum, Class, DepatD, PassName, NumB, DepaF, ArrA in (results):
                row += 1
                self.widgets[TrainNum] = {
                    "Train Number": Label(frame4, text=TrainNum),
                    "Station": Label(frame4, text=Class),
                    "Arrival Time": Label(frame4, text=self.newDate.get()),
                    "Depart Time": Label(frame4, text=PassName),
                    "Num B": Label(frame4, text=str(NumB)),
                    "DepaF": Label(frame4, text=DepaF),
                    "ArrA": Label(frame4, text=ArrA)
                }

                self.widgets[TrainNum]["Train Number"].grid(row=row, column=0, sticky="nsew")
                self.widgets[TrainNum]["Station"].grid(row=row, column=1, sticky="nsew")
                self.widgets[TrainNum]["Arrival Time"].grid(row=row, column=2, sticky="nsew")
                self.widgets[TrainNum]["Depart Time"].grid(row=row, column=3, sticky="nsew")
                self.widgets[TrainNum]["Num B"].grid(row=row, column=4, sticky="nsew")
                self.widgets[TrainNum]["DepaF"].grid(row=row, column=5, sticky="nsew")
                self.widgets[TrainNum]["ArrA"].grid(row=row, column=6, sticky="nsew")

            frame4.grid_columnconfigure(1, weight=1)
            frame4.grid_columnconfigure(2, weight=1)
            # invisible row after last row gets all extra space
            frame4.grid_rowconfigure(row + 1, weight=1)

            frame5 = Frame(self.updateWin3)
            frame5.pack(side=TOP)
            Label(frame5, text="Change Fee:", font=("Calibri", 12, "bold")).grid(row=0, column=0, padx=30,pady=10)
            Label(frame5, text="Updated Total Cost:",font=("Calibri",12,"bold")).grid(row=1,column=0,padx=30,pady=10)
            Label(frame5,text=str(50)).grid(row=0,column=1,pady=10)
            #Label(frame5,text=("'%s'" % str(results[0][priceIndex] + 50))).grid(row=1,column=0,pady=10)
            Button(frame5,text="Back").grid(row=3,column=0,padx=30)
            Button(frame5,text = "Sumbit",command=self.submitUpdate).grid(row=3,column=1)

    def submitUpdate(self):
        messagebox.showerror(message="Your Ticket Has Been Updated")
        sql = "UPDATE Reserves SET DepartureDate='%s' WHERE ReservationID=%i and TrainNumber='%s'" % (self.newDate.get(),int(self.resIDUpdate.get()),self.trainUpdate.get())
        db = self.connect()
        cursor=db.cursor()
        #cursor.execute(sql)

    def connect(self):
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu",
                             user="cs4400_Team_39",
                             passwd="HSaWNuO5",
                             db="cs4400_Team_39")
        return (db)

win = Tk()
app = GUI(win)
win.mainloop()
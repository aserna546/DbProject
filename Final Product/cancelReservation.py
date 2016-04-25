from tkinter import *
from tkinter.ttk import *
import pymysql
from tkinter import messagebox
from datetime import datetime,timedelta


class GUI:

    def __init__(self, cancelWin, mainFrame):
        #self.primaryWindow.withdraw()
        self.cancelWin = cancelWin
        self.cancelWin.title("Cancel Reservation")
        self.mainFrame = mainFrame
        frame = Frame(self.cancelWin)
        frame.pack()
        self.resIDCancel = StringVar()

        l1 = Label(frame, text="Reservation ID")
        l1.grid(row=0, column=0, sticky=E)
        e1 = Entry(frame, width=10, textvariable = self.resIDCancel)
        e1.grid(row=0, column=1)
        b1 = Button(frame, text="Search", command=self.cancelRes2)
        b1.grid(row=0, column=2, sticky=E)
        b2 = Button(frame, text="Back", command=self.goBackToMain)
        b2.grid(row=1, column=1, sticky=E)

    def goBackToMain(self):
        self.cancelWin.destroy()
        self.mainFrame.deiconify()
    def cancelRes2(self):
        self.cancelWin.withdraw()
        self.cancelWin2 = Toplevel()
        self.cancelWin2.title("Cancel Reservation 2")
        frame1 = Frame(self.cancelWin2)
        frame1.pack()
        frame3 = Frame(self.cancelWin2)
        frame3.pack(side=TOP)
        frame2 = Frame(self.cancelWin2)
        frame2.pack(side=BOTTOM)
        sql = "Select IsCancelled From Reservation where ReservationID = %i" % int(self.resIDCancel.get())
        db = self.connect();
        cursor = db.cursor()
        cursor.execute(sql)
        can = cursor.fetchall()
        print(can)
        if can[0][0]:
            messagebox.showerror("Error", "You Cannot Cancel a Cancelled Reservation")
            self.cancelWin2.destroy()
            self.cancelWin.deiconify()
        else:
            sql = "Select * From ReservationView where ReservationID = %i" % int(self.resIDCancel.get())
            cursor.execute(sql)
            results = cursor.fetchall()
            self.widgets = {}
            dc = Label(frame1, text="TrainNumber", font=("Calibri", 12, "bold"))
            dc.grid(row=1, column=0, sticky='W')
            Label(frame1, text="Time", font=("Calibri", 12, "bold")).grid(row=1, column=1)
            dc2 = Label(frame1, text="Departs From", font=("Calibri", 12, "bold"))
            dc2.grid(row=1, column=2, padx=30, pady=10, sticky='nsew')
            dc3 = Label(frame1, text="Arives At", font=("Calibri", 12, "bold"))
            dc3.grid(row=1, column=3, padx=30, pady=10, sticky='W')
            dc4 = Label(frame1, text="Price", font=("Calibri", 12, "bold"))
            dc4.grid(row=1, column=4, padx=30, pady=10, sticky='W')
            Label(frame1, text="Class", font=("Calibri", 12, "bold")).grid(row=1, column=5, padx=30, pady=10,
                                                                           sticky='W')
            Label(frame1, text="Number of Bags", font=("Calibri", 12, "bold")).grid(row=1, column=6, padx=30, pady=10,
                                                                                    sticky='W')
            Label(frame1, text="Passenger Name", font=("Calibri", 12, "bold")).grid(row=1, column=7, padx=30, pady=10,
                                                                                    sticky='W')

            row = 1
            for Resd, TrainNum, ti, DepF, ArA, clv, p, nuB, PNa in (results):
                row += 1
                self.widgets[TrainNum] = {
                    "Train Number": Label(frame1, text=TrainNum),
                    "Time": Label(frame1, text=ti),
                    "Station": Label(frame1, text=DepF),
                    "Arrival Time": Label(frame1, text=ArA),
                    "Depart Time": Label(frame1, text=clv),
                    "Num B": Label(frame1, text=p),
                    "DepaF": Label(frame1, text=nuB),
                    "ArrA": Label(frame1, text=PNa)
                }

                self.widgets[TrainNum]["Train Number"].grid(row=row, column=0, sticky="nsew")
                self.widgets[TrainNum]["Time"].grid(row=row, column=1, sticky="nsew")
                self.widgets[TrainNum]["Station"].grid(row=row, column=2, sticky="nsew")
                self.widgets[TrainNum]["Arrival Time"].grid(row=row, column=3, sticky="nsew")
                self.widgets[TrainNum]["Depart Time"].grid(row=row, column=4, sticky="nsew")
                self.widgets[TrainNum]["Num B"].grid(row=row, column=5, sticky="nsew")
                self.widgets[TrainNum]["DepaF"].grid(row=row, column=6, sticky="nsew")
                self.widgets[TrainNum]["ArrA"].grid(row=row, column=7, sticky="nsew")

            frame1.grid_columnconfigure(1, weight=1)
            frame1.grid_columnconfigure(2, weight=1)
            # invisible row after last row gets all extra space
            frame1.grid_rowconfigure(row + 1, weight=1)
            sql3 = "Select TicketPrice from Reserves where ReservationID=%i" % int(self.resIDCancel.get())
            cursor.execute(sql3)
            resultsP = cursor.fetchall()
            self.totalCost = 0
            for pr in (resultsP):
                self.totalCost = self.totalCost + pr[0]
            Label(frame3,text = "Total Cost of Reservation: %i" % self.totalCost).grid(row=0,column=0,pady=10)
            Label(frame3, text="Date of Cancellation:").grid(row=1, column=0, pady=10,padx=10)
            self.cancelDate = StringVar()
            Entry(frame3,width=10,textvariable=self.cancelDate).grid(row=1,column=1,pady=10)

            b=Button(frame2,text='Check Amount to be Refunded',command =self.cancelReservation)
            b.pack(side=RIGHT)
            Button(frame2,text="Back", command=self.goBackToEnterID).pack(side=LEFT)

    def goBackToEnterID(self):
        self.cancelWin2.destroy()
        self.cancelWin.deiconify()

    def cancelReservation(self):
        frame1 = Frame(self.cancelWin2)
        frame1.pack(side=TOP)
        Label(frame1,text="Amount to be Refunded:", font=("Calibri", 12, "bold")).grid(row=0,column=0,padx=10,pady=10)
        sql2 = "SELECT min(DepartureDate) from Reserves where ReservationID=%i" % int(self.resIDCancel.get())
        db = self.connect()
        cursor=db.cursor()
        cursor.execute(sql2)
        resultsDate = cursor.fetchall()

        #print(totalCost)
        if datetime.strptime(self.cancelDate.get(), '%Y-%m-%d') >= resultsDate[0][0]:
            messagebox.showerror(message="Cannot Change Ticket so Soon!")
        elif datetime.strptime(self.cancelDate.get(), '%Y-%m-%d') + timedelta(days=7) <= resultsDate[0][0]:
            amountRefund = round(self.totalCost * 0.8 -50,2)
            if amountRefund <0:
                amountRefund = 0
            Label(frame1,text = "%i"%amountRefund).grid(row=0,column=1,pady=10)
            messagebox.showerror(message="Refunded 0.8")
        else:
            messagebox.showerror(message="Refunded 0.5")
            amountRefund = round(self.totalCost * 0.5 - 50,2)
            if amountRefund <0:
                amountRefund = 0
            Label(frame1,text = "%i"%amountRefund).grid(row=0,column=1,pady=10)
        frame2 = Frame(self.cancelWin2)
        frame2.pack(side=BOTTOM)
        Button(frame2,text = "Confirm",command=self.submit).pack(side=BOTTOM)

    def submit(self):
        sql = "UPDATE Reservation set isCancelled = 1\
                WHERE ReservationID = '%i';" % int(self.resIDCancel.get())
        db = self.connect()
        cursor=db.cursor()
        cursor.execute(sql)
        self.cancelWin.destroy()
        self.cancelWin2.destroy()
        self.mainFrame.deiconify()
    def connect(self):
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu",
                             user="cs4400_Team_39",
                             passwd="HSaWNuO5",
                             db="cs4400_Team_39")
        return (db)


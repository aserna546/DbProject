from tkinter import *
from tkinter.ttk import *
import pymysql
from tkinter import messagebox
from datetime import datetime,timedelta


class GUI:

    def __init__(self, cancelWin):
        #self.primaryWindow.withdraw()
        self.cancelWin = cancelWin
        self.cancelWin.title("Cancel Reservation")

        self.cancelWin2 = Toplevel()
        self.cancelWin2.withdraw()

        frame = Frame(self.cancelWin)
        frame.pack()
        self.resIDCancel = StringVar()

        l1 = Label(frame, text="Reservation ID")
        l1.grid(row=0, column=0, sticky=E)
        e1 = Entry(frame, width=10, textvariable = self.resIDCancel)
        e1.grid(row=0, column=1)
        b1 = Button(frame, text="Search", command=self.cancelRes2)
        b1.grid(row=0, column=2, sticky=E)
        b2 = Button(frame, text="Back")
        b2.grid(row=1, column=1, sticky=E)

    def cancelRes2(self):
        self.cancelWin.withdraw()
        self.cancelWin2.deiconify()
        self.cancelWin2.title("Cancel Reservation 2")
        frame1 = Frame(self.cancelWin2)
        frame1.pack()
        frame3 = Frame(self.cancelWin2)
        frame3.pack(side=TOP)
        frame2 = Frame(self.cancelWin2)
        frame2.pack(side=BOTTOM)
        sql = "Select * From Reserves where ReservationID = %i" % int(self.resIDCancel.get())
        db = self.connect();
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        if not results:
            messagebox.showerror(message="You Cannot Cancel a Cancelled Reservation")
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

        frame1.grid_columnconfigure(1, weight=1)
        frame1.grid_columnconfigure(2, weight=1)
        # invisible row after last row gets all extra space
        frame1.grid_rowconfigure(row + 1, weight=1)
        #totalCost = results[0][5]
        #Label(frame3,Text = "Total Cost of Reservation: %i" % totalCost).grid(row=0,column=0,pady=10)
        Label(frame3, text="Date of Cancellation:").grid(row=1, column=0, pady=10,padx=10)
        self.cancelDate = StringVar()
        Entry(frame3,width=10,textvariable=self.cancelDate).grid(row=1,column=1,pady=10)

        b=Button(frame2,text='Submit',command =self.cancelReservation)
        b.pack(side=RIGHT)
        Button(frame2,text="Back").pack(side=LEFT)

    def cancelReservation(self):
        frame1 = Frame(self.cancelWin2)
        frame1.pack(side=TOP)
        Label(frame1,text="Amount to be Refunded:", font=("Calibri", 12, "bold")).grid(row=0,column=0,padx=10,pady=10)
        sql2 = "SELECT min(DepartureDate) from Reserves where ReservationID=%i" % int(self.resIDCancel.get())
        db = self.connect()
        cursor=db.cursor()
        cursor.execute(sql2)
        resultsDate = cursor.fetchall()
        #totalCost=resultsDate[0][1]
        if datetime.strptime(self.cancelDate.get(), '%Y-%m-%d') >= resultsDate[0][0]:
            messagebox.showerror(message="Cannot Change Ticket so Soon!")
        elif datetime.strptime(self.cancelDate.get(), '%Y-%m-%d') + timedelta(days=7) <= resultsDate[0][0]:
            #amountRefund = round(totalCost * 0.8 -50,2)
            #if amountRefund <0:
             #   amountRefund = 0
            #Label(frame1,text = "%i"%amountRefund).grid(row=0,column=1,pady=10)
            messagebox.showerror(message="Refunded 0.8")
        else:
            messagebox.showerror(message="Refunded 0.5")
            #amountRefund = round(totalCost * 0.5 - 50,2)
            #if amountRefund <0:
            #    amountRefund = 0
            # Label(frame1,text = "%i"%amountRefund).grid(row=0,column=1,pady=10)
        sql = "UPDATE Reservation set isCancelled = 1\
                WHERE ReservationID = '%i';" % int(self.resIDCancel.get())
        cursor.execute(sql)

    def connect(self):
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu",
                             user="cs4400_Team_39",
                             passwd="HSaWNuO5",
                             db="cs4400_Team_39")
        return (db)

win = Tk()
app = GUI(win)
win.mainloop()
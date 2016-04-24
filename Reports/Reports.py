from tkinter import *
from tkinter.ttk import *
import pymysql
import urllib.request
import base64
from tkinter import messagebox
import datetime

class GUI:
    def __init__(self, rootChoose):
        self.rootChoose = Toplevel()
        self.rootChoose.title("Choose Report")
        #self.rootWinCF.withdraw()
        self.rootChoose.minsize(400,300)
        pic = Label(self.rootChoose, text="Choose Functionality",font=("Calibri", 18, "bold"))
        pic.place(x = 85, y = 50)
        frame = Frame(self.rootChoose);
        frame.pack();
        frame.place(x = 85, y = 100)
        frame2 = Frame(self.rootChoose);
        frame2.pack();
        frame2.place(x = 85, y = 130)
        viewRevReport = Button(frame, text="View Revenue Report", width=20, command = self.goRevenueReport)
        viewRevReport.pack()

        viewPopularRouteReport = Button(frame2, text="View Popular Report", width=20, command = self.goPopularReport)
        viewPopularRouteReport.pack()

    def goRevenueReport(self):
        self.newWindow = Toplevel(self.rootChoose)
        self.app = RevenueReport(self.newWindow)

    def goPopularReport(self):
        self.newWindow = Toplevel(self.rootChoose)
        self.app = PopularReport(self.newWindow)

    def connect(self):
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu",
                             user="cs4400_Team_39",
                             passwd="HSaWNuO5",
                             db="cs4400_Team_39")
        return (db)

class RevenueReport:
    def __init__(self, master):
        self.master = master
        self.master.minsize(300,200)

        labelframe = Frame(self.master)
        labelframe.pack()
        labelframe.place(x=50, y=20)
        label = Label(labelframe, text="View Revenue Report", font=("Calibri", 18, "bold"))
        label.pack()

        treeframe = Frame(self.master)
        treeframe.pack()
        treeframe.place(x=50,y=60)
        tree = Treeview(treeframe, selectmode='browse', height=3)

        tree["columns"] = ("Month", "Revenue")
        tree.column("#0", width=0, minwidth=0)
        tree.column("Month", width=100)
        tree.column("Revenue", width=100)
        tree.heading("Month", text="Month")
        tree.heading("Revenue", text="Revenue")
        tree.pack()

        sql = "(SELECT Month(DepartureDate) as Month,Sum(TicketPrice) as Revenue FROM Reserves WHERE Month(CurDate())=Month(DepartureDate)+1 AND DateDiff(CurDate(),DepartureDate)<62 Limit 3) UNION (SELECT Month(DepartureDate) as Month,Sum(TicketPrice) as Revenue FROM Reserves WHERE Month(CurDate())=Month(DepartureDate)+2 AND DateDiff(CurDate(),DepartureDate)<93 Limit 3) UNION (SELECT Month(DepartureDate) as Month,Sum(TicketPrice) As Revenue FROM Reserves WHERE Month(CurDate())=Month(DepartureDate)+3 AND DateDiff(CurDate(),DepartureDate)<124 Limit 3)"
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        if not results:
            r = messagebox.showerror("Error!", "Found No revenues to report!")
        row = 0
        d = {}
        for month, revenue in (results):
            today = datetime.date.today()
            if month == 2:
                today = today + datetime.timedelta(1*365/12)
            elif month == 3:
                today = today + datetime.timedelta(2*365/12)
            input = ""
            if today.month == 4:
                input = "APRIL"
            elif today.month == 5:
                input = "MAY"
            elif today.month == 6:
                input = "JUNE"
            elif today.month == 7:
                input = "JULY"
            d[row] = [input,revenue]
            row += 1
        for k in d:
            tree.insert("", k, text="", values=(d[k][0],"$"+str(d[k][1])))

        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text='Quit', width=5, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
        self.frame.place(x=110,y=150)

    def close_windows(self):
        self.master.destroy()

    def connect(self):
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu",
                             user="cs4400_Team_39",
                             passwd="HSaWNuO5",
                             db="cs4400_Team_39")
        return (db)

class PopularReport:
    def __init__(self, master):
        self.master = master
        self.master.minsize(400,300)

        labelframe = Frame(self.master)
        labelframe.place(x=100, y=30)
        labelframe.pack()
        label = Label(labelframe, text="View Most Popular Routes",font=("Calibri", 18, "bold"))
        label.pack()

        treeframe = Frame(self.master)
        treeframe.pack()
        tree = Treeview(treeframe, selectmode='browse',height=9)
        tree["columns"] = ("Month", "Train Number", "# Of Reservations")
        tree.column("#0", width=0, minwidth=0)
        tree.column("Month", width=80, anchor="center")
        tree.column("Train Number", width=100, anchor="center")
        tree.column("# Of Reservations", width=100, anchor="center")
        tree.heading("Month", text="Month")
        tree.heading("Train Number", text="Train Number")
        tree.heading("# Of Reservations", text="# Of Reservations")
        tree.pack()

        sql = "(SELECT TrainNumber,Count(TrainNumber),Month(DepartureDate) FROM Reserves WHERE Month(CurDate())=Month(DepartureDate)+1 AND DateDiff(CurDate(),DepartureDate)<62 GROUP By TrainNumber ORDER By Count(TrainNumber) Limit 3) UNION (SELECT TrainNumber,Count(TrainNumber),Month(DepartureDate) FROM Reserves WHERE Month(CurDate())=Month(DepartureDate)+2 AND DateDiff(CurDate(),DepartureDate)<93 GROUP By TrainNumber ORDER By Count(TrainNumber) Limit 3 ) UNION (SELECT TrainNumber,Count(TrainNumber),Month(DepartureDate) FROM Reserves WHERE Month(CurDate())=Month(DepartureDate)+3 AND DateDiff(CurDate(),DepartureDate)<124 GROUP By TrainNumber ORDER By Count(TrainNumber) Limit 3 );"
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        if not results:
            r = messagebox.showerror("Error!", "Found No revenues to report!")
        row = 0
        d = {}
        for TrainNumber, countTrainNumber, monthDepartureDate in (results):
            month = datetime.date.today()
            if monthDepartureDate == 2:
                month = month + datetime.timedelta(1*365/12)
            elif monthDepartureDate == 3:
                month = month + datetime.timedelta(2*365 / 12)
            input = ""
            if month.month == 4:
                input = "APRIL"
            elif month.month == 5:
                input = "MAY"
            elif month.month == 6:
                input = "JUNE"
            elif month.month == 7:
                input = "JULY"
            d[row] = [input, TrainNumber, countTrainNumber]
            row += 1
        for k in d:
            if k % 3 == 0:
                tree.insert("", k, text="", values=(d[k][0], d[k][1], d[k][2]))
            else:
                tree.insert("", k, text="", values=("", d[k][1], d[k][2]))

        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text='Back', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def connect(self):
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu",
                             user="cs4400_Team_39",
                             passwd="HSaWNuO5",
                             db="cs4400_Team_39")
        return (db)

    def close_windows(self):
        self.master.destroy()

win = Tk()
app = GUI(win)
win.mainloop()
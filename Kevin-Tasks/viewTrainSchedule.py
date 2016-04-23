from tkinter import *
from tkinter.ttk import *
import pymysql
from tkinter import messagebox

class GUI:
    def __init__(self, primaryWin):
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

        #tree = self.getTrainTree(frame1)
        #chosenTrain = self.trainName.get()
        sql = "SELECT * FROM Stop\
                WHERE TrainNumber='%s'\
                ORDER BY ArrivalTime" % self.trainName.get()
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        #trains = [train[0] for train in cursor.fetchall()]
        #stations = [station[0] for station in cursor.fetchall()]


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

        b1 = Button(frame2, text="Back")#, command=self.switchtotrainSchedule)
        b1.pack(side=BOTTOM)

    def connect(self):
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu",
                             user="cs4400_Team_39",
                             passwd="HSaWNuO5",
                             db="cs4400_Team_39")
        return (db)


    def getTrainTree(self, frame):
        tree = Treeview(frame)
        tree.pack()

        tree["columns"] = ("train", "station","arrv", "dept")
        tree.heading("train", text="Train (Train Number)")
        tree.heading("station", text="Station")
        tree.heading("arrv", text="Arrival Time")
        tree.heading("dept", text="Departure Time")
        return tree

win = Tk()
app = GUI(win)
win.mainloop()
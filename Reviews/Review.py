from tkinter import *
from tkinter.ttk import *
import pymysql
from tkinter import messagebox

class GUI:
    def __init__(self, rootChoose):
        self.rootChoose = Toplevel()
        self.rootChoose.title("Choose Report")
        self.rootChoose.minsize(400,300)
        pic = Label(self.rootChoose, font=("Helvetica",18), text="Choose Functionality")
        pic.place(x = 108, y = 50)

        frame = Frame(self.rootChoose);
        frame.pack();
        frame.place(x = 85, y = 100)
        frame2 = Frame(self.rootChoose);
        frame2.pack();
        frame2.place(x = 85, y = 130)
        viewReview = Button(frame, text="View a Review", width=20, command = self.goViewReview)
        viewReview.pack()

        WriteReview = Button(frame2, text="Write a Review", width=20, command = self.goWriteReview)
        WriteReview.pack()

    def goWriteReview(self):
        self.newWindow = Toplevel(self.rootChoose)
        self.app = WriteReview(self.newWindow)

    def goViewReview(self):
        self.newWindow = Toplevel(self.rootChoose)
        self.app = ViewReview(self.newWindow)

    def connect(self):
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu",
                             user="cs4400_Team_39",
                             passwd="HSaWNuO5",
                             db="cs4400_Team_39")
        return (db)

class ViewReview:
    def __init__(self, master):
        self.master = master
        self.master.minsize(400,300)
        pic = Label(self.master, font=("Helvetica",18), text="View Review")
        pic.place(x = 145, y = 30)
        frame2 = Frame(master)
        label = Label(frame2, text="Train Number")
        label.pack()
        self.routenum = StringVar()
        self.routenumEntry = Entry(frame2, textvariable=self.routenum, width=20)
        self.routenumEntry.pack()
        frame2.pack()
        frame2.place(x = 100, y = 70)

        frame3 = Frame(master)
        submit = Button(frame3, text="Find Review", command=self.loadReviews)
        submit.pack()
        frame3.pack()
        frame3.place(x=135, y=140)

        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text='Back', command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
        self.frame.place(x=145, y = 170)

    def loadReviews(self):
        self.newWindow = Toplevel(self.master)
        self.app = ShowReview(self.newWindow, self.routenumEntry.get())
    def close_windows(self):
        self.master.destroy()

class ShowReview:
    def __init__(self, master, input):
        self.master = master
        self.master.minsize(400,300)
        labelframe = Frame(master)
        labelframe.place(x = 110, y = 30)
        labelframe.pack()
        label = Label(labelframe, font=("Helvetica",18), text="View Review")
        label.pack()

        treeframe = Frame(master)
        treeframe.pack()
        tree = Treeview(treeframe, selectmode='browse', height=5)

        tree["columns"] = ("Rating", "Comment")
        tree.column("#0", width=0,minwidth=0)
        tree.column("Rating", width=100)
        tree.column("Comment", width=200)
        tree.heading("Rating", text="Rating")
        tree.heading("Comment", text="Comment")

        reviewNum = input
        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text='Back', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

        # sql = "SELECT * FROM Review;"
        sql = "SELECT * FROM Review WHERE TrainNumber='" + reviewNum + "'"

        db = self.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        verygood = ""
        good = ""
        neutral = ""
        bad = ""
        verybad = ""
        if not results:
            r = messagebox.showerror("Error!", "Found No Reviews found")

        for ReviewNum, Comment, Rating, TrainNumber, Username in (results):
            if Rating == "Very Good":
                verygood += Comment + ", "
            if Rating == "Good":
                good +=  Comment + ", "
            if Rating == "Neutral":
                neutral += Comment + ", "
            if Rating == "Bad":
                bad += Comment + ", "
            if Rating == "Very Bad":
                verybad += Comment + ", "

        tree.insert("", 0, text="", values=("VERY GOOD", verygood ))
        tree.insert("", 1, text="", values=("GOOD", good))
        tree.insert("", 2, text="", values=("NEUTRAL", neutral))
        tree.insert("", 3, text="", values=("BAD", bad))
        tree.insert("", 4, text="", values=("VERY BAD", verybad))
        tree.pack()
    def close_windows(self):
        self.master.destroy()

    def connect(self):
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu",
                             user="cs4400_Team_39",
                             passwd="HSaWNuO5",
                             db="cs4400_Team_39")
        return (db)

class WriteReview:
    def __init__(self, master):
        self.master = master
        self.master.minsize(400,300)
        self.frame = Frame(self.master)
        pic = Label(self.master, font=("Helvetica",18), text="Write Review")
        pic.place(x = 140, y = 10)

        trainframe = Frame(self.master);
        trainlabel = Label(trainframe, text="TrainNumber")
        trainlabel.pack()
        self.train = StringVar()
        trainEntry = Entry(trainframe, textvariable=self.train, width=20)
        trainEntry.pack();
        trainframe.pack();
        trainframe.place(x = 100, y = 50)

        commentframe = Frame(self.master);
        commentlabel = Label(trainframe, text="Comment")
        commentlabel.pack()
        self.comment = StringVar()
        commentEntry = Entry(trainframe, textvariable=self.comment, width=20)
        commentEntry.pack();
        commentframe.pack();
        commentframe.place(x= 100, y = 80)

        ratingframe = Frame(self.master);
        ratinglabel = Label(trainframe, text="Rating")
        ratinglabel.pack()
        self.rating = StringVar()
        ratingEntry = OptionMenu(ratingframe, self.rating, "Very Good","Good","Neutral","Very Bad","Bad")
        ratingEntry.pack();
        ratingframe.pack();
        ratingframe.place(x = 140, y = 165)

        self.submit = Button(self.frame, text='Submit', width=25, command=self.submit)
        self.submit.pack()

        self.quitButton = Button(self.frame, text='Back', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
        self.frame.place(x= 60, y = 200)

    def close_windows(self):
        self.master.destroy()

    def submit(self):

        sql = "SELECT COUNT(ReviewNum) FROM Review"
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        primaryKey = results[0][0] + 2

        sql = "SELECT * FROM TrainRoute WHERE TrainNumber = '" + self.train.get() + "'"

        db = self.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        if not results:
            r = messagebox.showerror("Error!", "Found No Train by that Route Number")
        else:
            sql = "INSERT INTO Review VALUES ('" + str(primaryKey) + "','" + self.comment.get() + "' ,'" + self.rating.get() +  "','" + self.train.get() + "', '" + "Mark_Ericson" + "');"
            db = self.connect()
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
        self.master.destroy()

    def connect(self):
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu",
                             user="cs4400_Team_39",
                             passwd="HSaWNuO5",
                             db="cs4400_Team_39")
        return (db)

win = Tk()
app = GUI(win)
win.mainloop()
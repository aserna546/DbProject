from tkinter import *
from tkinter import messagebox
import pymysql

class GUI:
    def __init__(self, window, username):
        self.username = username
        self.rootwindow = window
        self.rootwindow.title("Add Student Email")
        self.rootwindow.minsize(400, 200)

        labelframe = Frame(self.rootwindow)
        labelframe.pack()
        labelframe.place(x=100, y=30)
        label = Label(labelframe, text="Add School Info", font=("Calibri", 18, "bold"))
        label.pack()

        labelframe2 = Frame(self.rootwindow)
        labelframe2.pack()
        labelframe2.place(x=30, y=82)
        label2 = Label(labelframe2, text="School email")
        label2.pack()

        emailframe = Frame(self.rootwindow)
        self.email = StringVar()
        self.emailEntry = Entry(emailframe, textvariable=self.email, width=20)
        self.emailEntry.pack()
        emailframe.pack()
        emailframe.place(x= 120, y = 80)

        frame = Frame(self.rootwindow)
        submit = Button(frame, text='Submit', width=8, command=self.submit)
        submit.pack()
        frame.pack()
        frame.place(x = 80, y = 120)

        backframe = Frame(self.rootwindow)
        quitButton = Button(backframe, text='Back', width=8, command=self.close_window)
        quitButton.pack()
        backframe.pack()
        backframe.place(x=180, y=120)

    def close_window(self):
        print("CLOSE")

    def submit(self):
        email = self.emailEntry.get()
        validateEmail = re.match(r'\w[\w\.-]*@\w[\w\.-]+\.edu',email)
        print(validateEmail)
        print("we in")
        if (validateEmail != None):
            if email[len(email)-3:len(email)] == "edu":
                print(email)
                sql = "UPDATE Customer SET IsStudent = '1' WHERE Username = '" + self.username + "'"
                db = self.connect()
                cursor = db.cursor()
                cursor.execute(sql)
                r = messagebox.showerror("Success!", "You are now registered as student in our system")
            else:
                r = messagebox.showerror("Error!", "Your Email does not have the .edu domain")
        else:
            r = messagebox.showerror("Error!", "Your Email does not have a .edu ending")

    def connect(self):
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu",
                             user="cs4400_Team_39",
                             passwd="HSaWNuO5",
                             db="cs4400_Team_39")
        return (db)

win = Tk()
app = GUI(win,"alejandro2")
win.mainloop()
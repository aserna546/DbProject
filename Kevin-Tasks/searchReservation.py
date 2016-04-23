from tkinter import *
from tkinter.ttk import *
import pymysql
from tkinter import messagebox



def updateReservation(self):
    self.primaryWindow.withdraw()
    self.updateWin.deiconify()
    self.updateWin.title("Update Reservation")

    frame = Frame(self.updateWin)
    frame.pack()

    l1 = Label(frame, text="Reservation ID")
    l1.grid(row=0, column=0, sticky=E)
    e1 = Entry(frame, width=10)
    e1.grid(row=0, column=1)
    b1 = Button(frame, text="Search", command=self.updateReservation2)
    b1.grid(row=0, column=2, sticky=E)
    b2 = Button(frame, text="Back")
    b2.grid(row=1, column=1, sticky=E)
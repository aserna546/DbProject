from tkinter import *
import pymysql
import urllib.request
import base64
from tkinter import messagebox
import datetime

class GUI:
    def __init__(self, rootWin):
        # creates window
        self.rootWin = rootWin
        self.rootWin.title('Payment Information')

        # Payment Title
        n = Label(self.rootWin, text='Name on Card')
        n.grid(row=4, column=0, padx=5,sticky=W)

        # Card Number Title
        cn = Label(self.rootWin, text="Card Number")
        cn.grid(row=5, column=0, padx=5, sticky=W)

        # CVV Title
        cvv = Label(self.rootWin, text="CVV")
        cvv.grid(row=6, column=0, padx=5, sticky=W)

        # Expiration Date
        ed = Label(self.rootWin, text="Expiration Date")
        ed.grid(row=7, column=0, padx=5, sticky=W)

        # Makes Card name variable
        self.ncE = StringVar()
        self.uEntry = Entry(self.rootWin, textvariable=self.ncE, width=30)
        self.uEntry.grid(row=4, column=1, padx=5)

        # Makes card Number variable
        self.cnE = StringVar()
        self.uEntry = Entry(self.rootWin, textvariable=self.cnE, width=30)
        self.uEntry.grid(row=5, column=1, padx=5)

        # Makes card Number variable
        self.cvvE = StringVar()
        self.uEntry = Entry(self.rootWin, textvariable=self.cvvE, width=10)
        self.uEntry.grid(row=6, column=1, padx=5, sticky=W)

        # Makes card Number variable
        self.dateE = StringVar()
        self.uEntry = Entry(self.rootWin, textvariable=self.dateE, width=20)
        self.uEntry.grid(row=7, column=1, padx=5, sticky=W)

        # Payment Info
        pi = Label(self.rootWin, text="Payment Infomation", font=("Calibri", 15, "bold"), fg="gold", compound = CENTER)
        pi.grid(row=0, column=0, columnspan=4)

        #Add Card Label
        ac = Label(self.rootWin, text ="Add Card", font=("Calibri",12,"bold"), fg = "black")
        ac.grid(row=3,column=0, padx = 5, pady = 10, sticky = W)

        submit1 = Button(self.rootWin, text="Submit", command=self.addCard)
        submit1.grid(row=8, column=0, columnspan=2)

        # Delete Card
        dc = Label(self.rootWin, text="Delete Card", font=("Calibri", 12, "bold"))
        dc.grid(row=3, column=2, padx=30, pady=10, sticky=W)

        cn2 = Label(self.rootWin, text="Card Number")
        cn2.grid(row=4, column=2, padx=30, sticky=W)

        cards = [2541]  # get cards from database
        self.delCard = StringVar()
        pulldownDC = OptionMenu(self.rootWin, self.delCard, *cards)
        pulldownDC.grid(row=4, column=3, padx=15, pady=5, sticky=W)

        submit2 = Button(self.rootWin, text="Submit")#, command=self.deleteCard)
        submit2.grid(row=8, column=2, columnspan=2, pady=20)

    def addCard(self):
        # expDate = datetime.date.today()
        # server = self.connect()
        # cursor = server.cursor()
        # query = "SELECT * FROM PAYMENT_INFORMATION \
        #        WHERE Card_Number = '%s'" % (self.cnE.get())
        # cursor.execute(query)
        # results = cursor.fetchall()
        # if len(results) != 0:
        #     messagebox.showerror("Error", "Card number already in use")
        # elif self.expDate.get() == "" or self.cnE.get() == "" or self.cnE.get() == "" or self.cvvE.get() == "":
        #     messagebox.showerror("Error", "Expiration Date, Name, Number, and CVV must be filled")
        # #elif len(self.cardNumber.get()) != 10:
        #     #messagebox.showerror("Error", "Card Number must be 10 digits")
        # elif len(self.cvvE.get()) != 3:
        #     messagebox.showerror("Error", "CVV must be 3 digits")
        # elif cnE < datetime.now():
        #     messagebox.showerror("Error", "Card has already expired")
        # else:
        db = self.connect()
        cursor = db.cursor()
        query = "INSERT INTO PaymentInfo ( CardNumber, CVV, ExpDate, CardName, Username)\
                  VALUES( '%s', '%s',  '%s', '%s', 'kberman')" % (self.cnE.get(), self.cvvE.get(), self.dateE.get(),self.ncE.get())
        cursor.execute(query)

    #def deleteCard(self):
       # delete card info from database

    def connect(self):
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu",
                             user="cs4400_Team_39",
                             passwd="HSaWNuO5",
                             db="cs4400_Team_39")
        return(db)



win = Tk()
app = GUI(win)
win.mainloop()

from tkinter import *
import urllib.request
import base64
from tkinter import messagebox
import datetime

class GUI:

    def __init__(self,rootWin):
        #creates window
        self.rootWin = rootWin
        self.rootWin.title('Login')
        #self.rootWin.config(bg="grey")

        #Username label
        u = Label(self.rootWin,text='Username:')
        u.grid(row=2,column=0,sticky=E)

        #makes variable of username input
        self.usv = StringVar()
        self.uEntry = Entry(self.rootWin,textvariable=self.usv,width=30)
        self.uEntry.grid(row=2,column=1,padx=5)

        #Password label
        p = Label(self.rootWin,text="Password:")
        p.grid(row=3,column=0,sticky=E)

        #makes variable of password input
        self.psv = StringVar()
        self.pEntry = Entry(self.rootWin,textvariable=self.psv,width=30)
        self.pEntry.grid(row=3,column=1,padx=5)

        #add GT logo
        self.response = urllib.request.urlopen("http://www.cc.gatech.edu/classes/AY2015/cs2316_fall/codesamples/techlogo.gif")
        self.html = self.response.read()
        self.response.close()

        b64_data = base64.encodebytes(self.html)
        self.image = PhotoImage(data=b64_data)

        pic = Label(self.rootWin,image=self.image)
        pic.grid(row=0,column=0,columnspan=2,padx=5,pady=5)
        
        #Login label
        l = Label(self.rootWin,text="Login",font=("Calibri",15,"bold"),fg="gold")
        l.grid(row=1,column=0,columnspan=2)

        #creates button frame
        self.frame = Frame(self.rootWin)
        self.frame.grid(row=4,column=1,padx=2,sticky=E)

        #creates Register button
        register = Button(self.frame,text="Register",command=self.toRegister)
        register.pack(side=RIGHT,padx=2,pady=5)

        #creates Login button
        login = Button(self.frame,text="Login",command=self.chooseCFunc)#,command=self.toLogin)
        login.pack(side=RIGHT,padx=2,pady=5)

##    def connect(self):
##        db = pymysql.connect(host="academic-mysql.cc.gatech.edu",
##                             user="yposhedly3",
##                             passwd="A8KvQybO",
##                             db="cs2316db")
##        return(db)

        
##    def toLogin(self):
##        self.connect()
##
##        try:
##            check login info
##        if customer:
##            self.chooseCFunc
##        if manager:
#            self.chooseMFunc
##        
##        except:
##            r = messagebox.showerror("Error!","An invalid username or password has been entered.")


###### REGISTER #######

    def toRegister(self):
        self.rootWin2 = Toplevel()
        self.rootWin.withdraw()
        self.rootWin2.title("Register")

        pic = Label(self.rootWin2,image=self.image)
        pic.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=W)

        n = Label(self.rootWin2,text="New User Registration",font=("Calibri",15,"bold"),fg="gold")
        n.grid(row=1,column=0,columnspan=2,pady=5)

        u = Label(self.rootWin2,text="Username:")
        u.grid(row=2,column=0,sticky=E)

        self.usv = StringVar()
        self.uE = Entry(self.rootWin2,textvariable=self.usv,width=30)
        self.uE.grid(row=2,column=1,padx=5)

        e = Label(self.rootWin2,text="Email Address:")
        e.grid(row=3,column=0,sticky=E)

        self.esv = StringVar()
        self.eE = Entry(self.rootWin2,textvariable=self.esv,width=30)
        self.eE.grid(row=3,column=1,padx=5)

        p = Label(self.rootWin2,text="Password:")
        p.grid(row=4,column=0,sticky=E)

        self.psv = StringVar()
        self.pE = Entry(self.rootWin2,textvariable=self.psv,width=30)
        self.pE.grid(row=4,column=1,padx=5)

        cp = Label(self.rootWin2,text="Confirm Password:")
        cp.grid(row=5,column=0,sticky=E)

        self.cpsv = StringVar()
        self.cpE = Entry(self.rootWin2,textvariable=self.cpsv,width=30)
        self.cpE.grid(row=5,column=1,padx=5)

        back = Button(self.rootWin2,text="Back",command=self.backLogin)
        back.grid(row=6,column=0,padx=5,pady=5,sticky=W)

        create = Button(self.rootWin2,text="Create",command=self.checkReg)
        create.grid(row=6,column=1,padx=5,pady=5,sticky=E)

    def backLogin(self):
        self.rootWin2.destroy()
        self.rootWin.deiconify()

    def checkReg(self):
##        self.connect()

        username = self.uE.get()
        email = self.eE.get()
        password = self.pE.get()
        confirm = self.cpE.get()
        if username == "" or email == "" or password == "" or confirm == "":
            r = messagebox.showerror("Error!","One or more fields has been left blank.")

##        check if username is avilable
##        else:
##            r = messagebox.showerror("Error!","The entered username is unavailable.")
##
        if password != confirm:
            r = messagebox.showerror("Error!","The entered passwords do not match.")
##
##        check if email address is valid and unique
##            self.next function
##        else:
##            r = messagebox.showerror("Error!","An invalid email address has been entered.")




###### CHOOSE CUSTOMER FUNCTION SCREEN #######

    def chooseCFunc(self):
        self.rootWinCF = Toplevel()
        self.rootWinCF.title("Menu")
        try:
            self.rootWin2.withdraw()
        except:
            self.rootWin.withdraw()

        pic = Label(self.rootWinCF,image=self.image)
        pic.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=W)

        c = Label(self.rootWinCF,text="Choose Functionality",font=("Calibri",15,"bold"),fg="gold")
        c.grid(row=1,column=0,columnspan=2,pady=5)

        view = Button(self.rootWinCF,text="View Train Schedule",fg="blue",command=self.typeTrainNum)
        view.grid(row=2,column=0,columnspan=2,pady=5)
        
        make = Button(self.rootWinCF,text="Make a new reservation",fg="blue",command=self.searchTrain)
        make.grid(row=3,column=0,columnspan=2,pady=5)

        update = Button(self.rootWinCF,text="Update a reservation",fg="blue")
        update.grid(row=4,column=0,columnspan=2,pady=5)

        cancel = Button(self.rootWinCF,text="Cancel a reservation",fg="blue",command=self.cancelReservation)
        cancel.grid(row=5,column=0,columnspan=2,pady=5)

        giveR = Button(self.rootWinCF,text="Give review",fg="blue",command=self.giveReview)
        giveR.grid(row=6,column=0,columnspan=2,pady=5)

        viewR = Button(self.rootWinCF,text="View review",fg="blue",command=self.viewReview)
        viewR.grid(row=7,column=0,columnspan=2,pady=5)

        school = Button(self.rootWinCF,text="Add school information (student discount)",fg="blue",command=self.addSchool)
        school.grid(row=8,column=0,columnspan=2,pady=5)

        logout = Button(self.rootWinCF,text="Log out",command=self.logout)
        logout.grid(row=9,column=1,padx=5,pady=5,sticky=E)

    def logout(self):
        try:
            self.rootWinCF.destroy()
        except:
            self.rootWinMF.destroy()
        self.rootWin.deiconify()


###### VIEW TRAIN SCHEDULE ########

    def typeTrainNum(self):
        self.rootWin5 = Toplevel()
        self.rootWin5.title("View Train Schedule")
        self.rootWinCF.withdraw()

        pic = Label(self.rootWin5,image=self.image)
        pic.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=W)

        v = Label(self.rootWin5,text="View Train Schedule",font=("Calibri",15,"bold"),fg="gold")
        v.grid(row=1,column=0,columnspan=2,pady=5)

        tNum = Label(self.rootWin5,text="Train Number:")
        tNum.grid(row=2,column=0,padx=5,pady=5)

        self.tNsv = StringVar()
        self.tNE = Entry(self.rootWin5,textvariable=self.tNsv,width=20)
        self.tNE.grid(row=2,column=1,padx=5,pady=5)

        search = Button(self.rootWin5,text="Search",command=self.trainSchedule)
        search.grid(row=3,column=0,columnspan=2,pady=10)

    def trainSchedule(self):
        tNum = self.tNE.get()
        if tNum == "":
            r = messagebox.showerror("Error!","Please enter a train number.")

        else:
            #check if train number is unique
            
            self.rootWinSched = Toplevel()
            self.rootWinSched.title("View Train Schedule")
            self.rootWin5.withdraw()

            v = Label(self.rootWinSched,text="View Train Schedule",font=("Calibri",15,"bold"),fg="gold")
            v.grid(row=1,column=0,columnspan=2,pady=5)

            ## table of train schedule ##

            back = Button(self.rootWinSched,text="Back",command=self.backViewTrain)
            back.grid(row=3,column=0,padx=10,pady=15)

    def backViewTrain(self):
        self.rootWinSched.destroy()
        self.rootWin5.deiconify()

####### MAKE A NEW RESERVATION ########

    ### search trains that fit criteria ###

    def searchTrain(self):
        self.rootWinSearch = Toplevel()
        self.rootWinSearch.title("Make a Reservation")
        self.rootWinCF.withdraw()

        pic = Label(self.rootWinSearch,image=self.image)
        pic.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=W)

        s = Label(self.rootWinSearch,text="Search Train",font=("Calibri",15,"bold"),fg="gold")
        s.grid(row=1,column=0,columnspan=2,pady=5)

        tNum = Label(self.rootWinSearch,text="Departs From")
        tNum.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        #populate with possible starting cities
        cities = ["Boston (BBY)","New York (Penn Station)"]

        self.departsFrom = StringVar()
        pulldownD = OptionMenu(self.rootWinSearch,self.departsFrom,*cities)
        pulldownD.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        r = Label(self.rootWinSearch,text="Arrives At")
        r.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        self.arrivesAt = StringVar()
        pulldownA = OptionMenu(self.rootWinSearch,self.arrivesAt,*cities)
        pulldownA.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        c = Label(self.rootWinSearch,text="Departure Date")
        c.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        self.departDatesv = StringVar()
        self.departDateE = Entry(self.rootWinSearch,textvariable=self.departDatesv,width=20)
        self.departDateE.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        submit = Button(self.rootWinSearch,text="Find Trains",command=self.selectDepart)
        submit.grid(row=5,column=1,padx=10,pady=15,sticky=E)

    ### of available trains, select which to buy ticket from ###
    
    def selectDepart(self):
        departsFrom = self.departsFrom.get()
        arrivesAt = self.arrivesAt.get()
        departDate = self.departDateE.get()
        
##        if departsFrom == "":
##            r = messagebox.showerror("Error!","Please select a departure city.")
##        elif arrivesAt == "":
##            r = messagebox.showerror("Error!","Please select an arrival location.")
##        elif departDate == "":
##            r = messagebox.showerror("Error!","Please enter a departure date.")
##
##        else:
        #locate trains
        
        self.rootWinSelectD = Toplevel()
        self.rootWinSelectD.title("Make a Reservation")
        self.rootWinSearch.withdraw()

        v = Label(self.rootWinSelectD,text="Select Departure",font=("Calibri",15,"bold"),fg="gold")
        v.grid(row=1,column=0,columnspan=2,pady=5)

        ## table of train schedule with costs ##

        back = Button(self.rootWinSelectD,text="Back",command=self.backToSearch)
        back.grid(row=3,column=0,padx=10,pady=15)

        search = Button(self.rootWinSelectD,text="Next",command=self.travelInfo)
        search.grid(row=3,column=1,padx=10,pady=15,sticky=E)

    def backToSearch(self):
        self.rootWinSelectD.destroy()
        self.rootWinSearch.deiconify()

    ### add number of baggages and passenger name ###

    def travelInfo(self):
        self.rootWinTravel = Toplevel()
        self.rootWinTravel.title("Make a reservation")
        self.rootWinSelectD.withdraw()

        v = Label(self.rootWinTravel,text="Travel Extras & Passenger Info",font=("Calibri",15,"bold"),fg="gold")
        v.grid(row=1,column=0,columnspan=2,pady=5)
        
        n = Label(self.rootWinTravel,text="Number of Baggage")
        n.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        self.numBag = IntVar()
        pulldownB = OptionMenu(self.rootWinTravel,self.numBag,0,1,2,3,4)
        pulldownB.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        small = Label(self.rootWinTravel,text="Every passenger can bring up to 4 baggage. 2 free of charge, 2 for $30 per bag",font=("Calibri",8))
        small.grid(row=3,column=0,columnspan=2,padx=5,pady=5,sticky=W)

        c = Label(self.rootWinTravel,text="Passenger Name")
        c.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        self.passNamesv = StringVar()
        self.passNameE = Entry(self.rootWinTravel,textvariable=self.passNamesv,width=30)
        self.passNameE.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        back = Button(self.rootWinTravel,text="Back",command=self.backToSelect)
        back.grid(row=5,column=0,padx=10,pady=15)

        search = Button(self.rootWinTravel,text="Next",command=self.reserveInfo)
        search.grid(row=5,column=1,padx=10,pady=15,sticky=E)

    def backToSelect(self):
        self.rootWinTravel.withdraw()
        self.rootWinSelectD.deiconify()

    ### shows reservation info and total calculated cost ###

    def reserveInfo(self):
        self.rootWinRes = Toplevel()
        self.rootWinRes.title("Make a reservation")
        self.rootWinTravel.withdraw()

        v = Label(self.rootWinRes,text="Make Reservation",font=("Calibri",15,"bold"),fg="gold")
        v.grid(row=0,column=0,columnspan=3,pady=5)

        cs = Label(self.rootWinRes,text="Currently Selected")
        cs.grid(row=1,column=0,padx=5,sticky=W)

        # table with reservation informaation

        # check if student discount is to be applied, if so:
        sd = Label(self.rootWinRes,text="Student Discount Applied")
        sd.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        tc = Label(self.rootWinRes,text="Total Cost")
        tc.grid(row=4,column=0,padx=5,sticky=W)

        #calculate total cost from database
        self.costIV = IntVar()
        #self.costIV.set(cost)
        self.costE = Entry(self.rootWinRes,textvariable=self.costIV,width=25)
        self.costE.grid(row=4,column=1,columnspan=2,padx=5,sticky=W)

        uc = Label(self.rootWinRes,text="Use Card")
        uc.grid(row=5,column=0,padx=5,sticky=W)

        cards = [2541] #get cards from database
        self.chosenCard = StringVar()
        pulldownC = OptionMenu(self.rootWinRes,self.chosenCard,*cards)
        pulldownC.grid(row=5,column=1,pady=5,sticky=W)

        ac = Button(self.rootWinRes,text="Add Card",fg="blue",command=self.payInfo)
        ac.grid(row=5,column=2,padx=5,pady=5,sticky=W)

        #still need to add function for going back and adding more trains
        ca = Button(self.rootWinRes,text="Continue adding a train",fg="blue")
        ca.grid(row=6,column=0,padx=5,pady=5,sticky=W)

        back = Button(self.rootWinRes,text="Back",command=self.backToTravel)
        back.grid(row=7,column=0,padx=10,pady=15,sticky=W)

        submit = Button(self.rootWinRes,text="Submit",command=self.confirmScreen)#,command=self.submitRes)
        submit.grid(row=7,column=2,padx=10,pady=15,sticky=E)

    def backToTravel(self):
        self.rootWinRes.withdraw()
        self.rootWinTravel.deiconify()

    #def submitRes(self):
        ## add all info to database ##

        # self.confirmScreen()

    def confirmScreen(self):
        self.rootWinCon = Toplevel()
        self.rootWinCon.title("Make a reservation")
        self.rootWinRes.withdraw()

        v = Label(self.rootWinCon,text="Confirmation",font=("Calibri",15,"bold"),fg="gold")
        v.grid(row=1,column=0,columnspan=2,pady=5)

        r = Label(self.rootWinCon,text="Reservation ID")
        r.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        resID = 12345
        self.resIDsv = StringVar()
        self.resIDsv.set(resID)
        self.resIDE = Entry(self.rootWinCon,textvariable=self.resIDsv,width=10)
        self.resIDE.grid(row=2,column=1,padx=5,pady=5)

        small = Label(self.rootWinCon,text="Thank you for your purchase! Please save reservation ID for your records.",font=("Calibri",8))
        small.grid(row=3,column=0,columnspan=2,padx=5,pady=5,sticky=W)

        back = Button(self.rootWinCon,text="Back to Choose Functionality",command=self.backConfirm)
        back.grid(row=4,column=0,columnspan=2,padx=10,pady=15)

    def backConfirm(self):
        self.rootWinCon.destroy()
        self.rootWinCF.deiconify()

    ## payment info ##

    def payInfo(self):
        self.rootWinPay = Toplevel()
        self.rootWinPay.title("Payment Information")
        self.rootWinRes.withdraw()

        v = Label(self.rootWinPay,text="Payment Information",font=("Calibri",15,"bold"),fg="gold")
        v.grid(row=0,column=0,columnspan=4,pady=5)

        ## ADD CARD ##
        
        ac = Label(self.rootWinPay,text="Add Card",font=("Calibri",12,"bold"))
        ac.grid(row=1,column=0,padx=5,pady=10,sticky=W)

        n = Label(self.rootWinPay,text="Name on Card")
        n.grid(row=2,column=0,padx=5,sticky=W)

        self.nameCsv = StringVar()
        self.nameCE = Entry(self.rootWinPay,textvariable=self.nameCsv,width=20)
        self.nameCE.grid(row=2,column=1,padx=5,sticky=W)

        cn = Label(self.rootWinPay,text="Card Number")
        cn.grid(row=3,column=0,padx=5,sticky=W)

        self.cardNumsv = StringVar()
        self.cardNumE = Entry(self.rootWinPay,textvariable=self.cardNumsv,width=20)
        self.cardNumE.grid(row=3,column=1,padx=5,sticky=W)

        cv = Label(self.rootWinPay,text="CVV")
        cv.grid(row=4,column=0,padx=5,sticky=W)

        self.cvvSV = StringVar()
        self.cvvE = Entry(self.rootWinPay,textvariable=self.cvvSV,width=5)
        self.cvvE.grid(row=4,column=1,padx=5,sticky=W)

        ex = Label(self.rootWinPay,text="Expiration Date")
        ex.grid(row=5,column=0,padx=5,sticky=W)

        self.exDatesv = StringVar()
        self.exDateE = Entry(self.rootWinPay,textvariable=self.exDatesv,width=10)
        self.exDateE.grid(row=5,column=1,padx=5,sticky=W)

        submit1 = Button(self.rootWinPay,text="Submit")#,command=self.addCard)
        submit1.grid(row=6,column=0,columnspan=2)

        ## DELETE CARD ##

        dc = Label(self.rootWinPay,text="Delete Card",font=("Calibri",12,"bold"))
        dc.grid(row=1,column=2,padx=30,pady=10,sticky=W)

        cn2 = Label(self.rootWinPay,text="Card Number")
        cn2.grid(row=2,column=2,padx=30,sticky=W)

        cards = [2541] #get cards from database
        self.delCard = StringVar()
        pulldownDC = OptionMenu(self.rootWinPay,self.delCard,*cards)
        pulldownDC.grid(row=2,column=3,padx=15,pady=5,sticky=W)

        submit2 = Button(self.rootWinPay,text="Submit")#,command=self.deleteCard)
        submit2.grid(row=6,column=2,columnspan=2,pady=20)

    #def addCard(self):
        #add card info to database

    #def deleteCard(self):
        #delete card info from database


        

####### CANCEL RESERVATION ######

    def cancelReservation(self):
        self.rootWinCR = Toplevel()
        self.rootWinCR.title("Cancel Reservation")
        self.rootWinCF.withdraw()

        pic = Label(self.rootWinCR,image=self.image)
        pic.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=W)

        v = Label(self.rootWinCR,text="Cancel Reservation",font=("Calibri",15,"bold"),fg="gold")
        v.grid(row=1,column=0,columnspan=2,pady=5)

        rNum = Label(self.rootWinCR,text="Reservation ID")
        rNum.grid(row=2,column=0,padx=5,pady=5)

        self.rIDsv = StringVar()
        self.rIDE = Entry(self.rootWinCR,textvariable=self.rIDsv,width=15)
        self.rIDE.grid(row=2,column=1,padx=5,pady=5)

        back = Button(self.rootWinCR,text="Back",command=self.backCancel)
        back.grid(row=3,column=0,padx=10,pady=15,sticky=W)

        search = Button(self.rootWinCR,text="Search",command=self.cancel)
        search.grid(row=3,column=1,padx=10,pady=15,sticky=E)

    def backCancel(self):
        self.rootWinCR.destroy()
        self.rootWinCF.deiconify()

    def cancel(self):
        rID = self.rIDE.get()
        if rID == "":
            r = messagebox.showerror("Error!","Please enter a reservation ID.")

        else:
        #check for reservation ID in database and that it has not already been cancelled

            self.rootWinC = Toplevel()
            self.rootWinC.title("Cancel Reservation")
            self.rootWinCR.withdraw()

            v = Label(self.rootWinC,text="Cancel Reservation",font=("Calibri",15,"bold"),fg="gold")
            v.grid(row=1,column=0,columnspan=2,pady=5)

        ## table with reservations listed ##

        #total cost of reservation

            c = Label(self.rootWinC,text="Total Cost of Reservation")
            c.grid(row=3,column=0,padx=5,pady=5,sticky=W)

            #cost = (from database)
            self.costRiv = IntVar()
            #self.costRsv.set(cost)
            self.costRE = Entry(self.rootWinC,textvariable=self.costRiv,width=15)
            self.costRE.grid(row=3,column=1,padx=5,pady=5)
            
        #date of cancellation
            
            d = Label(self.rootWinC,text="Date of Cancellation")
            d.grid(row=4,column=0,padx=5,pady=5,sticky=W)

            self.datesv = StringVar()
            self.datesv.set(datetime.date.today())
            self.dateE = Entry(self.rootWinC,textvariable=self.datesv,width=15)
            self.dateE.grid(row=4,column=1,padx=5,pady=5)

        #amount to be refunded
            
            amount = Label(self.rootWinC,text="Amount to be Refunded")
            amount.grid(row=5,column=0,padx=5,pady=5,sticky=W)

            #refund = (from database)
            self.rfiv = IntVar()
            #self.rfiv.set(refund)
            self.rfE = Entry(self.rootWinC,textvariable=self.rfiv,width=15)
            self.rfE.grid(row=5,column=1,padx=5,pady=5)

        #navigation buttons
            
            back = Button(self.rootWinC,text="Back",command=self.backCancel)
            back.grid(row=6,column=0,padx=10,pady=15,sticky=W)

            search = Button(self.rootWinC,text="Submit")#,command=self.cancel)
            search.grid(row=6,column=1,padx=10,pady=15,sticky=E)

####### GIVE REVIEW ########

    def giveReview(self):
        self.rootWinGR = Toplevel()
        self.rootWinGR.title("Give Review")
        self.rootWinCF.withdraw()

        pic = Label(self.rootWinGR,image=self.image)
        pic.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=W)

        g = Label(self.rootWinGR,text="Give Review",font=("Calibri",15,"bold"),fg="gold")
        g.grid(row=1,column=0,columnspan=2,pady=5)

        tNum = Label(self.rootWinGR,text="Train Number")
        tNum.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        self.tNRsv = StringVar()
        self.tNRE = Entry(self.rootWinGR,textvariable=self.tNRsv,width=30)
        self.tNRE.grid(row=2,column=1,padx=5,pady=5)        

        r = Label(self.rootWinGR,text="Rating")
        r.grid(row=3,column=0,padx=5,pady=5,sticky=W)
    
        self.rating = StringVar()
        pulldown = OptionMenu(self.rootWinGR,self.rating,"Very Good","Good","Neutral","Bad","Very Bad")
        pulldown.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        
        c = Label(self.rootWinGR,text="Comment")
        c.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        self.comsv = StringVar()
        self.comE = Entry(self.rootWinGR,textvariable=self.comsv,width=30)
        self.comE.grid(row=4,column=1,padx=5,pady=5)

        submit = Button(self.rootWinGR,text="Submit",command=self.submitReview)
        submit.grid(row=5,column=1,padx=10,pady=15,sticky=E)

    def submitReview(self):
        trainNum = self.tNRE.get()
        rating = self.rating.get()
        comment = self.comE.get()
        
        if trainNum == "":
            r = messagebox.showerror("Error!","Please enter a train number.")
        elif rating == "":
            r = messagebox.showerror("Error!","Please select a rating.")
        #check if train number is not available in database
            #r = messagebox.showerror("Error!","This train number is unavailable.")
            
        else:
            #assign review and comment to train number
            self.rootWinGR.destroy()
            self.rootWinCF.deiconify()
        

####### VIEW REVIEW ##########

    def viewReview(self):
        self.rootWinVR = Toplevel()
        self.rootWinVR.title("View Review")
        self.rootWinCF.withdraw()

        pic = Label(self.rootWinVR,image=self.image)
        pic.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=W)

        v = Label(self.rootWinVR,text="View Review",font=("Calibri",15,"bold"),fg="gold")
        v.grid(row=1,column=0,columnspan=2,pady=5)

        tNum = Label(self.rootWinVR,text="Train Number:")
        tNum.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        self.tNVRsv = StringVar()
        self.tNVRE = Entry(self.rootWinVR,textvariable=self.tNVRsv,width=20)
        self.tNVRE.grid(row=2,column=1,padx=5,pady=5)

        back = Button(self.rootWinVR,text="Back",command=self.backReview)
        back.grid(row=3,column=0,padx=10,pady=15,sticky=W)

        find = Button(self.rootWinVR,text="Next",command=self.reviewTable)
        find.grid(row=3,column=1,padx=10,pady=15,sticky=E)

    def backReview(self):
        self.rootWinVR.destroy()
        self.rootWinCF.deiconify()

    def reviewTable(self):
        self.rootWinRT = Toplevel()
        self.rootWinRT.title("View Review")
        self.rootWinVR.withdraw()

        pic = Label(self.rootWinRT,image=self.image)
        pic.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=W)

        v = Label(self.rootWinRT,text="View Review",font=("Calibri",15,"bold"),fg="gold")
        v.grid(row=1,column=0,columnspan=2,pady=5)

        back = Button(self.rootWinRT,text="Back to Choose Functionality",command=self.backReviewTable)
        back.grid(row=3,column=0,columnspan=2,padx=10,pady=15)

    def backReviewTable(self):
        self.rootWinRT.destroy()
        self.rootWinCF.deiconify()


##### ADD SCHOOL INFO #######

    def addSchool(self):
        self.rootWin4 = Toplevel()
        self.rootWin4.title("Add School Information")
        self.rootWinCF.withdraw()

        pic = Label(self.rootWin4,image=self.image)
        pic.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=W)

        a = Label(self.rootWin4,text="Add School Info",font=("Calibri",15,"bold"),fg="gold")
        a.grid(row=1,column=0,columnspan=2,pady=5)

        school = Label(self.rootWin4,text="School Email Address:")
        school.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        self.sesv = StringVar()
        self.seE = Entry(self.rootWin4,textvariable=self.sesv,width=30)
        self.seE.grid(row=2,column=1,padx=5,pady=5)

        small = Label(self.rootWin4,text="Your school email address ends with .edu",font=("Calibri",8))
        small.grid(row=3,column=0,columnspan=2,padx=5,pady=5,sticky=W)

        back = Button(self.rootWin4,text="Back",command=self.backSchool)
        back.grid(row=4,column=0,padx=10,pady=15,sticky=W)

        submit = Button(self.rootWin4,text="Submit",command=self.submitSchool)
        submit.grid(row=4,column=1,padx=10,pady=15,sticky=E)

    def backSchool(self):
        self.rootWin4.destroy()
        self.rootWinCF.deiconify()

    def submitSchool(self):
        schoolEmail = self.seE.get()
        
        if schoolEmail.endswith(".edu") == True:
            print("True")
            #add student to customer in database
            self.rootWin4.destroy()
            self.rootWinCF.deiconify()
        else:
            r = messagebox.showerror("Error!","This is not a valid school email address.")


####### CHOOSE MANAGER FUNCTION SCREEN ########

    def chooseMFunc(self):
        self.rootWinMF = Toplevel()
        self.rootWinMF.title("Menu")
        self.rootWin.withdraw()

        pic = Label(self.rootWinMF,image=self.image)
        pic.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=W)

        c = Label(self.rootWinMF,text="Choose Functionality",font=("Calibri",15,"bold"),fg="gold")
        c.grid(row=1,column=0,columnspan=2,pady=5)

        rev = Button(self.rootWinMF,text="View revenue report",fg="blue",command=self.viewRevenue)
        rev.grid(row=2,column=0,columnspan=2,pady=5)
        
        route = Button(self.rootWinMF,text="View popular route report",fg="blue",command=self.viewPopular)
        route.grid(row=3,column=0,columnspan=2,pady=5)

        logout = Button(self.rootWinMF,text="Log out",command=self.logout)
        logout.grid(row=4,column=1,padx=5,pady=10,sticky=E)
    


        
######## VIEW REVENUE REPORT ########

    def viewRevenue(self):
        self.rootWinRev = Toplevel()
        self.rootWinRev.title("Manager")
        self.rootWinMF.withdraw()

        c = Label(self.rootWinRev,text="View Revenue Report",font=("Calibri",15,"bold"),fg="gold")
        c.grid(row=1,column=0,columnspan=2,pady=5)

        b = Button(self.rootWinRev,text="Back",command=self.backRMgr)
        b.grid(row=2,column=0,padx=10,pady=15)

    def backRMgr(self):
        self.rootWinRev.destroy()
        self.rootWinMF.deiconify()

######## VIEW POPULAR ROUTE REPORT ########

    def viewPopular(self):
        self.rootWinPop = Toplevel()
        self.rootWinPop.title("Manager")
        self.rootWinMF.withdraw()

        c = Label(self.rootWinPop,text="View Popular Route Report",font=("Calibri",15,"bold"),fg="gold")
        c.grid(row=1,column=0,columnspan=2,pady=5)

        b = Button(self.rootWinPop,text="Back",command=self.backPMgr)
        b.grid(row=2,column=0,padx=10,pady=15)

    def backPMgr(self):
        self.rootWinPop.destroy()
        self.rootWinMF.deiconify()

        m=Label(self.rootWinUR,text="Update Reservation",font=("Calibri",15,"bold"),fg="gold")
        m.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

        rNum1= Label(self.rootWinUR,text="Reservation ID")
        rNum1.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

        self.uIDsv= StringVar()
        self.uIDE= Entry(self.rootWinUR,textvariable=self.uIDsv,width=15)
        self.uIDE.grid(row=2,column=1,padx=5,pady=5)

        back1=Button(self.rootWinUR,text="Back",command=self.backUpdate)
        back1.grid(row=3,column=1,padx=10,pady=15,sticky=E)

        search1=Button(self.rootWinUR,text="Search",command=self.update)
        search1.grid(row=3,column=1,padx=10,pady=15,sticky=E)

     def updateReservation(self):
        
        self.rootWinUR=Toplevel()
        self.rootWinUR.title("Update Reservation")
        self.rootWinCF.withdraw()
        
        pic9=Label(self.rootWinUR,image=self.image)
        pic9.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=W)

    def backUpdate(self):
        self.rootWinUR.destroy()
        self.rootWinCF.deiconify()
        
win = Tk()
app = GUI(win)
win.mainloop()

import random
import pickle
import sys

logged_in = False #global variable
uid = 0
pwd = ''

class train:
    def __init__(self,name = '', num = 0, arr_time = '', dep_time = '', src = '', des = '', day_of_travel = '',seat_available_in_1AC = 0, seat_available_in_2AC = 0, seat_available_in_SL = 0, fare_1AC = 0, fare_2AC=0,fare_SL=0):
        self.name = name
        self.num = num
        self.arr_time = arr_time
        self.dep_time = dep_time
        self.src = src
        self.des = des
        self.day_of_travel = day_of_travel
        self.seats = {'1AC' : seat_available_in_1AC, '2AC' : seat_available_in_2AC, 'SL' : seat_available_in_SL}
        self.fare = {'1AC' : fare_1AC, '2AC' : fare_2AC, '3AC' : fare_SL}
    def print_seat_availablity(self):
        print("no. of seats available in 1AC :- "+str(self.seats['1AC']))
        print("no. of seats available in 2AC :- "+str(self.seats['2AC']))
        print("no. of seats available in SL :- "+str(self.seats['SL']))
    def check_avaiability(self,coach = '', ticket_num = 0):
        coach = coach.upper()
        if coach not in ('SL','1AC','2AC'):
            print_seat_availablity()
            coach = input("Enter the coach (1AC/2AC/SL):-")
        else:
            if self.seats[coach] == 0:
                return False
            elif self.seats[coach] >= ticket_num:
                return True
            else:
                return False
    def book_ticket (self,coach = '',no_of_tickets = 0):
        self.seats[coach] -= no_of_tickets
        return True
class tickeṭ:
    def __init__(self,train,user,ticket_num,coach):
        self.pnr = str(train.num)+str(user.uid)+str(random.randint)
        self.train_num = train.num
        self.coach = coach
        self.uid = user.uid
        self.train_name = train.name
        self.user_name = user.name
        self.ticket_num = ticket_num
        user.history.update({self.pnr : self})
        ticket_dic.update({self.pnr : self})

class user:
    def __init__(self,uid = 0, name= '', hometown= '', cellnumber= '', pwd = ''):
        self.uid = uid
        self.name = name
        self.hometown = ''
        self.cellnumber = ''
        self.pwd = pwd
        self.history = {}

class acceptors:
    ''' class containing fuctions for accepting and validating values properly'''
    def accept_uid():
        uid = 0
        try:
            uid = int(input("Enter your user ID :-"))
        except ValueError():
            print("please enter valid user ID.")
            return acceptors.accept_uid()
        else:
            return uid

    def accept_pwd():
        pwd = input("Enter your ppassword:-")
        return pwd

    def accept_train_number():
        train_num = 0
        try:
            train_num = int(input("Enter your train number :-"))
        except ValueError:
            print("please check your given train number:-")
            return acceptors.accept_train_number()
        else:
            if train_num not in train:
                print("please enter valid train number :-")
                return acceptors.accept_train_number()
            else:
                return train_num
    def accept_menu_option():
        option = input("Enter your optin:-")
        if option not in ('1','2','3','4','5','6','7','8'):
            print("please enter a valid optin!")
            return acceptors().accept_menu_option()
        else:
            return int(option)
    
    def accept_coach():
        coach = input("Enter the coach :-")
        coach = coach.upper()
        if coach not in ('SL','1AC','2AC'):
            print("please enter coach properly.")
            return acceptors().accept_coach()
        else:
            return coach
    def accept_prompt():
        prompt = input("cofirm? (y/n) :-")
        if prompt not in ('y','n'):
            print("please choose proper choice.")
            return acceptors().accept_prompt() 
        else:
            return prompt
    def accept_ticket_number():
        ticket_num = 0
        try:
            ticket_num = int(input("Enter your ticket number :-"))
            if ticket_num < 0:
                raise ValueError()
        except ValueError:
            print("Enter proper ticket number.")
            return acceptors.accept_ticket_number()
       
        else:
            return ticket_num
    def accept_pnr():
        pnr = input("Enter your pnr numnber :-")
        if pnr not in ticket_dic:
            print("please enter proper pnr number.")
        else:
            return pnr


def book_ticket():
    if not logged_in:
        login('p')

    check_seat_availabilty('p')
    choice = acceptors.accept_train_number()
    train(choice).print_seat_availablity()
    coach = acceptors().accept_coach()
    ticket_num = acceptors().accept_ticket_number()
    if trains[choice].check_avaiability(coach,ticket_num):
        print ("you have to pay :-", train[choice].fare[choice]*train_num)
        prompt = acceptors().accept_prompt()
        if prompt == 'y':
            train[choice].book_ticket(coach,ticket_num)
            print("Booking succesfull!/n/n")
            tick = ticket(train[choice].user[uid],ticket_num,coach)
            print("please note your pnr number :- ", tick.pnr, "/n/n")
            menu()
        else:
            print("exit.../n/n")
    else:
        print(ticket_num, "tickets not available")
        menu()

def cancel_ticket():
    pnr = acceptors().accept_pnr()
    if pnr in ticket_dic:
        check_pnr(pnr)
        print("cancel the ticket?")
        prompt == 'y'
        if logged_in:
            print("Ticket cancelled. /n")
            train[train_dic[pnr].train_num].seats[ticket_dic[pnr].coach]
            del user[ticket_dic[pnr].uid].history[pnr]
            del ticket_dic[pnr]
        else:
            print("/n Ticket not cancelled")
    menu()

def check_seat_availabilty(flag = ''):
    src = input("Enter the source station:-")
    des = input("Enter the destination station")
    flag_2 = 0
    for i in train:
        if train[i].src == src and train[i].des == des:
            print("Train name :-", train[i].name, " " ,"Number :-" ,train[i].num)
            flag_2 += 1
    if flag_2 == 0:
        print(" No train found in between the stations your enetered")
        menu()
    if flag == '':
        train_num = acceptors().accept_train_number()
        train[train_num].print_seat_availablity()
        menu()
    else:
        pass

def check_pnr(pnr = ''):
    if pnr == '':
        pnr = acceptors().accept_pnr()
        print()
        print("user name:- ", ticket_dic[pnr].user_name)
        print("train name:- ",ticket_dic[pnr].train_name)
        print("train number :- ", ticket_dic[pnr].train_num, "source :-", ticket_dic[pnr].src , "destination:-", ticket_dic[pnr].des)
        print("number of train tickets bookes :- ", ticket_dic[pnr].ticket)
        print()
        menu()
    else:
        print()
        print("user name:- ", ticket_dic[pnr].user_name)
        print("train name:- ",ticket_dic[pnr].train_name)
        print("train number :- ", ticket_dic[pnr].train_num, "source :-", ticket_dic[pnr].src , "destination:-", ticket_dic[pnr].des)
        print("number of train tickets bookes :- ", ticket_dic[pnr].ticket)
        print()
def create_new_accaount():
    user_name = input("enter your name :-")
    pwd = input("enter your password :-")
    uid = random.randint(1000, 9999)
    hometown = input("Enter your home town :- ")
    cellnumber = input("enter your mobile number:- ")
    u = user(uid,user_name,hometown,cellnumber,pwd)
    print("your user ID is :- ",uid)
    user.update({u.uid : u})
    menu()


def login(flag = ''):
    global uid
    global pwd
    uid = acceptors().accept_uid()
    pwd = acceptors().accept_pwd()
    if uid in user and user[uid].pwd == pwd:
        print ("/n welcome ", user[uid].name, "! /n")
        global logged_in
        logged_in = True
    else:
        print(" /n No such user id/ wrong password! /n")
        return login()
    if flag ==  '':
        menu()
    else:
        pass
def check_previous_booking():
    if not logged_in:
        login('p')
    for i in user[uid].history:
        print("/n pnr number :", i)
        check_pnr(i)
    menu() 
def end():
    s()
    print("----------------------------------------------THANKYOU---------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------------------------------------")
    sys.exit()
t1 = train('odisha',12345,'12:34','22:12','ctc','kgp','wed',30,23,43,2205,320,234)
t2 = train('howrah',12565,'10:24','10:30','kol','mac','thursday',30,23,43,2500,650,500)
trains = {t1.num:t1,t2.num:t2}
u1 = user(1111,'akash','jaggampeta','1234567890','akash')
u2 = user(1234,'akash1','jaggampeta1','1234567890','akash1')
user = {u1.uid:u1,u2.uid:u2}
ticket_dic = ()

def load():
    global trains, user, ticket_dic
    with open ("data.pk1","rb")as f:
        trains = pickle.load(f)
        users = pickle.load(f)
        ticket_dict = pickle.load(f)

def s():
    with open ("data.pkl","wb")as f:
        pickle.dump(trains,f)
        pickle.dump(users,f)
        pickle.dump(tickle_dic,f)


def menu():
    print("choose one of the following option:-")
    print("1.Book Ticket")
    print("2.Cancel ticket")
    print("3.check pnr")
    print("4.check seat availability")
    print("5.create new account")
    print("6.check previous booking")
    print("7.login")
    print("8.Exit")
    func = {1:book_ticket, 2 : cancel_ticket, 3 : check_pnr, 4: check_seat_availabilty, 5: create_new_accaount, 6: check_previous_booking, 7: login, 8: exit }
    option = acceptors.accept_menu_option()
    func[option]()

menu()

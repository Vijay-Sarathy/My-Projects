from datetime import datetime
def gethour():
    now = datetime.now()
    current_time = now.strftime("%H")
    return int(current_time)
def printtime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("\n\n\nA.K.R Homely Mess             ",current_time)
def p(c, n):
    str = "{:11} = {}"
    print(str.format(n, c))

def printprice(n, p):
    str = "{:11} = Rs.{}"
    print(str.format(n, p))


def Morning():
    Idly = 4
    Dosa = 10
    Chapathi = 10
    Vadai = 5
    Pongal = 20
    Icount = int(input("Idly: "))
    Dcount = int(input("Dosa: "))
    Ccount = int(input("Chapathi:"))
    Vcount = int(input("Vadai: "))
    Pcount = int(input("Pongal: "))
    Bill = Idly*Icount+Dosa*Dcount+Chapathi*Ccount+Vadai*Vcount+Pongal*Pcount
    parcel = input("is parcel: ")
    if parcel == "yes":
        Bill += 10
    printtime()
    if Icount != 0:
        p(Icount, ' Idly ')
    if Dcount != 0:
        p(Dcount, ' Dosa ')
    if Ccount != 0:
        p(Ccount, ' Chapathi ')
    if Vcount != 0:
        p(Vcount, ' Vadai ')
    if Pcount != 0:
        p(Pcount, ' Pongal ')

    return Bill

def afrn():
    Meals=40
    Briyani=70
    Chickengravy=50
    Egg=10
    Fishfry=40
    Mcount = int(input("Meals: "))
    Bcount = int(input("Briyani: "))
    Ccount = int(input("Chickengravy: "))
    Ecount = int(input("Egg: "))
    Fcount = int(input("Fishfry: "))
    Bill = Meals * Mcount + Briyani * Bcount + Chickengravy * Ccount + Egg * Ecount + Fishfry * Fcount
    parcel = input("is parcel: ")
    if parcel == "yes":
        Bill += 10
    printtime()
    if Mcount != 0:
        p(Mcount, ' Meals ')
    if Bcount != 0:
        p(Bcount, ' Briyani ')
    if Ccount != 0:
        p(Ccount, ' Chickengravy ')
    if Ecount != 0:
        p(Ecount, ' Egg ')
    if Fcount != 0:
        p(Fcount, ' Fishfry ')

    return Bill

def night():
   Idly=4
   Dosa=10
   Chapathi=10
   Parota=10
   Egg=10
   Icount = int(input("Idly: "))
   Dcount = int(input("Dosa: "))
   Ccount = int(input("Chapathi: "))
   Pcount = int(input("Parota: "))
   Ecount = int(input("Egg: "))
   Bill = Idly * Icount + Dosa * Dcount + Chapathi * Ccount + Parota * Pcount + Egg * Ecount
   parcel = input("is parcel: ")
   if parcel == "yes":
       Bill += 10
   printtime()
   if Icount != 0:
       p(Icount, ' Idly ')
   if Dcount != 0:
       p(Dcount, ' Dosa ')
   if Ccount != 0:
       p(Ccount, ' Chapathi ')
   if Pcount != 0:
       p(Pcount, ' Parota ')
   if Ecount != 0:
       p(Ecount, ' Egg ')

   return Bill

Bill=0
time = gethour()
if(time>=7 and  time<=10):
   Bill=Morning()
elif (time >=12 and time <=15):
    Bill=afrn()
elif(time>=19 and time<=23):
    Bill= night()

printprice("Net Amount",Bill)
Gst=Bill/10
printprice("Gst",Gst)
printprice("Total",Bill+Gst)
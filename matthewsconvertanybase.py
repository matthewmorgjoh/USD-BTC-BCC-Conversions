letters = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15, "G":16, "H":17, "I":18, "J":19, "K":20, "L":21, "M":22, "N":23, "O":24, "P":25, "Q":26, "R":27, "S":28, "T":29, "U":30, "V":31, "W":32, "X":33, "Y":34, "Z":35}
numbers = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F", 16:"G", 17:"H", 18:"I", 19:"J", 20:"K", 21:"L", 22:"M", 23:"N", 24:"O", 25:"P", 26:"Q", 27:"R", 28:"S", 29:"T", 30:"U", 31:"V", 32:"W", 33:"X", 34:"Y", 35:"Z"}

def anytodecint(theint, thebase):
    mycount = 0
    mylength = len(theint)

    while mycount < mylength:
        mydig = theint[mycount]
        if mydig.isalpha() == True:
            mydig = letters[mydig.capitalize()]
        else:
            mydig = int(mydig)
        if mycount == 0:
            mydecint = mydig * thebase
        elif mycount < mylength - 1:
            mydecint = mydecint + mydig
            mydecint = mydecint * thebase
        else:
            mydecint = mydecint + mydig
        mycount = mycount + 1
    return mydecint

def anytodecfrac(thefrac, thebase):
    mycount = -1
    mylength = -len(thefrac)
    mysum = 0
    while mycount >= mylength:
        mydigit = thefrac[mycount]
        if mydigit.isalpha() == True:
            mydigit = letters[mydigit.capitalize()]
        else:
            mydigit = thefrac[mycount]
        mysum = (float(mydigit) + mysum) / thebase
        mycount = mycount - 1
    return mysum

def dectoanyint(thedecint, thebase):
    myendnum = ""
    myquotient = thedecint
    while myquotient != 0:
        myremainder = myquotient % thebase
        myquotient = myquotient / thebase
        if myremainder > 9:
            myremainder = numbers[myremainder]
        else:
            "Do nothing"
        myendnum = str(myremainder) + myendnum
    return myendnum

def dectoanyfrac(thedecfrac, thebase):
    myproduct = thedecfrac
    myplace = 1
    newfrac = ""
    while myproduct != 0 and myplace <= 10:
        myresult = myproduct * thebase
        digittoleft, digittoright = str(myresult).split(".")
        if int(digittoleft) >= 10:
            digittoleft = numbers[int(digittoleft)]
        else:
            "Do nothing"
        newfrac = newfrac + digittoleft
        myproduct = float("." + digittoright)
        myplace = myplace + 1
    return newfrac

myint, myfrac = input("Please enter a real number:  ").split(".")
mybase = int(input("Please enter the source base of the number:  "))
newbase = int(input("Please enter the target for the conversion:  "))
#mynewline = int(myint) + float(myfrac)

#print type(myint)
#print type(myfrac)
#print type(mybase)
#print type(newbase)



myline = myint + "." + myfrac + "," + str(mybase) + "," + str(newbase)
#print myline

mynum, mybase, newbase = myline.split(",")
#print mynum, mybase, newbase
myint, myfrac = mynum.split(".")
mybase = int(mybase)
newbase = int(newbase)
myintresult = anytodecint(myint, mybase)
myfracresult = anytodecfrac(myfrac, mybase)
mynewresult = dectoanyint(myintresult, newbase)
mynewresult1 = dectoanyfrac(myfracresult, newbase)



print ("\n" +mynum, "in base", mybase, "is", str(mynewresult) + "." + str(mynewresult1), "in base", newbase)




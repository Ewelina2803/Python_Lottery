# Drawing of numbers to be bet in lotteries: "Extrapensja" and "Lotto".

import random

myNumbers=[]

while len(myNumbers)<5:
    newNumber=random.randint(1,35)
    if newNumber in myNumbers:
        print("Eliminated", newNumber)
        continue
    myNumbers.append(newNumber)
print("My numbers for EKSTRAPENSJA 5 of 35:",myNumbers)

myNumbers2=[]
while len(myNumbers2)<1:
    newNumber=random.randint(1,4)
    if newNumber in myNumbers2:
        print("Eliminated",newNumber)
        continue
    myNumbers2.append(newNumber)

print("My numbers for EKSTRAPENSJA 1 of 4:",myNumbers2)

myNumbers3=[]
while len(myNumbers3)<6:
    newNumber=random.randint(1,49)
    if newNumber in myNumbers3:
        print("Eliminated", newNumber)
        continue
    myNumbers3.append(newNumber)
print("My numbers for LOTTO 6 of 49:",myNumbers3)

#Ministry of Silly Codes July 2017
#Part5
#Lists and such

newList = [2,4,6,8,10]
print(newList[0])
#>>>2
newList[0] = 6
print(newList[0])
#>>>6
for i in range(5):
    print(newList[i])
#2
#4
#6
#8
#10

length = len(newList)
# length = 5
#Therefor...
for i in range(len(newList)):
    print(newList[i])
#... prints each element of a list of unknown size. BUT WAIT!...
for i in newList:
    print(i)
#will do the same thing.

#Operations on lists.
#sum of elements
total = 0
for i in newList:
    total += i
print(total)
#Python streamlined
sum(newList)

#Merge lists
list1 = [2,4,6]
list2 = [8,10,12]
list3 = list1 + list2
for i in list3:
    print(i)
#>>>2 4 6 8 10 12 (on individual lines)

#Append lists
list1 = [2,4,6,8]
list1.append(10)
print(list1)
#>>>[2,4,6,8,10]

#Index negative numbers
list1 = [2,4,6]
print(list1[-1])
#>>>6

#Slicing
list1 = [2,4,6,8,10,12,14,16]
list1[0:3]  #1st 3 elements (2 4 6)
list1[4:6]  #elements 4 and 5   (8 10)
list1[:6]   #1st 6 elements (2 4 6 8 10 12)
list1[-3:]  #last 3 elements (12 14 16)
list1[:]    #copy of list

#In practice
daysByMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
daysInSummer = daysByMonth[5:8]  #Jun-Aug are elements 5-8; remember count from 0
daysFirstQ = daysByMonth[:3]  #Jan-Mar are elements 0-2
daysLastQ = daysByMonth[-3:]    #Oct-Dec are accessible counting backwards

#Tuples are like lists but the values can't change and the elements are typically various types.
creditCard = "Bank name", 1321321321321321, "Feb, 2020"
print(creditCard)
#Assign values from tuple to variables
bank, cardNum, expire = creditCard
print(bank)
#>>>Bank name







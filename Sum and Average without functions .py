#Sum/Average Program
#Your first and last name:Robert Hart
#Your student ID:s1197899

#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers
#Instead of searching for a name in the list
#   Compute the sum of all 10 numbers
#   Compute the average for all 10 numbers

#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:

numberList = []
sumInt = 0
avgInt = 0.0

for x in range(0,10):
    n1=(int(input("Enter a number:")))
    numberList.append(n1) 

for x in range (0,10):
    sumInt = sumInt + numberList[x]

avgInt = sumInt/10

print("The sum of the numbers you entered is ", sumInt)
print("The average of the numbers you entered is ", avgInt)

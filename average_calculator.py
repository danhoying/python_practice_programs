# AVERAGE CALCULATOR
# Calculates the average of a set of input numbers

import re

def getNumbers():
    numList = []
    print('This program will allow you to enter a series of numbers.')
    print()
    print('Press the "c" key when finished to calculate the average.')
    print('Press the "d" key to delete an entry.')
    print()
    while True:
        number = input('Please enter a number: ')
        try:
            numList.append(float(number))
            print(numList)
            print()
        except ValueError:
            if number == 'd': # Allows user to delete a number already entered
                try:
                    print()
                    print(numList)
                    delete = float(input('Which number would you like to delete? '))
                    numList.remove(delete)
                    print(delete, 'has been deleted.')
                    print()
                except ValueError:
                    print('That is not in the list.')
                    print()
            if number == 'c':
                return numList

myList = getNumbers()
print()
print('Okay, the numbers you have entered are:')
print()
for i in myList:
    print(i)
def average(numbers): # Calculates average from the list user inputted
    total = 0
    for i in numbers:
        total += i
    average = total / len(numbers)
    return average

myAverage = (average(myList))
print()
print('The average is:', myAverage)

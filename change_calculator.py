# CHANGE CALCULATOR
# Takes two inputs, the total amount owed and the customer payment amount,
# and calculates the total number of dollars and the amount of individual
# coins to be returned to the customer

quarters = 0
dimes = 0
nickels = 0
pennies = 0

def getTotalCost(): # function to get a valid float input (e.g. 9.75)
    while True:
        try:
            total = float(input("Enter the total cost: "))
        except ValueError:
            print("Please enter a monetary value")
        else:
            return total
            
def getCustPayment(cost): # function to get a valid float input (e.g. 9.75)
    while True:
        try:
            total = float(input("Enter the payment amount: "))
            while cost > total:
                print("You owe more money. Pay up!")
                total = float(input("Enter the payment amount: "))
        except ValueError:
            print("Please enter a monetary value")
        else:
            return total

cost = getTotalCost()
payment = getCustPayment(cost)
change = payment - cost # Determines the total change due

remainingChange = change - int(change) # Any change remaining less than 1 dollar

while remainingChange > .25:
    remainingChange -= .25
    quarters += 1
 
while remainingChange > .10:
    remainingChange -= .10
    dimes += 1

while remainingChange > .05:
    remainingChange -= .05
    nickels += 1

while remainingChange > .001: # Allows this loop to run if the remaining change is 
    remainingChange -= .01    # slightly less than 0.01 due to rounding errors      
    pennies += 1
    if .001 < remainingChange < .01: # accounts for float rounding errors
        pennies += 1                 # by adding an extra penny if necessary
        remainingChange -= .01
        
    
print()
print("Your change is: %.2f" % round(change,2))
print()
print("Dollars: ", int(change)) # Uses int value of change, therefore rounding
print("Quarters: ", quarters)   # down to total dollar amount
print("Dimes: ", dimes)
print("Nickels: ", nickels)
print("Pennies: ", pennies)
    


    

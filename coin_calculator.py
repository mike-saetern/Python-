# Write a function that given an amount of cents returns the fewest number of quarters, dimes, nickels, and pennies required to equal that amount.
#         coinCalculator(99) should return {"Quarters":3,"Dimes":2,"Nickels":0,"Pennies":4}
#     Bonus:
#         Account for Dollar increments as well (Ones/Fives/Tens/Twenties/Fifties/Hundreds)
#     Double Bonus:
#         Account for the elusive 2 dollar bills as well.

import math

def coin_cal(cents):
    change ={
        "quarters": 0,
        "dimes" : 0,
        "nickels" : 0,
        "pennies" : 0
    }
    
    change ["quarters"] = math.floor(cents/25)
    cents -= change["quarters"] * 25
    change ["dimes"] = math.floor(cents/10)
    cents -= change["dimes"] * 10
    change ["nickels"] = math.floor(cents/5)
    cents -= change["nickels"] * 5
    change ["pennies"] = math.floor(cents/1)
    return change
#code works with import math
print(coin_cal(99))

def divis_change(amount):
    change_left ={
        "Quarters":0,
        "Dimes":0,
        "Nickels":0,
        "Pennies":0
    }
    quarters = amount // 25
    change_left["Quarters"] = quarters
    amount -= 25 * quarters
    dimes = amount // 10
    change_left["Dimes"] = dimes
    amount -= 10 * dimes
    nickels = amount // 5
    change_left["Nickels"] = nickels
    amount -= 5 * nickels
    pennies = amount // 1
    change_left["Pennies"] = pennies
    return change_left
#code works
print(divis_change(99))




#Create function ​ThreesFives()​ that adds each value from 100 and 4000000 (inclusive) if that value is evenly divisible 
# by 3 or 5 ​but not both​. Display the final sum in the console.

def threes_fives(start,end):
    sum = 0
    for i in range(start,end):
        if i % 5 == 0:
            sum += i
        elif i % 3 == 0:
            sum += i
        
    return sum

print(threes_fives(100,4000000))


#write a function that adds each value from 100 to 4000000 if that value is evenly divisible by 3 or 5 but not both.
def threesandfives(num1,num2):
    total = 0
    for x in range(num1,num2+1):
        if x % 3 == 0 and x % 5 == 0:
            continue
        elif x % 3 == 0:
            total += x
        elif x % 5 == 0:
            total += x
    return(total)

print(threesandfives(100,4000000))


#write a function that given a number sums that numbers digits repeatedly until the sum is only one digit. return that final one digit results.
# sumToOne(99999981) would return 9
def sum_to_one(num):
    str_num = str(num)
    sum = num
    while sum >= 10:
        for i in range(len(str_num)-1):
            if sum >= 10:
                sum = int(str_num[i]) + int(str_num[i + 1])
    return sum

print(sum_to_one(99999981))
def sumToOne(num):
    str_num = str(num)
    for i in range(len(str_num)-1):
        if ((int(str_num[i])+int(str_num[i+1])<10) and (int(str_num[i])+int(str_num[i+1]) > 10)):
            return int(str_num[i] + int(str_num[i+1]))

print(sumToOne(99999981))

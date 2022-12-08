# - Write a function that accepts a list and returns whether that List has an even amount of values or 
# an odd amount of values. oddOrEvenList([1,2,3]) should return odd while  oddOrEvenList([1,2,3,4]) will return even

def odd_even_list(arr):
    for i in range(len(arr)):
        if len(arr) % 2 == 0:
            return ("even") 
        elif len(arr) % 2 != 0:
            return ("odd") 

print(odd_even_list([1,2,3,4]))
print(odd_even_list([1,2,3]))

# - write a function that given a string date such as "12/07/2022", return whether or not that a person's birthday
#  has passed this year. Birthday("07/29/1993") should return true
# bonus - return a string with the users current age and whether or not they have had a birthday, Birthday("07/29/1993") 
# should return "User is currently 29 years old and has had their birthday this year"

def has_past(birth, today):
    if(int(birth[:2]) < int(today[:2])):
        return True
    elif(int(birth[:2]) > int(today[:2])):
        return False
    elif(int(birth[3:5]) > int(today[3:5])):
        return False
    else:
        return True


print(has_past("07/29/1993", "12/07/2022"))
print(has_past("12/29/1993", "12/07/2022"))
print(has_past("12/06/1993", "12/07/2022"))

#write a function given a 12 hr am/pm format, returns time to military time
#     - example timeconvert('01:45:00PM') returns '13:45:00'
#     - example 2 timeconvert('12:59:00AM') returns '00:59:00'

def time_convert(time):
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if time[-2:] == "AM" and time[:2] == "12":
        return "00" + time[2:-2]
    # remove the AM    
    elif time[-2:] == "AM":
        return time[:-2]
    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif time[-2:] == "PM" and time[:2] == "12":
        return time[:-2]
    else:
        # add 12 to hours and remove PM
        return str(int(time[:2]) + 12) + time[2:8]

print(time_convert('01:45:00PM'))
print(time_convert('12:59:00AM'))

def timeconvert(time):
    hour = "00"
    if time[len(time)-2:] == "PM":
        if time[:2] == "12":
            hour = "12"
        else:
            hour = int(time[:2]) + 12
    else:
        if time[:2] != "12":
            hour = time[:2]
    return f'{hour}{time[2:len(time)-2]}'
# - rotate String
#         Create a standalone function that accepts a string and an integer, and rotates the characters in the string 
#  to the right by that amount. ex: given ("boris godunov",5) return "dunovBoris Go" 

def rotate(input,num):
    Rfirst = input[0 : len(input)-num]
    Rsecond = input[len(input)-num : ]
    return (Rsecond + Rfirst) 

print(rotate("boris godunov",5))

def rotate_string_right(s, n):
    first_part = s[-n:]
    second_part = s[:-n]
    return first_part + second_part

s = "Boris Godunov"
n = 5
result = rotate_string_right(s, n)
print(result) # dunovBoris Go

# when given two strings, the second string contains characters that must be romved from the first. return the resultant string

def string_dup(str,str2):
    for x in str2:
        if x in str:
            str = str.replace(x,'')
    print(str)

string_dup('abcde', "abts")

def strings(str1,str2):
    new_string = ""
    for i in str1:
        if i not in str2:
            new_string+= i
    print(new_string)

strings('abcde', "abts")
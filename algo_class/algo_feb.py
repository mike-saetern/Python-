#create a function that, given an input string, returns a boolean whether parenteses in the string are valid. 
#input 'y(3(p)p(3)r)s', returns true, given 'n(0(p)3' returns False given 'n)0(t()k' returns false)

def check_parethesis(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0

print(check_parethesis("y(3(p)p(3)r)s'"))
print(check_parethesis('n(0(p)3'))
print(check_parethesis("n)0(t()k"))


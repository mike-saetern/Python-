# - given a string of roman numbers ("VII") convert those roman numerals to their corresponding numerical value (7)
    # I = 1 , V = 5, X = 10, L = 50, C = 100, IV = 4, XL = 40

def roman_num(arg):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(arg)):
        if roman[arg[i]] > roman[arg[i-1]]:
            num += roman[arg[i]] - 2 * roman[arg[i-1]]
        else:
            num += roman[arg[i]]
    return num

print(roman_num('VII'))
print(roman_num('XL'))
print(roman_num('MMVI'))

def roman_numerals(string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for i in range(len(string)-1):
        if roman[string[i]] < roman[string[i+1]]:
            sum -= roman[string[i]]
        else:
            sum += roman[string[i]]
    sum += roman[string[len(string) - 1]]
    return sum

print(roman_numerals('XL'))
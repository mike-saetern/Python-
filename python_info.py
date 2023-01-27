num1 = 42 #variable declaration number
num2 = 2.3 #variable declaration decimal
boolean = True #variable declaration boolean
string = 'Hello World' #variable declaration string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declation dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declation tuple
print(type(fruit)) # print to console, type check
print(pizza_toppings[1])#print to console, list access value
pizza_toppings.append('Mushrooms')#list add value
print(person['name']) #print to console, ductionary access value
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #dictionary change value
print(fruit[2]) #print to console Tuple access data

if num1 > 45: #conditional if
    print("It's greater")#print to console
else: #conditional else
    print("It's lower")#print to console

if len(string) < 5: #conditional if
    print("It's a short word!") #print to console
elif len(string) > 15: #elif
    print("It's a long word!") #print to console
else: #else
    print("Just right!") #print to console

for x in range(5): #for loop from 0-5
    print(x) #print to console
for x in range(2,5): #for loop from 2-5
    print(x) #print to console
for x in range(2,10,3): #for loop from 2-10 add 3 each time
    print(x) #print to console
x = 0 #variable declaration
while(x < 5): #while loop
    print(x) #print to console
    x += 1 #increase x by 1

pizza_toppings.pop() #list delete at end
pizza_toppings.pop(1) #lis delete second 

print(person) #print to console of dictionary
person.pop('eye_color') #delete value from dictionary
print(person) #print to console

for topping in pizza_toppings: #for loop through list
    if topping == 'Pepperoni': #if statement
        continue
    print('After 1st if statement') #print to console
    if topping == 'Olives': #if statement
        break #stop the loop

def print_hello_ten_times(): #declare function
    for num in range(10): #for loop 0-10
        print('Hello') #print to console

print_hello_ten_times() #call function

def print_hello_x_times(x): #declare function with parameter x
    for num in range(x): #for loop with x parameter
        print('Hello') #print to console

print_hello_x_times(4) #call function with parameter 4

def print_hello_x_or_ten_times(x = 10): #declare function with parameter
    for num in range(x): #for loop until x
        print('Hello') #print to console

print_hello_x_or_ten_times() #function call goes to 10
print_hello_x_or_ten_times(4) #function call goes to 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
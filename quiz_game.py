print('Welcome to my quiz game!')
 
play = input('Do you want to play? Type yes to play. ')
 
if play.lower() != 'yes': #.lower makes all answers into lower case
    quit()
 
print("Okay! Let's play!")

count = 0
 
answer = input('Who is the leader of the seven deadly sins? ')
if answer.lower() == "meliodas":
    print('You got it correct!!')
    count += 1
else:
    print('Incorrect')
 
answer = input("Who bears the sin of greed? ")
if answer.lower() == "ban":
    print('You got it correct!!')
    count += 1
else:
    print('Incorrect')
 
answer = input("Who bears the sin of sloth? ")
if answer.lower() == "king":
    print('You got it correct!!')
    count += 1
else:
    print('Incorrect')
 
answer = input("Who bears the sin of pride? ")
if answer.lower() == "escanor":
    print('You got it correct!!')
    count += 1
else:
    print('Incorrect')
 
answer = input('Who bears the sin of envy? ')
if answer.lower() == "diane":
    print('You got it correct!!')
    count += 1
else:
    print('Incorrect')
 
print(f"You got {count}/5 correct!")
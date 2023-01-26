import random
 
player_wins= 0
cpu_wins = 0
choices = ["rock", "paper", "scissors"]
 
while True:
    player_input = input(" Type Rock/Paper/Scissors or Q to quit. ").lower()
    if player_input == "q":
        break
 
    if player_input not in choices:
        print("Please type Rock/Paper/Scissors")
        continue
 
    random_num = random.randint(0,2)
    #rock = 0 paper = 1 scissors = 2
    cpu_guess = choices[random_num]
    print("cpu picked", cpu_guess + ".")
 
    if player_input == cpu_guess:
        print("It's a tie!!")
 
    elif player_input == "rock" and cpu_guess == "scissors":
        print("You beat the cpu!!")
        player_wins += 1
 
    elif player_input == "paper" and cpu_guess == "rock":
        print("You beat the cpu!!")
        player_wins += 1
 
    elif player_input == "scissors" and cpu_guess == "paper":
        print("You beat the cpu!!")
        player_wins += 1
 
    else:
        print("You lost!")
        cpu_wins += 1
   
print("You beat the cpu", player_wins, "times")
print("The CPU beat you", cpu_wins, "times")
print("Thank you for playing, Goodbye!!")
name = input("Please type your name ")
print("Welcome", name, "to your adventure!")
 
answer = input("You wake up in the forest with no memory. You look around and see two paths, you can go right on the dirt path or left on the rocky path. Which direction would you like to go? Type left or right.").lower()
if answer == "left":
    print("You stepped on some jagged rocks and bleed to death. Game Over")
    quit()
 
elif answer == "right":
    print("You walk down the path to find a shield and sword.")
    answer2 = input("The shield has a lion logo while the sword has a dragon handle. Do you take the shield or sword? Type shield or sword.").lower()
    if answer2 == "shield":
        print("You take the shield. It is heavy and slows you down.")
        answer3  = input("The shield wears you down. Do you take or leave the shield. Type leave or take").lower()    
        if answer3 == "leave":  
            print("You get to the end of your path where a lion kills you. Game Over!!")
            print("Thank you for playing")
            quit()
        elif answer3 == "take":
            print("You drag the shield with you to the end of your path where a lion greets you")
            answer5 = input("You stay behind your shield as you see it glow and get hot. Do you run away or keep holding the shield? Type run or hold").lower()
            if answer5 == "run":
                print("You drop the shield, turn and run where the lion catches up to you promtly and kills you. Game Over")
                quit()
            elif answer5 == "hold":
                answer4 = input("The shield shoots a beam of light destroying the lion. You continue on until you reach a lake. You can swim or walk around the lake. Type swim or walk").lower()
                if answer4 == "swim":
                    print("While you swim across you run into a jelly fish that stings you causing instant death. Game Over")
                    quit()
                elif answer4 == "walk":
                    print("You walk around the lake to a path up to a castle. You follow the path into the castle gates where you are greeted by the princess. You have made it to the end. Thank you for playing")
                    quit()
            else:
                print("Invalid selection. You lose")
                quit()
        else:
            print("Invalid selection. You lose")
            quit()
    elif answer2 == "sword":
        print("You pick up the sword, It is weightless and lights up with flames. You walk to the end of your path, a lion greets you. You easily kill the lion.")
        answer4 = input("You continue walking to the end where you find a lake. You can swim acorss or walk around the lake. Type swim or walk")
        if answer4 == "swim":
            print("While you swim across you run into a jelly fish that stings you causing instant death. Game Over")
            quit()
        elif answer4 == "walk":
            print("You walk around the lake to a path up to a castle. You follow the path into the castle gates where you are greeted by the princess. You have made it to the end. Thank you for playing")
            quit()
    else:
        print("Invalid selection. You lose")
        quit()
 
else:
    print("Invalid selection. You lose")
    quit()
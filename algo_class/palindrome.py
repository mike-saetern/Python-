#visable building function
def visible_buildings(buildings):
    visible = []
    max_height = 0
    for i in range(len(buildings)):
        if buildings[i] > max_height: #checks value if it is bigger than max_height
            visible.append(buildings[i])#appends into list
            max_height = buildings[i]#max height becomes the value
    return visible

print(visible_buildings([-1,1,1,7,3,9,13,2]))

#create a function that returns true if word is a palidrome and returns false if it is not also account for case uppercases
def is_palindrome(word):
    # Convert the word to lowercase
    word = word.lower()
    # for loop through word
    for i in range(len(word)):
        # Check if the corresponding letter from the end of the word is the same
        if word[i] != word[len(word)-i-1]:
            # If not, return False
            return False
    # If all the letters match, return True
    return True

print(is_palindrome('racecaR'))

import random

def shuffle(arr):
    # Iterate over each index in the array, starting from the last one
    for i in range(len(arr)-1, 0, -1):
        # Generate a random index between 0 and i 
        j = random.randint(0, i)
        # Swap the elements at indices i and j
        arr[i], arr[j] = arr[j], arr[i]
    return arr

print(shuffle([4,6,7,2,6,100]))

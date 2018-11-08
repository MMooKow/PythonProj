#Guess my number LIMITED
#
#Program generates a number between 1 and 100. Player gueses number and when correct is given number of tries it took.
 
import random
roll = random.randint(1,100)
playerGuess = ""
tries = 0

while playerGuess != roll:
    print("You have", 10 - tries,"tries remaining.")
    playerGuess = int(input("Guess a number between 1 and 100: "))
    tries += 1
    if tries == 10:
        print("\nOut of tries!!!")
        break
    if playerGuess == roll:
        print("You guessed correct!!!!")
        print("\nThe number was", roll)
        print("It only took you", tries, "tries!")
        break
    
    if playerGuess > roll:
        if playerGuess > 100:
            print("The number wont be THAT high!\n")
        else:
            print("You guessed too high!\n")
    if playerGuess < roll:
        if playerGuess < 1:
            print("The number wont be THAT low!\n")
        else:
            print("You guessed too low!\n")
            
    continue

input("Press the enter key to exit...")

#Number Guessing Game Computer Version
#
#Player enters a number and the computer tries to guess that number

#setup
import random
import time
target = int(input("Enter a number for the computer to guess.\nIt wont look... I promise! Make sure it is between 1 and 100! "))
guess = 50

#computer guessing loop
while guess != target:
    
    if target < 50:
        guess = random.randint(1,49)
        print(guess)
        time.sleep(1)
    elif guess > target:
        guess = random.randint(guess,49)
    else:
        guess = random.randint(1,guess)

    if target > 50:
        guess = random.randint(51,100)
        difference = target - guess
        print(guess)
        time.sleep(1)

        if difference < 5:
            guess += 1
            print(guess)
            time.sleep(1)

else:
    print("\nThe computer guessed correctly!")
    print("The number was:", target)
    input("Press the enter key to exit...")

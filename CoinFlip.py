#Coin Flip
#
#Flips a coin 100 times and tells you how many heads and tails

import random
numFlip = 0
heads = 0
tails = 0

while numFlip < 100:
    coinFlip = random.randint(1, 100)
    numFlip += 1

    if coinFlip <= 50:
        heads += 1
    else:
        tails += 1

print("You flipped heads", heads, "times.")
print("You flipped tails", tails, "times.")

input("Press the enter key to exit...")

#Fortune Cookie
#
#Displays one of five random fortunes when run.

#impoting random
import random

#def fortunes
fort1 = "Eat Mor Chikin"
fort2 = "May you live in boring times"
fort3 = "A hiney is a terrible thing to leave un-popped"
fort4 = "Follow the golden chicken"
fort5 = "A garlic, pepper spray a day keeps the garden pests away... except gophers...and chickens..."

#fortune list
fortList = [fort1, fort2, fort3, fort4, fort5]

#roll
roll = random.randint(0,4)
print(fortList[roll])

input("\nPress the enter key to exit...")

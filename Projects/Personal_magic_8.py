import random
import sys

keep_playing = 'yes'

while keep_playing == 'yes':
    str(input("Please ask a yes or no question: ")).lower()
    response = random.randint(0,8)
    
    if response == 1:
        print("Absolutely")
    elif response == 2:
        print("Yes")
    elif response == 3:
        print("Don't count on it.")
    elif response == 4:
        print("Probably.")
    elif response == 5:
        print("I am unsure")
    elif response == 6:
        print("The Universe No.")
    elif response == 7:
        print("Let me think....Yes.")
    elif response == 8:
        print("To hard to answer, go with how you feel.")
   
    keep_playing = str(input("Do you want to ask another question? yes/no ")).lower()
    if keep_playing == 'no':
        print("Ok bye")
        sys.exit()
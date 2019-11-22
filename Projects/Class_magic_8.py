import random
import sys

ans = True

while ans:
    question = input("Ask the Magic 8 ball a question (press enter to quit) ")

    answers = random.randint(1, 8)

    if question == "":
        sys.exit()

    elif answers == 1:
        print("Yes")

    elif answers == 2:
        print("Maybe")

    elif answers == 3:
        print("Yolo")

    elif answers == 4:
        print("Ya")

    elif answers == 5:
        print("Yep")

    elif answers == 6:
        print("Nope")

    elif answers == 7:
        print("Never")

    elif answers == 8:
        print("No")


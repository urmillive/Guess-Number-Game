"""
    This is Very Simple Guess Number Game,
    you've only 
"""
import random

def game():
    computer_no = random.randint(0, 20)
    print("Hello Coder you're enter in Game")
    print("you\'ve only 5 change for won this game")
    x = 5
    while x > 0:
        guess_number = int(input("Enter you number : "))
        if (guess_number < computer_no):
            print("Please Enter greater number")
        elif (guess_number > computer_no):
            print("Please Enter Small number")
        elif (guess_number == computer_no):
            print("********You won the Match**********")
            break
        else:
            print("Sorry you lose this game")

        x = x - 1
        print("you\'ve only", x, "chance")


if __name__ == "__main__":
    game()

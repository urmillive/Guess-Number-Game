"""
    This is Very Simple Guess Number Game,
    you've only need to guess random number and computer also guess number and if 
    it's match then you won otherwise not.
"""
import random
def guess_the_number():
    dream_number = random.randint(0,25)
    no_of_guesses = 5

    print("enter number between 0 to 25")
    while no_of_guesses>0:
        n = int(input("Enter your Number : "))
        if n > dream_number:
            print("your number is greater than dream number 😌")
        elif n < dream_number:
            print("your number is less than dream number 😌")
        elif n == dream_number:
            print("congratulations you win 👏")
            print(f"you completed game with {no_of_guesses} chance 😎")
            break

        print(f"you have only {no_of_guesses-1} chances left")
        no_of_guesses-=1
    else:
        print("Game Over💀")
            

if __name__=="__main__":
    guess_the_number()

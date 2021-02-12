# This is the simple guess the number game.
# Remember to take care with indenting
import random
#Intial statements to the user
print("\nWelcome to 'Guess my number'")
print("I'm thinking of a number between 1 & 20")
#set initial values
theNumber = random.randint(1,10)
tries = 0
guess = None
#guessing loop

def ask_number():
    global tries, guess
    guess = int(input("Try to guess it -take a guess "))
    tries += 1
    if guess > theNumber :
        print("Lower...")
    if guess < theNumber :
        print("Higher..")
    return guess

while tries <= 6:
    if ask_number() == theNumber:
        break

# back outside the loop
if guess == theNumber:
    tries = str(tries)
    print("You guessed it. The number was", theNumber)
    print("and you only took ",tries,"tries")
if guess != theNumber:
    print("No, the number I was thinking of was",theNumber)
input("\n Press any key to exit")
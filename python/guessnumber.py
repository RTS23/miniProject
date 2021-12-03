import random

def genRandNumb():
    return random.randint(1,100)

def welcomeState():
    print("Welcome to Guess the Number")
    print("Please input and guess the number")

def main():
    
    welcomeState()
    guess = int(input("Guess your number: "))
    randNum = genRandNumb()
    
    while guess != randNum:
        if guess > randNum:
            print("It's too high ! Guess more | Input Q for quit")
            guess = int(input("Guess again: "))
        elif guess < randNum:
            print("It's too low ! Guess more | Input Q for quit")
            guess = int(input("Guess again: "))
        elif guess == q or Q:
            break

    print(" Congratulations !")

main()
    
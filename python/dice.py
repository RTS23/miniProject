import random

dice = [1,2,3,4,5,6]

def rollDice():
    return random.choice(dice)

def main():
    times = int(input("How much dice rolled: "))

    for time in range(1,times+1):
        print(rollDice())

main()
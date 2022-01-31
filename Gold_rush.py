

import random

boxContainer = [
    ("green box", 1000),
    ("orange box", 4000),
    ("violet box", 9000),
    ("gold box", 16000),
]
gameLength = 6
goldTotal = 0


haveBoxContainer = [True, False]


def findApproximateValue(value):
    lowestValue = value - 0.1 * value
    highestValue = value + 0.1 * value
    return random.randint(lowestValue, highestValue)


print("Welcome in the GOLD RUSH!")
print(f"You've got only {gameLength} steps, to get as much gold as possible")


while gameLength > 0:

    nextStep = int(input("Press (1) to keep going "))

    if nextStep == 1:

        box_have = random.choices(haveBoxContainer, [60, 40], k=1)

        if (True in box_have):
            what_box_have = random.choices(boxContainer, [75, 20, 4, 1], k=1)
            goldLevel = findApproximateValue(what_box_have[0][1])
            print(
                f"You found {what_box_have[0][0]}, so get {goldLevel} gold!")
            goldTotal += goldLevel

        else:
            print("You found nothing!")
        gameLength -= 1
    elif nextStep != 1:
        print("You must click (1) to keep going!")
        continue
print(f"In total you earned {goldTotal} gold!")

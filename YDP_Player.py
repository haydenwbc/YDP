from random import randint

def turn():
    keeps = []
    rolls1 = []
    for x in range(5):
        rolls1.append(randint(1,6))
    s = input(print("Type in the rolls that you want to keep, separated by a comma: ")
    keeps1 = s.split(,)
    for roll in keeps1:
        try:
            roll = int(roll)
            keeps.append(roll)
        except ValueError:
            print(f"{roll} is not a valid input.")
    rolls2 = []
    for x in range(5 - len(keeps)):
        rolls2.append(randint(1,6))
    s2 = input(print("Type in the rolls that you want to keep, separated by a comma: ")
    keeps2 = s2.split(,)
    for roll in keeps2:
        try:
            roll = int(roll)
            keeps.append(roll)
        except ValueError:
            print(f"{roll} is not a valid input.")





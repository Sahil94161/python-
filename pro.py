import random
cpu=random.randint(1,100)
player= int(input("Enetr a number b/w 1-100:-"))
while player!=cpu:
    if player>cpu:
        print("Too high")
    else:
            print(" Too low")
    player = int(input("Enetr a number b/w 1-100:-"))

else:
    print("Well done")

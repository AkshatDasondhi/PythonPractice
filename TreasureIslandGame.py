print("Welcome to the Treasure Island.")
print("Your Mission is to Find the Treasure")
print("You are at a Cross Road , Where you want to go ? Type 'left' or 'right'")
road = input()
if road == "left":
    print("You came to a lake. There is an island in the middle. Type 'wait' to wait for the boat or 'swim' to swim in lake") 
    lake = input()
    if lake == "wait":
        print("You got to the Island. There is a House with 3 Doors. One red, one Yellow and one Blue. Which one you choose?")
        room = input()
        if room == "Blue":
            print("Congrats , You found the Treasure.")
        elif room == "Red":
            print("You Lose , The room was on fire")
        else:
            print("You Lose, The room had a Monster")
    else:
        print("You Lose , Lake had Crowcodiles")
else:
    print("You Lose , it was a Dead End")

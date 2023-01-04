import random
rock = ("""
    _______

---'   ____)
      (_____)
      (_____)
      (____)

---.__(___)
""")
paper = ("""
     _______

---'    ____)____
           ______)
          _______)
         _______)

---.__________)
""")
scissor = ("""
    _______

---'   ____)____
          ______)
       __________)
      (____)

---.__(___)
""")
print("What do you choose? Type 0 for Rock , 1 for Paper and 2 for Scissors")
choose = int(input())
if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
else:
    print(scissor)
computer = random.randint(0, 2)
if computer == 0:
    print("Computer Chose : ")
    print(rock)
elif computer == 1:
    print("Computer Chose : ")
    print(paper)
else:
    print("Computer Chose : ")
    print(scissor)
if computer == choose:
    print("Its a Draw")
elif computer == 0 and choose == 1:
    print("You Win")
elif computer == 0 and choose == 2:
    print("You Lose")
elif computer == 1 and choose == 0:
    print("You Lose")
elif computer == 1 and choose == 2:
    print("You Win")
elif computer == 2 and choose == 0:
    print("You Win")
else:
    print("You Lose")


    
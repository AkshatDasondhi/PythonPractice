import random
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
diff = input("Choose a difficulty. Type 'easy' or 'hard' :  ")
attempts = 0
number = random.randint(1,101)
if diff == "easy":
    attempts = 10
else:
    attempts = 5 
print(number)
while attempts > 0: 
    print("You have %s attempts remaining to guess the number." % attempts)
    guess = int(input("Make a Guess : "))
    attempts -= 1
    if guess > number and attempts != 0:
        print("Too High. \nGuess Again")
    elif guess < number and attempts != 0:
        print("Too Low. \nGuess Again")
    elif guess == number:
        print("You Got it . The answer was %s" % number) 
if guess != number and attempts == 0:
    print("You have ran out of guesses , you Lose ")
    
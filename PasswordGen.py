# Easy : 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to PyPassword Generator.")
print("How many letters would you like in your password?")
num_of_letters = int(input())
print("How many symbols would you like?")
num_of_symbols = int(input())
print("How many numbers would you like?")
num_of_numbers = int(input())
password = ""
for i in range(1,num_of_letters+1):
    password = password + random.choice(letters)
for i in range(1,num_of_numbers+1):
    password = password + random.choice(numbers)
for i in range(1,num_of_symbols+1):
    password = password + random.choice(symbols)
print(password)
print("Here is your Password : %s" % password)

# Hard : 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to PyPassword Generator.")
print("How many letters would you like in your password?")
num_of_letters = int(input())
print("How many symbols would you like?")
num_of_symbols = int(input())
print("How many numbers would you like?")
num_of_numbers = int(input())
password = []
for i in range(1,num_of_letters+1):
    new = random.choice(letters)
    password.append(new)
for i in range(1,num_of_numbers+1):
    new2 = random.choice(numbers)
    password.append(new2)
for i in range(1,num_of_symbols+1):
    new3 = random.choice(symbols)
    password.append(new3)
print(password)
random.shuffle(password)
print(password)
newpass = ""
for i in password:
    newpass = newpass + i
print("Here is your Password : %s" % newpass)


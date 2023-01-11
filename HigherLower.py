import random
import higherlowerdata
import os
flag = 0
final_score = 0
flag2 = 0
while flag == 0:
    if flag2 == 0:
        second = random.choice(higherlowerdata.data)
        first = random.choice(higherlowerdata.data)
    elif flag2 == 1:
        first = temp
        second = random.choice(higherlowerdata.data)
    else:
        second = temp 
        first = random.choice(higherlowerdata.data)
    print("Compare A : %s , a %s , from %s" % (first['name'] , first['description'] , first['country']))
    print("Against B : %s , a %s , from %s" % (second['name'] , second['description'] , second['country']))
    ans = input("Who has more followers? Type 'A' or 'B' : ")
    A = first['follower_count']
    B = second['follower_count']
    flag2 = 0
    if A > B and ans == 'A':
        flag2 = 1
        temp = first
        final_score += 1
        os.system('cls')
        print("You're  right ! Current Score : %s" % final_score)
    elif B > A and ans == 'B':
        flag2 = 2
        temp = second
        final_score += 1
        os.system('cls')
        print("You're  right ! Current Score : %s" % final_score)
    else:
        flag = 1
        os.system('cls')
        print("Sorry , that's Wrong. Final Score : %s" % final_score)
        
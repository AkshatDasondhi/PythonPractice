import random
choice = input("Do you want to play the game of Black Jack ? Type 'y' or 'n' : ")
while choice == 'y':
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    our_cards = []
    house_cards= []
    our_cards.append(random.choice(cards))
    our_cards.append(random.choice(cards))
    house_cards.append(random.choice(cards))
    house_cards.append(random.choice(cards))
    house_sum = house_cards[0]
    our_sum = 0 
    for i in our_cards:
        our_sum = our_sum + i
    flag = "notlose"
    print("Your cards : %s , Current Score : %s" % (our_cards, our_sum))
    print("Computer's cards = %s , Computer Score : %s" % (house_cards[0] , house_sum))
    if our_sum > 21:
        print("Your score exceeded 21 , You lose.")
    choice2 = input("Type 'y' to get another card, type 'n' to pass : ")
    while choice2 == 'y':
        our_sum = 0
        our_cards.append(random.choice(cards))
        for i in our_cards:
            our_sum = our_sum + i
        print("Your cards : %s , Current Score : %s" % (our_cards, our_sum))
        print("Computer's cards = %s , Computer Score : %s" % (house_cards , house_sum))
        if our_sum > 21:
            flag = "lose"
            print("Your score exceeded 21.")
            break
        else:
            choice2 = input("Type 'y' to get another card, type 'n' to pass : ")
    if flag == "notlose":
        house_sum = 0
        while house_sum < 17:
            house_sum = 0
            for i in house_cards:
                house_sum = house_sum + i
            house_cards.append(random.choice(cards))
            house_sum = 0
            for i in house_cards:
                house_sum = house_sum + i
        print("Computer's cards = %s , Computer Sum = %s" % (house_cards,house_sum))
    house_sum = 0
    for i in house_cards:
        house_sum = house_sum + i
    if our_sum > house_sum and our_sum <= 21:
        print("You Win")
    elif our_sum == house_sum:
        print("Draw")
    else:
        print("You Lose")
    choice = 'n'


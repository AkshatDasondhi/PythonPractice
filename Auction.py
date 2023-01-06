import os
print("Welcome to the Silent Auction Program.")
name = input("What is your name ? : ")
bid = int(input("What's your bid ? : $"))
participants = {name:bid}
option = input("Are there any other bidders ? Type 'yes' or 'no'. : " )
while option == "yes":
    os.system('cls')
    name = input("What is your name ? : ")
    bid = int(input("What's your bid ? : $"))
    participants[name] = bid
    option = input("Are there any other bidders ? Type 'yes' or 'no' ." )
bids = list(participants.values())
names = list(participants.keys())
m = max(bids)
pos = bids.index(m)
print("The winner is %s with a bid of $%d" % (names[pos],max(bids)))

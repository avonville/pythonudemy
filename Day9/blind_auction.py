from blind_auction_art import logo
print(logo)

bidders = {}


def add_bid(name, bid):
    bidders[name] = bid


bidding_finished = False

while bidding_finished == False:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    add_bid(name, bid)

    another_bid = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if another_bid == "no":
        bidding_finished = True
        break

highest_bid = 0

for bidder in bidders:
    bid_amount = bidders[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}.")

from art import logo

print(logo)

bidding_finished = False
bids = {}

print("Welcome to the secret auction program")


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        big_amount = bidding_record[bidder]
        if big_amount > highest_bid:
            highest_bid = big_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)

import os
from art import logo

os.system('cls')
print(logo)
print("Welcome to the secret Auction Program.")

bidders = []

continue_bid = True

while continue_bid != False:

  bidder_name = input("What is your name?: ").title()
  bid_amount = int(input("What is your bid?: $"))
  bidders.append(
          {
          bidder_name: bid_amount
          }
      )
  
  repeat = input('Are there any other bidders? Type "yes" or "no": ')

  if repeat == "yes":
    os.system('cls')

  elif repeat == "no":
    continue_bid = False

os.system('cls')

winner_name = ""
winner_bid = 0

for name in range(len(bidders)):
  bid = name
  for price in bidders[bid]:
    if bidders[bid][price] > (bidders[bid][price] - 1):
      winner_name = bidder_name
      winner_bid += bid_amount

os.system

print(f"The winner of the auction is {winner_name} with a bid of ${winner_bid}.")

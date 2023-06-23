import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret Auction Program.")

bidder_name = input("What is your name?: ")
bid_amount = int(input("What is your bid?: $"))
bidders = []

replay = True

bidders.append(
        {
         bidder_name: bid_amount
        },
    )

repeat = input('Are there any other bidders? Type "yes" or "no": ')

while replay != False:
  if repeat == "yes":
    os.system('cls')
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    bidders.append(
          {
          bidder_name: bid_amount
          },
      )
    repeat = input('Are there any other bidders? Type "yes" or "no": ')
  elif repeat == "no":
    replay = False

os.system('cls')

winner = ""

for name in range(len(bidders)):
  bid = name
  for price in bidders[bid]:
    if bidders[bid][price] > (bidders[bid][price] - 1):
      winner = bidder_name

os.system

print(f"The winner of the auction is {winner}.")

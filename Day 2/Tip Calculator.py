print("Welcome to the Tip Calculator \n")

bill = float(input("What was the total bill ? \n$"))

tip_category = int(input("What percentage tip will you like to give? 10, 12, or 15?  \n"))

split = int(input("How many people will you like to split the bill? \n"))

tip_percentage = tip_category / 100

per_person = ((bill * tip_percentage) + bill) / split

print(f"Each person should pay: {round(per_person, 2)}")
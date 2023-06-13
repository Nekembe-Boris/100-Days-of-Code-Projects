import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")

alphabet = int(input("How many letters would you like in your password?\n"))
numeric = int(input("How many numbers would you like? \n"))
character = int(input("How many symbols would you like? \n"))

#getting the total number of times the iteration will occur
total = alphabet + numeric + character

#naming variables to assign the generated letter, number and symbol respectively
gen_letters = ""
gen_numbers = ""
gen_symbols = ""

#generating all the random characters
for n in range(0, total):
    gen_letters = random.sample(letters, alphabet)
    gen_numbers = random.sample(numbers, numeric)
    gen_symbols = random.sample(symbols, character)

#creating a list of the randomly generated items
final = gen_letters + gen_numbers + gen_symbols

#the accumulator for the password
password = ""

#randomly generating the password from the final List
for i in range(0, len(final)):
    #the assigning the randomly generated character to the generator variable
    generator = random.choice(final)
    password = generator + password


print(f"Here is your password: {password}")







# print(gen_letters)
# print(gen_numbers)
# print(gen_symbols)

# print(password)
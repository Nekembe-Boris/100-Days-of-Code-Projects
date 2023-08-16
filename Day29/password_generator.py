import random

def p_generator():
    """This function generates and returns a random password that is used when the 'Generate Password button is pressed"""
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    alphabet = random.randint(8, 10)
    numeric = random.randint(2, 4)
    character = random.randint(2, 4)

    total = alphabet + numeric + character

    gen_letters = ""
    gen_numbers = ""
    gen_symbols = ""

    for n in range(0, total):
        gen_letters = random.sample(letters, alphabet)
        gen_numbers = random.sample(numbers, numeric)
        gen_symbols = random.sample(symbols, character)


    final = gen_letters + gen_numbers + gen_symbols


    password = ""

    for i in range(0, len(final)):
        generator = random.choice(final)
        password = generator + password

    return password

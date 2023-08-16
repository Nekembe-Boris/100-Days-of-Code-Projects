import random

def p_generator():
    """This function generates and returns a random password that is used when the 'Generate Password button is pressed"""
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    alphabet = random.randint(8, 10)
    numeric = random.randint(2, 4)
    character = random.randint(2, 4)

    gen_letters = [random.choice(letters) for char in range(alphabet)]
    gen_numbers = [random.choice(numbers) for char in range(numeric)]
    gen_symbols = [random.choice(symbols) for char in range(character)]

    final = gen_letters + gen_numbers + gen_symbols

    password = "".join(final)

    return password


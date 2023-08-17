import pandas

phonetic_data = pandas.read_csv("./nato_phonetic_alphabet.csv")


for (index, row) in phonetic_data.iterrows():
    new_dict = {row.letter : row.code for (index, row) in phonetic_data.iterrows()}

valid = False

while valid != True:

    word = input("Enter a word: ").upper()

    try:
        coded_word = [new_dict[letter] for letter in word]
    except KeyError:
        print("Please enter only letters of the alphabet")
    else:
        print(coded_word)
        valid = True
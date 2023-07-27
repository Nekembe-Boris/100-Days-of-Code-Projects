import pandas

phonetic_data = pandas.read_csv("./nato_phonetic_alphabet.csv")


for (index, row) in phonetic_data.iterrows():
    new_dict = {row.letter : row.code for (index, row) in phonetic_data.iterrows()}


word = input("Enter a word: ").upper()

coded_word = [new_dict[letter] for letter in word]


print(coded_word)
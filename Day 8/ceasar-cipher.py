alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(character, code):
  cipher = 0
  new_char = ""
  for i in range(len(character)):
    letter = character[i]
    current_letter = letter

    for item_number in range(len(alphabet)):

      if current_letter == alphabet[item_number]:
        cipher = item_number + code

        if cipher > item_number:
          excess = cipher - len(alphabet)
          crypted = alphabet[excess]
          new_char += crypted
        else:
          crypted = alphabet[cipher]
          new_char += crypted      
        # if cipher > n:
        #    print(n)
        
        
  print(new_char)

ceasar(text, shift)

# cipher = 0

# for i in range(len(alphabet)):
#     if text == alphabet[i]:
#       cipher = i + shift
#     if cipher > i:
#         excess = cipher - len(alphabet)
#         crypted = alphabet[excess]
#     else:
#         crypted = alphabet[cipher]

# print(crypted)
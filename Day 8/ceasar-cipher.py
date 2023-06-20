alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(action, character, code):
  
  if action == "encode":
    cipher = 0
    new_message = ""
    for i in range(len(character)):
      letter = character[i]
      current_letter = letter

      for letter_number in range(len(alphabet)):

        if current_letter == alphabet[letter_number]:
          cipher = letter_number + code

          if cipher > letter_number:
            excess = cipher - len(alphabet)
            crypted = alphabet[excess]
            new_message += crypted
          else:
            crypted = alphabet[cipher]
            new_message += crypted      
  
    print(new_message)

  elif action == "decode":
    cipher = 0
    original_message = ""
    for i in range(len(character)):
      de_letter = character[i]
      key_letter = de_letter

      for letter_number in range(len(alphabet)):

        if key_letter == alphabet[letter_number]:
          cipher = letter_number - code
          original_message += alphabet[cipher]
            
    print(original_message)
        
  

ceasar(direction, text, shift)

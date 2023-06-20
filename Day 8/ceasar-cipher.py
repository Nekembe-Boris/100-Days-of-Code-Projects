alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(action, character, code):
  
  cipher = 0
  new_message = ""
  original_message = ""

  if action == "encode":
    
    for i in range(len(character)):
      letter = character[i]

      for letter_number in range(len(alphabet)):

        if letter == alphabet[letter_number]:
          cipher = letter_number + code

          if cipher > letter_number:
            excess = cipher - len(alphabet)
            crypted = alphabet[excess]
            new_message += crypted
          else:
            crypted = alphabet[cipher]
            new_message += crypted      
  
    print(f"The encoded text is {new_message}")

  elif action == "decode":
   
    for i in range(len(character)):
      new_letter = character[i]

      for letter_number in range(len(alphabet)):

        if new_letter == alphabet[letter_number]:
          cipher = letter_number - code
          original_message += alphabet[cipher]
            
    print(f"The original text is {original_message}")

  else:
    print("Your action does not match any function of the program")      
  

ceasar(direction, text, shift)

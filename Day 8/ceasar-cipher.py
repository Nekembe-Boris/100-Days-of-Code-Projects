from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(action, plain_text, code):
  
  cipher = 0
  new_message = ""
  original_message = ""

  if action == "encode":
    
    for letter in plain_text:  #looping through the text the user entered

      for letter_index in range(len(alphabet)): #looping through the alphabet list

        if letter == alphabet[letter_index]:
          cipher = letter_index + code

          if cipher > letter_index: #starts counting from the last item on the list to avoid range errors especially for letters at the near end of the list.
              excess = cipher - len(alphabet)
              new_message += alphabet[excess]
          else:
            new_message += alphabet[cipher]     

      if letter not in alphabet: # this line ensures that the position of non-alphabetic characters are maintained
        new_message += letter
    print(f"The encoded text is {new_message}")

  elif action == "decode":
  
    for letter in plain_text: #same function as line 12

      for letter_index in range(len(alphabet)): #same function as line 14

        if letter == alphabet[letter_index]:
          cipher = letter_index - code
          original_message += alphabet[cipher]

      if letter not in alphabet: #same funtion as line 25
        original_message += letter      
    print(f"The original text is: {original_message}")

  else:
    print("Your action does not match any function of the program")   
  

print(logo)

repeat = True

while repeat:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if shift > 37:
    shift = shift % len(alphabet)

  ceasar(direction, text, shift)

  replay = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

  if replay == "no":
    repeat = False
    print("Goodbye")

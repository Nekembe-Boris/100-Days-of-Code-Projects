logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


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
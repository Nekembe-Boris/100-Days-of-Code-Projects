with open("100-Days-of-Code-Projects\Day24\mail_merge\Input\Letters\starting_letter.txt") as data:
    letter_body = data.read()
    print(letter_body)

with open(r"100-Days-of-Code-Projects\Day24\mail_merge\Input\Names\invited_names.txt") as names:
    for lines in names:
        invited = lines.rstrip()
        invited_person = letter_body.replace('name', invited)
        with open(rf"100-Days-of-Code-Projects\Day24\mail_merge\Output\ReadyToSend\{invited}.txt", mode="w") as final_letter:
            final_letter.write(invited_person)


#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
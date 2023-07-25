with open("100-Days-of-Code-Projects\Day24\mail_merge\Input\Letters\starting_letter.txt") as data:
    letter_body = data.read()

with open(r"100-Days-of-Code-Projects\Day24\mail_merge\Input\Names\invited_names.txt") as names_list:
    for name in names_list:
        invited_person = name.rstrip()
        invitation_letter = letter_body.replace('[name]', invited_person)
        with open(rf"100-Days-of-Code-Projects\Day24\mail_merge\Output\ReadyToSend\{invited_person}.txt", mode="w") as final_letter:
            final_letter.write(invitation_letter)

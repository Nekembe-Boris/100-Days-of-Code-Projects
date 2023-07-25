with open("100-Days-of-Code-Projects\Day24\mail_merge\Input\Letters\starting_letter.txt") as data:
    letter_body = data.read()
    print(letter_body)

with open(r"100-Days-of-Code-Projects\Day24\mail_merge\Input\Names\invited_names.txt") as names_list:
    for name in names_list:
        invited = name.rstrip()
        invited_person = letter_body.replace('[name]', invited)
        with open(rf"100-Days-of-Code-Projects\Day24\mail_merge\Output\ReadyToSend\{invited}.txt", mode="w") as final_letter:
            final_letter.write(invited_person)

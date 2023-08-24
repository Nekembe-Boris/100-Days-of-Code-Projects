##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import smtplib
import random



current_date = dt.datetime.now()
MY_EMAIL = "aminaousmanu@gmail.com"
PASSWORD = "wyehocmtatsbatlm"

data = pandas.read_csv("birthdays.csv")

for (index, row) in data.iterrows():

    if row.month == current_date.month and row.day == current_date.day:

        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as file:
            print(row.names)
            letter_contents = file.read()
            letter_contents= letter_contents.replace("[NAME]", row.names)
            print(letter_contents)
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=MY_EMAIL, password=PASSWORD)
        #     connection.sendmail(
        #         from_addr=MY_EMAIL,
        #         to_addrs= row.email,
        #         msg=f"Subject:Happy Birthday\n\n{letter_contents}"
        #     )
        

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
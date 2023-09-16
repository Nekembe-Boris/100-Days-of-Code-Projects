import pandas
import datetime as dt
import smtplib
import random


current_date = dt.datetime.now()
MY_EMAIL = "aminaousmanu@gmail.com"
PASSWORD = "PASSWORD"

data = pandas.read_csv("birthdays.csv")

for (index, row) in data.iterrows():

    if row.month == current_date.month and row.day == current_date.day:

        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as file:
            letter_contents = file.read()
            letter_contents = letter_contents.replace("[NAME]", row.names)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs= row.email,
                msg=f"Subject:Happy Birthday\n\n{letter_contents}"
            )
        

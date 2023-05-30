import pandas
import random
import datetime as dt
import smtplib

MY_EMAIL = "bovina.santiago@gmail.com"
MY_PASS = "yrwmuiatwemlyigv"
PLACEHOLDER = "[NAME]"

# Datetime
now = dt.datetime.now()
today = (now.month, now.day)

bday_data = pandas.read_csv("birthdays.csv")


bday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in bday_data.iterrows()}

if today in bday_dict:

    birthday_person = bday_dict[today]
    f_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(f_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace(PLACEHOLDER, birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!\n\n{contents}")

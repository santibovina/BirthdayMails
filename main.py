import pandas
import random
import datetime as dt
import smtplib

MY_EMAIL = "your-email@your-email.com"
MY_PASS = "password"
PLACEHOLDER = "[NAME]"

# Datetime
now = dt.datetime.now()

# Tuple of month and day
today = (now.month, now.day)

# Read the csv file
bday_data = pandas.read_csv("birthdays.csv")

# Compare the data on the csv with the actual date
bday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in bday_data.iterrows()}

if today in bday_dict:

    # Select a random letter template from the folder
    birthday_person = bday_dict[today]
    f_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    # Read the file and replace the NAME PLACEHOLDER with the name that matches the birthday date with actual date
    with open(f_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace(PLACEHOLDER, birthday_person["name"])

    # Connect with the smtp service to send the birthday greeting email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!\n\n{contents}")

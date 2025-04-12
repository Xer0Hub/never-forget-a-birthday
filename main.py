##################### Extra Hard Starting Project ######################
from operator import index
from turtledemo.clock import current_day

import pandas as pd
import datetime as dt
from random import randint
import smtplib

#---------PROJECT CONSTANTS------------#
MY_EMAIL = "mike.genaric@gmail.com"
MY_PASSWORD = "gwhd dqpu jeyg engb"

#---------PROJECT VARIALBES------------#
now = dt.datetime.now()
this_month = now.month
today = now.day

birthday_letters = ["letter_templates\\letter_1.txt",
                    "letter_templates\\letter_2.txt",
                    "letter_templates\\letter_3.txt"]
opened_letters = []

for letters in birthday_letters:
    with open(letters, "r") as file:
        opened_letters.append(file.read())

#CHECK IF THERE ARE ANY BIRTHDAYS TODAY
birthdays_df = pd.read_csv("birthdays.csv")

#CHECK IF ANYONE'S BIRTHDAY IS TODAY BY ITERATING THROUGH ALL BIRTHDAYS
for _, row in birthdays_df.iterrows():
    if row['month'] == this_month and row['day'] == today:
        #CHOOSE A RANDOM LETTER TO SEND
        random_letters = opened_letters[randint(0, 2)]
        #SELECT A RANDOM LETTER TO SEND
        send_me = random_letters.replace("[NAME]", row["name"])
        birthday_person = row["email"]
        #FIRE UP SMTP TO SEND THE RANDOM LETTER
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person, msg=f"Subject: HAPPY BIRTHDAYY!!! \n\n {send_me}")
            print("Happy birthday deployed...")





"""WHAT I LEARNED:
Dictionary comprehension is often the simplest, fastest way to do things here. 
It's also a great idea with Pandas Dataframes to pull the data out of them."""


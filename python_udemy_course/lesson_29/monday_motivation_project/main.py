import smtplib
import datetime as dt
import random

EMAIL = "my_email"
PASSWORD = "my_password"
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="my_email",
                            msg=f"Subject:Friday Motivation\n\n{quote}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="email",
                            msg=f"Subject:Friday Motivation\n\n{quote}")


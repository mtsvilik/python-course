import smtplib
import datetime as dt
import random

EMAIL = "maryia.tsvilik@gmail.com"
PASSWORD = "fzkjalbvkllwdgpt"
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
                            to_addrs="mtsvilik@solvd.com",
                            msg=f"Subject:Friday Motivation\n\n{quote}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="opapina@solvd.com",
                            msg=f"Subject:Friday Motivation\n\n{quote}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="mbelyuk@solvd.com",
                            msg=f"Subject:Friday Motivation\n\n{quote}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="dmelnikova@solvd.com",
                            msg=f"Subject:Friday Motivation\n\n{quote}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="amuravskiy@solvd.com",
                            msg=f"Subject:Friday Motivation\n\n{quote}")

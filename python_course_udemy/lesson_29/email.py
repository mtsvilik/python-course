import smtplib

my_email = "my_email"
password = "my_password"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs="email",
#                     msg="Subject:Hello\n\nThis is the body of my email.")
# connection.close()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="email",
                        msg="Subject:Hello\n\nThis is the body of my email.")

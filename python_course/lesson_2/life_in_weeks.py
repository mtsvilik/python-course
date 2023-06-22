age = input("What is your current age? ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks__remaining = years_remaining * 52
months__remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks__remaining} weeks, and {months__remaining} months left."

print(message)

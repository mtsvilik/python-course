def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user("John", "Smith")
greet_user(last_name="Smith", first_name="Mary")
print("Finish")


def square(number):
    return number * number


square(3)

import random

for i in range(4):
    print(random.randint(4, 15))
    print(random.random())

members = ["John", "Mary", "Mosh", "Bob"]
choice = random.choice(members)
print(choice)


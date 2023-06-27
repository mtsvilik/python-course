numbers = [1, 2, 3]
new_list = [number for number in numbers]
print(new_list)

name = "Maryia"
new_name = [letter for letter in name]
print(new_name)

new_numbers = [number * 2 for number in range(1, 5)]
print(new_numbers)

names = ["Alex", "Den", "Peter", "Maryia", "Angela"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)

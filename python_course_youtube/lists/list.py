names = ["Mary", "Mosh", "Bob", "Sarah", "John"]
names[0] = "Maryia"
print(names)
print(names[2:])
print(names[-2])
print(names[2:4])
print(names[0])

numbers = [3, 5, 8, 10, 4, 7]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

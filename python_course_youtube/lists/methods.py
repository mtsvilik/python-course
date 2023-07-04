numbers = [3, 5, 8, 10, 4, 7, 4, 3, 10, 11]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

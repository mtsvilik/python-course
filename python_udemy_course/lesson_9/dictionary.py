dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

dict["c"] = [1, 2, 3]
print(dict)

for key in dict:
    dict[key] += 1
print(dict)

dict[1] = 4
print(dict)

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2])

print(order["main"][2][0])

print(order["main"][1][0])

import pandas

data = pandas.read_csv("squirrel_data.csv")
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
print(grey_squirrels)

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirrels_count)
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrels_count)
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")

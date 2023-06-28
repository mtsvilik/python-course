import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

avg_temp_list = sum(temp_list) / len(temp_list)
print(avg_temp_list)

avg_temp_list2 = data["temp"].mean()
print(avg_temp_list2)

max_temp_list = data["temp"].max()
print(max_temp_list)

# get data in columns

print(data["condition"])
print(data.condition)

# get data in row

print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp_F = (monday.temp * 9 / 5) + 32
print(monday_temp_F)

# create a data frame from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)

data_frame.to_csv("new_data.csv")

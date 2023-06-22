import csv

with open("weather_data.csv") as file:
    new_file = file.readlines()
    print(new_file)

with open("weather_data.csv") as data:
    new_data = csv.reader(data)
    temperatures = []
    for row in new_data:
        if row[1] != "temp":
            temperatures.append(row[1])
    print(temperatures)

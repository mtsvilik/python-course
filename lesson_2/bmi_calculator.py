height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

new_weight = int(weight)
new_height = float(height)

result = new_weight / (new_height * new_height)
print(int(result))

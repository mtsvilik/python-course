# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("/Users/solvd/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# with open("new_my_file.txt", mode="w") as file:
#     file.write("New text.")
#
with open("/text/my_file.txt", mode="a") as file:
    file.write("\nNew text.")


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Picachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table.align)
table.align = "l"
print(table)

name = input("What is your name? ")
color = input("What is your favorite color? ")
print(name + " likes " + color + " color")

birth_year = int(input("Birth year: "))
print(type(birth_year))
age = 2023 - birth_year
print(type(age))
print(age)

course = "Python for beginners"
print(course[0:4])
print(course[1:])
another_course = course[:]
print(another_course)

course = "Python for beginners"
print(course.upper())
print(course.lower())
print(course)
print(course.find("t"))
print(course.replace("beginners", "New Beginners"))



class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog = Dog()
dog.walk()

cat = Cat()
cat.be_annoying()
cat.walk()

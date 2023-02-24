class Rectangle:

    test = 1

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def printRect(self, name):
        print(f"hello {name}")
        for i in range(self.height):
            print("* " * self.width)


rect1 = Rectangle(2, 2)
rect1.printRect("world")
print(rect1.width)

rect2 = Rectangle(10, 5)
rect2.printRect("bob")

# rect2.test += 1
Rectangle.test += 1

print(rect2.test)
print(rect1.test)
print(Rectangle.test)

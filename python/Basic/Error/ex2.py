def getRemainder(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        print("you can't devide by zero")
    except:
        print("other exception occurred")


getRemainder(10, "a")


numbers = [1, 2, 3, 4, 5, 6]


def findNumber(numbers, searchNum):
    index = 0
    while True:
        num = numbers[index]
        if searchNum == num:
            return index
        index += 1


print(findNumber(numbers, 10))


def findNumber(numbers, searchNum):
    index = 0
    try:
        while True:
            num = numbers[index]
            if searchNum == num:
                return index
            index += 1
    except IndexError:
        print("index error")
    except TypeError:
        print("type error")
    except:
        print("something error")


findNumber(numbers, 10)

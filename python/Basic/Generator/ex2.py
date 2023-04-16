def myGenerator():
    for i in range(5, 30, 4):
        yield i

    return "hello"


def myGenerator2():
    x = range(5, 30, 4)
    yield from x


for i in myGenerator2():
    print(i)

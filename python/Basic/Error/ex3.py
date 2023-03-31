def getRemainder(a, b):
    try:
        return a % b
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)


getRemainder(10, "a")

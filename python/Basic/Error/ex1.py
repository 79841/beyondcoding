# # 1.
# 10 / 0

# # 2.
# ["a", "b", "c"][3]

# # 3.
# "a" + 1

# # 4.
# open("fileDoesNotExist.txt", "r")

# 5.
def getRemainder(a, b):
    if b == 0:
        print("you can't devide by zero")
    else:
        return a % b


print(getRemainder(10, "a"))


def getRemainder(a, b):
    try:
        return a % b
    except:
        print("error occurred")


print(getRemainder(10, "a"))

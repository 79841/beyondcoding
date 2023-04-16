def cg(start, end):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    startIndex = alpha.index(start)
    endIndex = alpha.index(end) + 1
    if startIndex > endIndex:
        raise IndexError("start index is larger than end index")
    yield from alpha[startIndex:endIndex]


for i in cg("z", "g"):
    print(i)

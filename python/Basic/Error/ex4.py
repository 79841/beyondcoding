def getFileContent(fileName):
    try:
        f = open(fileName, "r")
    except FileNotFoundError as e:
        print(e)
    else:
        print(f.read())
        f.close()
    finally:
        print("end")


getFileContent("test.txt")

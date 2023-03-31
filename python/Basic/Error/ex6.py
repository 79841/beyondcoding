class CustomException(Exception):
    def __init__(self):
        print("custom error occurred")


def testException():
    raise CustomException


try:
    testException()
except CustomException as e:
    print(e)

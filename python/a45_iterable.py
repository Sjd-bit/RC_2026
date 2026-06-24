from collections.abc import Iterable

class SimpleIter:
    def __init__(self, start, end):
        pass
        


def main():
    iter = SimpleIter(0, 10)
    print(isinstance(iter, Iterable))
    print(isinstance("aa", str))
    print(isinstance("aa", object))



if __name__ == "__main__":
        main()

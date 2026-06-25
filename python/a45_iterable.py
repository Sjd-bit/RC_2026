from collections.abc import Iterable

class SimpleIter:
    def __init__(self, start, end):
        pass
        

# __iter__, __next__가 이터러블의 필요충분 조건
def main():
    iter = SimpleIter(0, 10)
    print(isinstance(iter, Iterable))
    print(isinstance("aa", str))
    print(isinstance("aa", object))



if __name__ == "__main__":
        main()

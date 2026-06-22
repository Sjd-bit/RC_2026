class Add_test:
    def __add__(self, other):
        return "Add_test객체끼리 더하기 연산을 수행한다."

def main():
    print(2 ** 4)
    print(2 ** 64)
    print(18/4)
    print(type(18/4))
    print(18//3)
    print(type(18//3))
    print(18%3)
    
    a=Add_test()
    b=Add_test()
    print(a+b) 
    print(a + 123)# 연산오류는 연산이 정의가 되지 않아서 발생한다
    a = 5
    a += 1
    print(a)
    print(a)
    print(a)

if __name__ == "__main__":
    main()
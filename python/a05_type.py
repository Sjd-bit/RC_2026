def main():
    # 파이썬에는 변수 선언을 따로하지 않는다.파이썬의 모든 변수는 클래스의 객체이다.
    int_a = 123
    print(int_a, type(int_a))
    int_a = "123 숫자"
    print(int_a, type(int_a))
    int_a = 3.141592
    print(int_a, type(int_a))
    int_a = 2**3
    print(int_a, type(int_a))

if __name__ == "__main__":
    main()
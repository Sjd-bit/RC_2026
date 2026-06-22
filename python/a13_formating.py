def main():
    string = "abc"
    string2 = "this is format test: {}".format(10)
    print(string)
    print(string2)

    string3 = "this is format test: {2} {1} {0}".format(10, 20, 30)
    print(string3)
    string4 = "this is format test: {2:d} {1:5d} {0:05d}".format(-10, -20, -30)
    print(string4)#d는 정수형태로 표현해라

    string5 = "this is format test: {2:+.2f} {1:+5.2f} {0:+05.2f}".format(10.1263, -20.4213, -30)    
    print(string5)#f는 실수형태로 표현해라
#포멧은 가시성이 떨어져서 잘 안쓰인다. f-string을 쓰는게 좋다.
    string6 = 10.216
    print(f"this is format test: {string6:10.2f}")
    print(f"this is format test: {22.19:10.2f}")

if __name__ == "__main__":
    main()
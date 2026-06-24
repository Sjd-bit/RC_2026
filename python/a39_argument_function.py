def call_10(func):
    for _ in range(10):
        func()

def print_hello():
    print("hello!")


def main():
    temp_f = print_hello   #함수도 클래스의 객체이다
    print(type(print_hello))
    call_10(print_hello)
    call_10(temp_f)

if __name__ == "__main__":
        main()
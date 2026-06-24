def simpple_wrapper(func):
    def wrapper():
        print("함수 실행 전 코드")
        func()
        print("함수 실행 완료 코드")
    return wrapper

@simpple_wrapper
def print_hello():
    print("실행됨")


def main():
    # wrapper = simpple_wrapper(print_hello)
    # wrapper()
    print_hello()

if __name__ == "__main__":
        main()

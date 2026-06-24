from functools import wraps

def simpple_wrapper(value)""
    def simpple_wrapper_inner(func):
        @wraps(func)
        def wrapper(*args, **kargs):
            print("함수 실행 전 코드")
            result = func(*args, **kargs)
            print("함수 실행 완료 코드")
            return result
    return wrapper
return simpple_wrapper_inner

@simpple_wrapper
def print_hello(n, v):
    for _ in range(n): 
        print(v)


def main():
    # wrapper = simpple_wrapper(print_hello)
    # wrapper()
    print_hello()

if __name__ == "__main__":
        main()

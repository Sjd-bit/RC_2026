from functools import lru_cache

def rec_fac(n):
    if n == 1:   #추천하지 않는다.
        return 1
    else:
        return n * rec_fac(n-1)



def for_fac(n):
    output = 1
    for i in range(n):
        output *= i+1
    return output     

cnt = 0
dic_cnt = 0
dictionary = {1: 1, 2: 1}


def fibonacci_memory(n):
    global cnt, dic_cnt
    cnt += 1
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci_memory(n-1) + fibonacci_memory(n-2)
        dictionary[n] = output
        dic_cnt += 1
        return output

@lru_cache(maximize=none)
def fibonacci(n):
    if n == 1:
         return 1
    elif n == 2:
         return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    print(rec_fac(30))
    print(for_fac(30))
    print(fibonacci(29))
    print(f"fibonacci 함수가 실행된 횟수: {cnt},{dic_cnt}")

if __name__ == "__main__":
        main()
def print_n_times(value, n=2, v=3, g=5, *sum):
    sum_=0
    for i in range(n):
        print(value)
    for i in sum:
        sum_ += 1
    return sum_



def main():
    print(print_n_times("hello", n=10, v=123, g=235453))
#positional, default, 가변인자 순으로
#가변인자가 없으면 default 인자 or keyward 인자



if __name__ == "__main__":
        main()
def print_n_times(n, *args, abc="abc", defg="defg", **keyargs):
    #순서대로 포지셔널, 디폴트, variable-length, keyward, variable-length-keyword
    for i in range(n):
        print(args)
    print(abc, defg)
    print(type(keyargs),keyargs)

    for k, v in keyargs.items():
         print(k, v)
def general_f(*args, **keyargs):
    pass


def main():

    print_n_times(3, "seo", "jeong", "dae", "is", "student")
    print_n_times(3, "test", defg="마지막 문자", abc="첫 문자",a=1,b="two")
    general_f(1, 2, 4, k="234")



if __name__ == "__main__":
        main()
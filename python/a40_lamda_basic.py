def power(item):
    return item * item

def under_3(item):
    return item < 3



def main():
    li = [1,2,3,4,5]
    output_map = map(power, li)
    print(list(output_map))
    output_map = map(lambda x : x * x, li)
    output_under_3 = filter(under_3, li)
    print(list(output_map))

if __name__ == "__main__":
        main()
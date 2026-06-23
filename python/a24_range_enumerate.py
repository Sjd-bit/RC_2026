def main():

    print(range(10)) #range는 0부터 9까지의 정수 시퀀스를 생성
    print(range(0,10,1))
    a = range(10)
    print(list(a))
    print(list(range(5,10,3)))
    a = []
    for i in range(0,100,2):
         a.append(i+1)
    print(a)
    list_b = ["a","b","c","d","e","f"]
    for a, ele in enumerate(list_b):
        print(ele+"원소", a)
    #list comprehension
    c = [i+1 for i in range(0,100,2)]
    print(c)

    list_c = ["에이","비","씨","디","이","에프"]
    for i in range(6):
        print(list_b[i], list_c[i])
    for b, c in zip(list_b, list_c): #pyhonic, pydantic
        print(b, c)



if __name__ == "__main__":
        main()
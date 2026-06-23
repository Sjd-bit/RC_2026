import datetime

def main():
#파이썬 리스트(배열) 선언 크기와 타입 상관없음
    list_a = []
    list_b = list()
    print(type(list_a))
    print(type(list_b))
    ptime = datetime.datetime.now()
    list_c = [1,2,3.3,"seo",ptime,True]
    print(list_c[3])
    print(list_c[2])
    list_c[5]=False
    print(list_c[5])

    list_d = [[1,2,3],[4,5,6],[7,8,9]]
    print(list_d[1][2])
    print(list_d[0][1])
    #len(length)함수로 리스트 길이 확인 
    print(len(list_d))
#리스트의 연산 곱하기는 n번 123*2 = 123123 더하기는 순서대로 123 + 123 = 123123
#list_n.extend([123])= 리스트n에 123더하기


if __name__ == "__main__":
        main()
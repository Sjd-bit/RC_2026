def main():
    tu= tuple()
    print(tu, type(tu))
    tu = (1,2) #원소 추가, 제거 및 변경이 불가
    print(tu,type(tu))
    print(tu[0])
    for ele in tu:
          print(ele)# list와 같은 기능을 가진 컨테이너
          #시스템 내부적으로 안전하게 데이터를 전달하기 위해서 사용
    tu_1 = 1,2
    print(tu_1,type(tu_1))
    a = 1
    b = 2
    #swap C스타일
    tmp = a
    a = b
    b = tmp
    print(a, b)
    # swap 파이썬 스타일
    a, b = b, a
    print(a, b)


if __name__ == "__main__":
        main()
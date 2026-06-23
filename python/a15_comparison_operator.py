def main():
    print(10 == 100)  #False
    print(10 != 100)  #True
    print(10 < 100)   #True
    print(100 >= 100) #True
    print(type(True)) #<class 'bool'>

    print(not True)   #False      
    print(not False)  #True
    print(True and True) #True
    print(False or False) #False
    
    a = int(input("정수 입력: "))

    if a > 100:
        print("100보다 큰 수를 입력하셨습니다.")
    print("프로그램을 종료합니다.")
#! && ||

if __name__ == "__main__":
    main()
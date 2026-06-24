import math
import sys

def main():
    input_a = input("정수 입력: ")
    try:
        number_input = int(input_a)
    except ValueError as e:
    #except Exception as e:
        print(e)
        sys.exit()
    else:
        print(f"원의 반지름: {number_input}")
        print(f"원의 둘레: {number_input*2*math.pi}")
        print(f"원의 넓이: {number_input**2*math.pi}")    
    finally:
        print("-----프로그램이 종료되었습니다-----") 
         

if __name__ == "__main__":
        main()

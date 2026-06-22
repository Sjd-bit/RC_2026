def main():

    input_Q = input("숫자를 입력하세요: ")
    print(type(input_Q), input_Q)
    # try:
    #     print(int(input_var) + 100)
    # except ValueError:
    #     print("입력한 값이 숫자가 아닙니다.")
    if input_Q.isdigit():
        print(int(input_Q) + 100)
    else:
        print("입력한 값이 숫자가 아닙니다.")



        
if __name__ == "__main__":
    main()
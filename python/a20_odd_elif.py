def main():
    number = int(input("정수 입력: "))
    if number % 2:
        print(f"{number}은/는 홀수입니다.")
    else:
        print(f"{number}은/는 짝수입니다.")
    print(f"{number}은/는 " "홀수" if number % 2 else "짝수",sep="","입니다.")

if __name__ == "__main__":
        main()
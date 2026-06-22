def main():
    input A = input("상품 정보를 입력하세요.(이름, 가격)")
    print(type(input_A), input_A)
    print("상품 정보:", input_A)

# 1. 상품 이름과 가격 입력 받기
product_name = input("상품 이름을 입력하세요: ")
original_price = int(input("상품 가격을 입력하세요(숫자만): "))

# 2. 할인율 설정 및 할인된 가격 계산
discount_rate = 0.20  # 20% 할인
discounted_price = int(original_price * (1 - discount_rate))

# 3. 결과 출력
print("\n" + "="*30)
print(f"🛍️  [할인 결과] {product_name}")
print(f"▪️ 정상 가격: {original_price:,}원")
print(f"▪️ 할인 가격 (20% OFF): {discounted_price:,}원")
print("="*30)

if __name__ == "__main__":
    main()
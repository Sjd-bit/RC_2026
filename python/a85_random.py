import random


def main():
    hangeul = list("김이박최우임서심정장")
    hangeul2 = list("정상대종보성제동관열우준혁재순원호준세윤하태")
    for _ in range(100):
        name = random.choice(hangeul) + str().join(random.choices(hangeul2, k=2))
        print(name)

    
if __name__ == "__main__":
        main()


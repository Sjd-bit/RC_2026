import pickle
import random
from pathlib import Path



def main():
    li = [random.randint(0, 100) for _ in range(1000)]
    pickle_path = Path(__file__).parent / "random_list.pickle"
    with pickle_path.open("wb") as f: # as f 는 이후 이 파일을 f로 부르겠다는 뜻
         # 피클은 이진 데이터로 저장하기 때문에 바이너리b를 넣어야 함
        pickle.dump(li, f)
    print("pickle file is generated")



if __name__ == "__main__":
        main()

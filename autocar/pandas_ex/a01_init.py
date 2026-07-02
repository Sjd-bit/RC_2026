import pandas as pd
import numpy as np

def main():
    arr = np.array([1, 2, 3, 4], dtype=np.int8)
    sr = pd.Series(arr)
    print(sr, type(sr))
    sr[1] = 100
    print(sr[1])
    
    value = [32, 68, 220, 72]
    index = ["온도", "습도", "강수량", "불쾌지수"]
    sr = pd.Series(value, index=index)

    print(type(sr))
    print(sr)
    print(sr["온도"])

if __name__ == "__main__":
    main()

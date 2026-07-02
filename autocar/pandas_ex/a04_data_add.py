import pandas as pd
import numpy as np

def main():
    value = [[32, 68, 220, 72],
            [28, 30, 0, 12],
            [38, 81, 0, 91]]
    columns = ["온도", "습도", "강수량", "불쾌지수"]
    index = ["초여름", "늦봄", "한여름"]
    df = pd.DataFrame(value, index=index, columns=columns, dtype=np.uint8)

    index2 = ["한여름"]
    value2 = [[36, 100, 0, 1000]]
    df2 = pd.DataFrame(value2, index=index2, columns=columns)
    print(pd.concat([df, df2], axis=0))
    df.insert(0, "체감온도", [30, 28, 35])
    print(df)
    
if __name__ == "__main__":
    main()

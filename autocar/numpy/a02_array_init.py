import numpy as np


def main():
    arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int8)
    print(arr.ndim, arr.shape)
    arr = np.arange(5)
    print(arr)
    arr = np.arange(5,30,10)
    print(arr)


    
    arr = np.zeros(5)
    print(type(arr), arr)
    

if __name__ == "__main__":
    main()

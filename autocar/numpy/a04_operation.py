import numpy as np

def main():

    x = np.arange(40).reshape(8, 5)
    print(x)
    y = np.arange(39,-1,-1).reshape(8, 5)
    print(y)

    z = np.linspace(30, 100, 40).reshape(8, 5)
    print(z)
    s1 = x + y
    print(s1)
    s2 = x - z
    print(s2)
    s3 = x / z
    print(s3)
    s4 = x @ y.T
    print(s4)

    x = x + 10
    print(x)
    x = x + np.array([1, 2, 3, 4, 5])
    print(x)

    s5 = np.matmul(x, y.T)
    print(s5)
    s6 = np.dot(x, y.T)
    print(s6)

    A = np.array([[1, 2], [3, 4]])
    inv_A = np.linalg.inv(A)
    print(A, inv_A)
    print(A @ inv_A)

    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = np.array([30, 20, 10])
#    result = np.linalg.solve(A, B)
    A_inv = np.linalg.inv(A)
    result = A_inv @ B
    x, y, z = result
    print(f"x={x}, y={y}, z={z}")

if __name__ == "__main__":
    main()


import numpy as np

x = np.random.random(20)
print(x)
y = np.random.random(20)
print(y)
np.savez("randoms", arr1=x, arr2=y)
z=np.load("randoms.npz")
print(z["arr1"])
print(z["arr2"])
z.close()


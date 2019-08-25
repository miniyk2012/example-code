import os
from time import perf_counter as pc
import numpy as np
a = np.arange(12)
print(a)
print(a.shape)
a.shape = 3, 4
print(a)
print(a.transpose())
print()
floats = np.arange(10**7)
print(floats.dtype)
floats = np.float64(floats)
print(floats.shape)
print(floats[-3:])
print(floats.dtype)
t0 = pc()
floats /= 3
print(floats[-3:])
print(pc()-t0)

np.save('floats-10M', floats)
floats2 = np.load('floats-10M.npy', 'r+')
floats2 *= 5  # 'r+' 模式也会对实际文件内容做修改哟, 因为它做的是memroy-mapping
print(floats2[-3:])

floats3 = np.load('floats-10M.npy', 'r')
print(floats3[-3:])

os.remove('floats-10M.npy')

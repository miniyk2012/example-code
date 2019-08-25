import os
from array import array
from random import random

floats = array('d', (random() for i in range(10 ** 5)))
print(floats[-1])

with open('floats.bin', 'wb') as fb:
    floats.tofile(fb)

floats2 = array('d')
with open('floats.bin', 'rb') as fb:
    floats2.fromfile(fb, len(floats))
os.remove('floats.bin')

print(len(floats2))
print(floats2[-1])

print(floats.typecode)

print(floats == floats2)

floats = array(floats.typecode, sorted(floats))
print(floats[:10])

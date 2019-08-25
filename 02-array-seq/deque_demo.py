from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
print(dq[0])

dq.rotate(-4)
print(dq)

dq.appendleft(-1)
print(dq)

dq.extend([11, 22, 33])
print(dq)

dq.extendleft([10, 20, 30, 40])
print(dq)

print(len(dq))

del dq[5]
print(dq)

l = list(dq)
print(l)
print(deque(l))
print(deque(dq))
print(dq)
print(bytearray('杨', 'utf8'))
print(bytearray([97, 98]))

cafe = bytes('caf额', encoding='utf8')
print(cafe)
print(cafe[0])
print(cafe[:1])

cafe_arr = bytearray('caf额', encoding='utf8')
print(cafe_arr)
print(cafe_arr[0])
print(cafe_arr[:1])
print(len(cafe_arr))
cafe_arr[0] = ord('x')
print(cafe_arr)
cafe_arr[-3:] = '杨'.encode('utf8')
print(cafe_arr.decode())

import array

numbers = array.array('h', [-2, 2])
octets = bytes(numbers)
print(octets)

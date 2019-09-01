from collections.abc import Mapping, MutableMapping

my_dict = {}
print(isinstance(my_dict, Mapping))
print(isinstance(my_dict, MutableMapping))
print(isinstance(my_dict, dict))

print(hash((1, 2, frozenset([34, 50]))))

my_dict.update([(1, 2)], a=10)
print(my_dict)


a = my_dict.items()  # items()是视图, 会跟踪源对象的状态
print(a)
my_dict['x'] = 'y'
print(a)

# 不可变映射类型，可以认为是与frozenset相对应的不可变dict
from types import MappingProxyType
d_proxy = MappingProxyType(my_dict)
print(d_proxy)
my_dict.update(xx=1000)
print(d_proxy)
try:
    d_proxy['x'] = 101
except TypeError as e:
    assert e.args[0] == "'mappingproxy' object does not support item assignment"


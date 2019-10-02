from unicodedata import name
from pyuca import Collator

c = Collator()

assert sorted(["杨", "恺", "啊"]) == ["啊", "恺", "杨"]
assert sorted(["杨", "恺", "啊"], key=c.sort_key) == ["啊", "恺", "杨"]
assert sorted(["cafe", "caff", "café"]) == ["cafe", "caff", "café"]
assert sorted(["cafe", "caff", "café"], key=c.sort_key) == [
    "cafe", "café", "caff"]

print(name('杨'))
print('杨'.encode())
print("cafe\u0301")
print(hex(ord('杨')))  # 0x6768
print(chr(0x6768))

assert u'\u6768' == '杨'
assert u'\u6768' == '\u6768'
assert type(u'\u6768') == str

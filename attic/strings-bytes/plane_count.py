import sys
from unicodedata import name, normalize

averager_total_count = 0
bmp_count = 0

for i in range(sys.maxunicode):
    char = chr(i)
    char_name = name(char, None)
    if char_name is None:
        continue
    averager_total_count += 1
    if i <= 0xffff:
        bmp_count += 1

print(averager_total_count, bmp_count, bmp_count / averager_total_count, bmp_count / averager_total_count * 100)

# BEGIN RE_DEMO
import re

re_numbers_str = re.compile(r'\d+')     # <1>
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')  # <2>
re_words_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"  # <3>
            " as 1729 = 1³ + 12³ = 9³ + 10³.")        # <4>

text_bytes = text_str.encode('utf_8')  # <5>

print('Text', repr(text_str), sep='\n  ')
print('Str', text_str, sep='\n  ')
print('Numbers')
print('  str  :', re_numbers_str.findall(text_str))      # <6>
print('  bytes:', re_numbers_bytes.findall(text_bytes))  # <7>
print('Words')
print('  str  :', re_words_str.findall(text_str))        # <8>
print('  bytes:', re_words_bytes.findall(text_bytes))    # <9>


text_chinese_str = ("杨恺a 12尼玛")
text_chinese_bytes = text_chinese_str.encode('utf_8')
print("中文")
print('  str  :', re_words_str.findall(text_chinese_str))        # <8>
print('  bytes:', re_words_bytes.findall(text_chinese_bytes))    # <9>
# END RE_DEMO
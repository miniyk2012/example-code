invoice = """
牛奶  100元
香蕉  200元
"""

FRUIT = slice(0, 2)
PRICE = slice(4, None)
for item in invoice.split('\n')[1:-1]:
    print(item[FRUIT], '的价格是', item[PRICE])
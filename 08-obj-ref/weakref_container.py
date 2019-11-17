class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


import weakref

stock = weakref.WeakValueDictionary()
catalog = [Cheese('yangkai'), Cheese('yangchen')]

for cheese in catalog:
    stock[cheese.kind] = cheese

print(stock)
print(sorted(stock.keys()))

del catalog

print(stock)
print(sorted(stock.keys()))

del cheese
print(sorted(stock.keys()))
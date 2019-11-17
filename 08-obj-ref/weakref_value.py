import weakref
from pprint import pprint

import gc


# gc.set_debug(gc.DEBUG_LEAK)


class Man(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Man name=%s>' % self.name

    def __del__(self):
        print("deleting %s" % self)


def demo(cache_factory):
    all_refs = {}
    print("cache type:", cache_factory)
    cache = cache_factory()
    for name in ["Jim", 'Tom', 'Green']:
        man = Man(name)
        cache[name] = man
        all_refs[name] = man
        del man
    print("all_refs=", )
    pprint(all_refs)
    print("before, cache contains:", list(cache.keys()))
    for name, value in cache.items():
        print("%s = %s" % (name, value))
    print("\ncleanup")
    del all_refs
    del value  # 存着Man('Green')
    gc.collect()

    print("after, cache contains:", list(cache.keys()))
    for name, value in cache.items():
        print("%s = %s" % (name, value))
    print("demo returning")
    return


demo(dict)
print()

demo(weakref.WeakValueDictionary)

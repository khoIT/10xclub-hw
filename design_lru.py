db = {}

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LRU(object):
    def __init__(self, size, db):
        self.db = db
        self.store = {} # keys are node in a doubly linked-list, value is string
        self.orderedKeys = []
        self.size = size

    def reshuffle_key(self, key):
        idx = 0
        while idx < len(self.orderedKeys):
            if self.orderedKeys[idx] == key:
                del self.orderedKeys[idx]
            idx += 1
        self.orderedKeys.insert(0, key)


    def get_key(self, key):
        if key in self.store:
            self.reshuffle_key(key)
            return self.store.get(key)
        else:
            value = self.db.get(key)
            self.set_key(key, value)
            return value


    def set_key(self, key, value):
        self.store[key] = value
        self.reshuffle_key(key)

        # delete oldest key
        if len(self.orderedKeys) > self.size:
            removedKey = self.orderedKeys[-1]
            del self.orderedKeys[-1]
            self.store.pop(removedKey)


lru = LRU(10, {})
lru.orderedKeys = [1,2,3]
lru.reshuffle_key(2)
print(lru.orderedKeys == [2,1,3])


lru = LRU(3, {0: '0'})
lru.set_key(1, '1')
lru.set_key(2, '2')
lru.set_key(3, '3')
print lru.store
print lru.orderedKeys

lru.set_key(4, '4')
print lru.store
print lru.orderedKeys

# get key in dict
print lru.get_key(2), type(lru.get_key(2))
print lru.orderedKeys

# get key not in dict
print lru.get_key(0)
print lru.orderedKeys

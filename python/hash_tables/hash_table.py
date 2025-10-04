class HashTable:

    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash = 0
        for i, char in enumerate(key):
            hash = (hash + ord(char) * i) % len(self.data)

        return hash

    def set(self, key, value):
        address = self._hash(key)
        self.data[address] = [key, value]

    def get(self, key):
        address = self._hash(key)

        if self.data[address]:
            return self.data[address][1]
        else:
            return None

    def keys(self):

        keys = []

        for item in self.data:
            if item:
                keys.append(item[0])
            else:
                continue

        return keys

    def values(self):

        values = []

        for item in self.data:
            if item:
                values.append(item[1])
            else:
                continue

        return values


my_hash_table = HashTable(50)
my_hash_table.set('grapes', 10000)
print(my_hash_table.get('grapes'))
my_hash_table.set('apples', 9)
my_hash_table.set('oranges', 100)
print(my_hash_table.get('apples'))
print(my_hash_table.data)
print(my_hash_table.keys())
print(my_hash_table.values())

'''
// JavaScript Implementation:

class HashTable {
  constructor(size){
    this.data = new Array(size);
  }

  _hash(key) {
    let hash = 0;
    for (let i =0; i < key.length; i++){
        hash = (hash + key.charCodeAt(i) * i) % this.data.length
    }
    return hash;
  }
}

const my_hash_table = new HashTable(50);
my_hash_table.set('grapes', 10000)
my_hash_table.get('grapes')
my_hash_table.set('apples', 9)
my_hash_table.get('apples')
'''

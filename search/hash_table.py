from random import randint


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Double Hashing
    def custom_hash(self, key):
        return (key) % self.size

    def second_hash(self, key):
        return 1 + (key) % self.size - 1

    def insert(self, key, value):
        value_1 = self.custom_hash(key)
        value_2 = self.second_hash(key)

        i = 0
        while self.table[(value_1 + i * value_2) % self.size] is not None:
            i += 1
        self.table[(value_1 + i * value_2) % self.size] = (key, value)

    def search(self, key):
        value_1 = self.custom_hash(key)
        value_2 = self.second_hash(key)

        i = 0
        while self.table[(value_1 + i * value_2) % self.size] is not None:
            if self.table[(value_1 + i * value_2) % self.size][0] == key:
                return self.table[(value_1 + i * value_2) % self.size][1]

            i += 1

        return None

    def delete(self, key):

        value_1 = self.custom_hash(key)
        value_2 = self.second_hash(key)

        i = 0
        while self.table[(value_1 + i * value_2) % self.size] is not None:
            if self.table[(value_1 + i * value_2) % self.size][0] == key:
                self.table[(value_1 + i * value_2) % self.size] = None
                return True

            i += 1

        return False


hash_table = HashTable(100)


for i in range(hash_table.size):
    hash_table.insert(i, randint(0, 10000))

for j in range(1, 20):
    print(hash_table.search(j))

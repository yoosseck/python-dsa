class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        last = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last

    def insert(self, index, inserted):
        self._shift_items_right(index, inserted)
        return inserted

    def delete(self, index):
        deleted = self.data[index]
        self._shift_items_left(index)
        return deleted

    # You've got to shift items to left/right upon delete/insert: O(n)
    def _shift_items_left(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1

    def _shift_items_right(self, index, item):
        last = self.data[self.length - 1]
        for i in range(index, self.length):
            self.data[i+1] = self.data[i]
        self.data[index] = item
        self.length += 1
        self.data[self.length - 1] = last


if __name__ == '__main__':
    new_array = MyArray()
    new_array.push('Japan')
    print(new_array.push('UK'))
    print(new_array.push('US'))
    print(new_array.push('China'))
    print(new_array.push('Korea'))
    print(new_array.push('France'))

    print(new_array.data)

    print(new_array.insert(4, 'Germany'))
    print(new_array.data)
    print(new_array.length)

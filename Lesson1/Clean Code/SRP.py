#### Bad
class MyArray:
    def __init__(self):
        self._array = []
    
    def add(self, item):
        self._array.append(item)
        print(self._array)

arr = MyArray()
arr.add(1)
arr.add(2)

#### Better
class SRPArray:
    def __init__(self):
        self._array = []

    def add(self, item):
        self._array.append(item)
    
    def print_array(self):
        print(self._array)

arr = SRPArray()
arr.add(1)
arr.add(2)
arr.print_array()
arr.add(3)
arr.print_array()
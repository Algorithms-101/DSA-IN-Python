# Binary Heap in Python using Lists.

class BinaryHeap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

newBinaryHeap = BinaryHeap(5)

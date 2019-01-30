"""
Create stack operations from heap
- create min heap with element = (order, value) pairs
- order starts from 0 and keep on decrementing
- top of heap is min order value i.e. last element of list
"""
import heapq
class StackFromHeap:
    def __init__(self):
        self._minHeap = []
        self._order = 0

    def stack_from_heap(self, list):
        for i in range(len(list)):
            heapq.heappush(self._minHeap, (self._order, list[i]))
            self._order -= 1

    def push(self, data):
        heapq.heappush(self._minHeap, (self._order, data))
        self._order -= 1

    def pop(self):
        last_input = heapq.heappop(self._minHeap)
        return last_input[1]

def test():
    list = [10, 1, 3, 5, 20]
    obj = StackFromHeap()
    obj.stack_from_heap(list)
    print(str(obj._minHeap[0 : len(obj._minHeap)]))
    print(str(obj.pop()))
    print(str(obj._minHeap[0 : len(obj._minHeap)]))
    print(str(obj.pop()))
    print(str(obj._minHeap[0 : len(obj._minHeap)]))
    obj.push(25)
    print(str(obj._minHeap[0 : len(obj._minHeap)]))
    print(str(obj.pop()))
    print(str(obj.pop()))
    print(str(obj.pop()))
    print(str(obj._minHeap[0 : len(obj._minHeap)]))

if __name__ == '__main__':
    test()

'''
Caclulate Running median in array of numbers
package heapq = for min heap implementation
class MaxHeap for max heap implementation
'''
import heapq
from MaxHeap import MaxHeap

class RunningMedian:
    def __init__(self):
        self._minHeap = []
        self._maxHeap = MaxHeap()

    def getRunningMedian(self, list):
        for i in range(len(list)):
            # if incoming value is greater than top of max heap then push it into min heap
            if len(self._maxHeap._heap) != 0 and list[i] > self._maxHeap.peek() :
                heapq.heappush(self._minHeap, list[i])
            else :
                self._maxHeap.push(list[i])

            # if len(maxHeap) > len(minHeap)+1 or vice versa then take out el from bigger heap and push other
            if len(self._minHeap) > len(self._maxHeap._heap) + 1 :
                self._maxHeap.push(self._minHeap[0])
                heapq.heappop(self._minHeap)
            elif len(self._maxHeap._heap) > len(self._minHeap) + 1 :
                heapq.heappush(self._minHeap, self._maxHeap.peek())
                self._maxHeap.pop()

            print("maxHeap " + str( self._maxHeap._heap[0:len(self._maxHeap._heap)] ))
            print("minHeap " + str( self._minHeap[0:len(self._minHeap)] ))
            print("\n")

        if(len(self._maxHeap._heap) == len(self._minHeap)) :
            return 0.5 * (self._maxHeap.peek() + self._minHeap[0])
        else :
            if(self._maxHeap.peek() > self._minHeap[0]) :
                return self._maxHeap.peek()
            else :
                return self._minHeap[0]

def test():
    list = [100, 1, 2, 3, 400, 5, 1000, 20, 30, 100]
    object = RunningMedian()
    print (object.getRunningMedian(list))

if __name__ == '__main__':
    test()

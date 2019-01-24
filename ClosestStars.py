'''
Given array of number = distance of stars from earth , find closest k stars
'''
import heapq
class MaxHeap:
    def __init__(self, items = []):
        self._heap = []
        for i in items:
            self._heap.append(i)
            self.__floatUp(len(self._heap)-1)

    # push adds element to last index of array heap
    def push(self, data):
        self._heap.append(data)
        self.__floatUp(len(self._heap)-1)

    def peek(self):
        if len(self._heap) != 0:
            return self._heap[0]
        return False

    def pop(self):
        if len(self._heap) > 1:
            self.__swap(0, len(self._heap)-1)
            max = self._heap.pop()
            self.__bubbleDown(0)
        elif len(self._heap) == 1:
            max = self._heap.pop()
        else:
            max = False
        return max

    def __swap(self, i , j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def __floatUp(self, index):
        if index  == 0:
            return
        # get parent of heap[index]
        parent = (int)((index-1)/2)
        if self._heap[parent] < self._heap[index]:
            # swap elements at index and parent
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = 2*index+1
        right = 2*index+2
        largest = index
        if len(self._heap) > left and self._heap[largest] < self._heap[left]:
            largest = left
        if len(self._heap) > right and self._heap[largest] < self._heap[right]:
            largest = right
        if largest != index:
            self.__swap(largest, index)
            self.__bubbleDown(largest)


class ClosestStars():
    def __init__(self):
        # by default stores elements in increasing order
        self._maxHeap = MaxHeap()

    def closest_stars_from_earth(self, dist, k):
        # store first k closest stars
        [self._maxHeap.push(dist[i]) for i in range(k)]
        # print(str(self._maxHeap._heap[0:len(self._maxHeap._heap)]))

        for i in range(k, len(dist)):
            # if ith star distance from earth is less than star at top of maxHeap (which is farthest star)
            # delete max from maxHeap and add ith star
            if dist[i] < self._maxHeap._heap[0]:
                self._maxHeap.pop()
                self._maxHeap.push(dist[i])

        print(str(self._maxHeap._heap[0:len(self._maxHeap._heap)]))

def test():
    # distance of stars from earth
    dist = [199,31,590,100,13,20,0,1,1,3010,40,11,500,501]
    obj = ClosestStars()
    obj.closest_stars_from_earth(dist, 10)

if __name__ == '__main__':
    test()

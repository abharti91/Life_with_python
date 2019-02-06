'''
Seach minimum in cyclic sorted array
Complexity analysis
    - if there are no duplicate elements = O(logN)
    - if there are duplicates, there is no better algorithm to solve better than O(N)
'''

class MinInCyclicSorted:
    def searchMin(self, A, l, r):
        print("A[" + str(l) + "," + str(r) + "]=[" + str(A[l]) + "," + str(A[r]) + "]" )
        if l == r :
            return l
        if l < r:
            m = (int)(l + (r-l)/2)
            if A[m] > A[r] :
                return self.searchMin(A, m+1, r)
            elif A[m] < A[r] :
                return self.searchMin(A, l, m)
            else: #A[m]==A[r], then min can be on left or right ex. 1,1,1,1,0,1,1
                # this iteration runs on both left and right hence causing O(N) complexity
                x = self.searchMin(A, l, m)
                y = self.searchMin(A, m+1, r)
                if A[x] > A[y] :
                    return y
                else :
                    return x

def test():
    data = [1, 1, 1, 1, 1, 1, 0, 0, 0, 1]
    o = MinInCyclicSorted()
    print(o.searchMin(data, 0, len(data)-1))

if __name__ == '__main__':
    test()

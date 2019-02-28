
class BinarySearch:
    def __init__(self) :
        self.A = []

    # find position of element k in sorted array whose length is not known in advance
    # we will do binary search to get end of list with pow(2,p)-1
    def binary_search_unknown_len(self, A, k) :

        if len(A) == 0 :
            return -1

        # if first element of A is larger than k, return -1
        if (A[0] > k) :
            return -1

        p = 0
        while (1) :
            try:
                val = A[(1 << p) - 1]
                if (val == k) :
                    return (1 << p) - 1;
                elif (val > k):
                    break
            except Exception, e:
                break
            p = p + 1

        low = (1 << (p-1)) + 1
        high = (1 << p) - 2
        while (low <= high) :
            mid = low + ((high - low) >> 1)
            if (A[mid] == k) :
                return mid
            elif (A[mid] > k) :
                high = mid-1
            else :
                low  = mid+1
        
        print("not able to find " + str(k))
        return -1

def test() :
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    o = BinarySearch()
    x = 11
    print("index of element " + str(x) + " is " + str(o.binary_search_unknown_len(A, x)))

if __name__ == '__main__' :
    test()
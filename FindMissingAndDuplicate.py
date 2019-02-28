class FindMissingAndDuplicate :
    def __init__(self):
        self.list = []

    def find(self, list):
        miss_XOR_dup = 0
        
        # get XOR of list and Zn (1 to n)
        for i in range(len(list)) :
            miss_XOR_dup ^= i ^ list[i]

        miss_or_dup = 0

        # get a bit differs in m and t
        differ_bit = miss_XOR_dup & (~(miss_XOR_dup - 1))

        # when we do xor of this bit with all elements from list and Zn
        # we get one of the two elements m or t
        for i in range(len(list)):
            if i & differ_bit :
                miss_or_dup ^= i
            
            if list[i] & differ_bit :
                miss_or_dup ^= list[i]
        
        print("m^t : " + str(miss_XOR_dup) + " differ_bit : " + str(differ_bit) +
                " element 1 : " + str(miss_or_dup) + 
                " element 2 : " + str(miss_XOR_dup ^ miss_or_dup) )

def test() :
    # missing element(t) = 9 and duplicate element(m) = 4
    list = [0, 1, 2, 3, 4, 4, 5, 6, 7, 8]
    o = FindMissingAndDuplicate()
    o.find(list)

if __name__ == '__main__' :
    test()
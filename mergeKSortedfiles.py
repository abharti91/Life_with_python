'''
Suppose there are hundred of file containing stock details, starting int showing milliseconds from start of day, sorted by milliseconds.
Mere all files in sorted order, asumming RAM is in KB and file sizes may be of GB's or TB's.
'''
import heapq

class MergeKSortedFiles():
    def __init__(self):
        try:
            self._heap = []
            self._ouput_file = open('outputfile', 'w+')
        except:
            print("Error while creating Merge class ")

    def merge(self, input_files):
        try:
            open_files = []
            [ open_files.append(open(file, 'r')) for file in input_files ]
            #store first line of each file
            [heapq.heappush(self._heap, (int(file.readline()), file)) for file in open_files]
            while(self._heap):
                # get the smallest key smallest[0]=line from file, smallest[1]=file number
                smallest = heapq.heappop(self._heap)
                print(str(smallest[0]))
                # write to output file
                self._ouput_file.write(str(smallest[0]) + "\n")
                # read next smallest element in file = smallest[0]
                read_line = smallest[1].readline()
                if(len(read_line) != 0):
                    heapq.heappush(self._heap, (int(read_line), smallest[1]))

            [file.close() for file in open_files]
            self._ouput_file.close()
        except:
            print("Error while merging")

def test():
    files = ['1.txt', '2.txt', '3.txt']
    obj = MergeKSortedFiles()
    obj.merge(files)

if __name__ == '__main__':
    test()

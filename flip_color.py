'''
A is 2D array with 0=black and 1=white
    - starts from (x,y) and flip color of region associated with (x,y) only four adjacent directions
    - compute black region with most number of points/squares
'''

class FlipColor:
    def __init__(self):
        grid = [[0,0,1,1],[1,0,1,1],[1,0,0,1],[0,1,1,0]]
        self.flip_color(grid, 3, 3)

    def flip_color(self, grid, r, c):
        seen = set()
        color = grid[r][c]

        def area(r, c):
            # skip the cordinate if its color not same as color or is already visited
            if  (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == color and (r,c) not in seen):
                print("iterating with (x,y)" + str(r) + "," + str(c))
                # add to visited list
                seen.add((r,c))
                # flip the color
                if(grid[r][c] == 0):
                    grid[r][c] = 1
                else:
                    grid[r][c] = 0
                # check all 4 adjacent directions
                area(r+1,c)
                area(r-1,c)
                area(r,c+1)
                area(r,c-1)

        area(r,c)
        print()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                print(str(grid[x][y]), end=' ')
            print()


class LargestBlackRegion:
    def __init__(self):
        grid = [[0,0,0,1],[1,0,0,1],[1,0,0,0],[0,1,1,0]]
        self.compute_region(grid)

    def compute_region(self, grid):
        seen =set()
        maximum = 0

        # starting point of each region
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # if not seen get the count of black points in this region
                if((r,c) not in seen and grid[r][c] == 0):
                    print("Starting region from (" + str(r) + " " + str(c) + ")")
                    def countPoints(r, c):
                        if  (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0 and (r,c) not in seen):
                            seen.add((r,c))
                            return 1 + countPoints(r+1, c) + countPoints(r-1, c) + countPoints(r, c+1) + countPoints(r, c-1)
                        else:
                            return 0
                    maximum = max(maximum, countPoints(r,c))
        print("largest black region has " + str(maximum) + " points")
        return maximum

#foo = FlipColor()
obj = LargestBlackRegion()
'''
0 0 0 1
1 0 0 1
1 0 0 0
0 1 1 0
'''

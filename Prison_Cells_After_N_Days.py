class Solution(object):

    def __init__(self, cells, N):
        self.cells = cells
        self.N = N

    def prisonAfterNDays(self):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        cells2 = [0,0,0,0,0,0,0,0]
        for i in range(1,N+1):
            for j in range (1,7):
                if (self.cells[j-1] == 0 and self.cells[j+1] == 0) or (self.cells[j-1] == 1 and self.cells[j+1] == 1):
                    cells2[j] = 1
                else:
                    cells2[j] = 0
            self.cells = cells2.copy()
        return cells2

cells = [0,1,0,1,1,0,0,1]
N = 1

clase = Solution(cells,N)
print(clase.prisonAfterNDays())

clase = Solution(clase.prisonAfterNDays(),N)
print(clase.prisonAfterNDays())


# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]

# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

# Output: [0,0,1,1,0,0,0,0]
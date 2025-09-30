class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = set()
        a = 0
        actSum = 0
        expSum = 0
        b = 0
        n = len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                actSum += grid[i][j]
                if (grid[i][j] in s):
                    a = grid[i][j]
                else:
                    s.add(grid[i][j])
        
        expSum = n*n * (n*n + 1) / 2

        b = int(expSum - actSum + a)
        return [a, b]
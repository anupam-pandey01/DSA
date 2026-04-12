class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        for i in range(len(matrix)):
            count = 0
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    count += 1
            ans.append(count)

        return ans
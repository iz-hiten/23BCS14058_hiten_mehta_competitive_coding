class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        def dfs(i, j, memo: dict):
            if i >= m or j >= n:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if (i, j) not in memo:
                memo[(i, j)] = dfs(i+1, j, memo) + dfs(i, j+1, memo)
            return memo[(i, j)]
        return dfs(0, 0, {})

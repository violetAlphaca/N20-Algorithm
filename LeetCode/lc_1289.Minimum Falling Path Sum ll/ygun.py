class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        rows = len(arr)
        cols = len(arr[0])
        dp = [[0]*cols for i in range(rows)]
        for i in range(cols):
            dp[0][i] = arr[0][i]
        
        
        for r in range(1,rows):
            for c in range(cols):
                localMin = 999999999999
                for compCol in range(cols):
                    if c != compCol:
                        localMin = min(dp[r-1][compCol] + arr[r][c], localMin)
                dp[r][c] = localMin
        
        return min(dp[rows-1])
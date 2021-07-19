class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        1.DFS
        2.two moving option: grid[i+1][j], grid[i][j+1]
        3.return min path sum
        bottom up
        """

        def getPathSum(i, j):
            if i == len(grid) - 1 and j == len(grid[i]) - 1:
                return grid[i][j]
            cur_sum1 = 10000000000
            cur_sum2 = 10000000000

            if i < len(grid) - 1:
                cur_sum1 = grid[i][j] + getPathSum(i + 1, j)
            if j < len(grid[i]) - 1:
                cur_sum2 = grid[i][j] + getPathSum(i, j + 1)
            return min(cur_sum1, cur_sum2)

        i = 0
        j = 0
        sum = getPathSum(i, j)
        return sum


    def minPathSum_dp(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        DFS + backtrack
        """
        w = len(grid)
        l = len(grid[0])

        def getMin(i, j):
            pre1 = None
            pre2 = None
            if i > 0:
                pre1 = record[i - 1][j]
            if j > 0:
                pre2 = record[i][j - 1]
            # print(pre1)
            # print(pre2)
            if pre1 is None and pre2 is not None:
                record[i][j] = pre2 + grid[i][j]
            elif pre2 is None and pre1 is not None:
                record[i][j] = pre1 + grid[i][j]
            elif pre2 is not None and pre1 is not None:
                record[i][j] = min(pre2, pre1) + grid[i][j]
            else:
                record[i][j] = grid[i][j]
            # print(record)

        record = [[0] * l for i in range(w)]
        record[0][0] = grid[0][0]

        w_c = 0
        l_c = 0
        while w_c < w and l_c < l:
            for i in range(w_c, w):
                getMin(i, l_c)
            for j in range(l_c, l):
                getMin(w_c, j)
            w_c += 1
            l_c += 1
        return record[-1][-1]

    def minPathSum1(self, grid):
        r, c = len(grid), len(grid[0])
        dp = [[grid[0][0] for _ in range(c)] for _ in range(r)]
        for i in range(1, r):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, c):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]







class Solution(object):
    #  recursive start from [m-1,n-1]
    #  recursive when reach target[0,0], return 1
    #  recursive also return the number of leaves of this node
    #  each node have two children at most [m-1] [n-1]
    _path_cnt = 0

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.getLeavesOfTree(m - 1, n - 1)
        return self._path_cnt

    def getLeavesOfTree(self, m, n):
        up_cnt = 0
        left_cnt = 0

        if m == 0 and n == 0:
            self._path_cnt = self._path_cnt + 1

        if m - 1 >= 0 and n >= 0:
            self.getLeavesOfTree(m - 1, n)

        if n - 1 >= 0 and m >= 0:
            self.getLeavesOfTree(m, n - 1)


    def solution2(self, m, n):
        if m < 0 or n < 0 :
            return False;
        a = [[0] * n] * m
        a[0] = [1] * n
        for i in range(m) :
            a[i][0] = 1
        print(a)
        #
        for i in range(1,m):
            for j in range(1,n):
                print(f"i:{i},j:{j}")
                a[i][j] = a[i-1][j] + a[i][j-1]

        print(a)







test = Solution()
test.solution2(3,7)

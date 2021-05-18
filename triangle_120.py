class Solution(object):

    def row_add(self,pre_row,cur_row):
        new_row = [0]*len(cur_row)
        new_row[0] = cur_row[0] + pre_row[0]
        new_row[-1] = cur_row[-1] + pre_row[-1]
        for i in range(1,len(cur_row)-1):
            new_row[i] = min(cur_row[i] + pre_row[i-1],cur_row[i] + pre_row[i])
        return new_row

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # in place add
        if triangle is None:
            return False;
        if len(triangle) == 1:
            return triangle[0][0];

        rowNo = 0
        curRow = triangle[0]

        while rowNo <  len(triangle)-1:
            rowNo += 1
            print(rowNo)
            curRow = self.row_add(curRow, triangle[rowNo])

        return max(curRow)




test = Solution()

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

print(triangle[0][-1])

test.minimumTotal(triangle)









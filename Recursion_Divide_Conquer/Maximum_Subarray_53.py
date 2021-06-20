class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        cur_sum = nums[0]
        for n in nums[1:]:
            if cur_sum + n > n:
                cur_sum = cur_sum + n
                max_sum = max(max_sum,cur_sum)
            else:
                cur_sum = n
                max_sum = max(max_sum, cur_sum)
        return max_sum



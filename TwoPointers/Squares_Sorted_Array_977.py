class Solution(object):
    def sortedSquare_sample(self, nums):
        """
        :param nums:
        :return:
        time complexity: O(nlog(n))
        space comlexity: no extra space
        [-4,-1,0,3,10]
        1. [16,1,0,9,100] in place
        2. sorted([16,1,0,9,100])
        """
        # in-place
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        # new a list
        # nums = [x**2 for x in nums]
        return sorted(nums)

    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]


       #   how to merge two sorted list
        [-4,-1,0,3,10]
         l          r     [100]
         l        r       [100,16]
             l    r       [100,16,9]
             l  r         [100,16,9,1]
                l/r       [100,16,9,1,0]

         return [100,16,9,1,0][::-1]

       Space complexity: O(n), time complexity: O(n)
        """
        l = 0
        r = len(nums) - 1
        squares_nums = []
        while l != r:
            if abs(nums[l]) > abs(nums[r]):
                squares_nums.append(nums[l]**2)
                l += 1
            else:
                squares_nums.append(nums[r] ** 2)
                r -= 1
        squares_nums.append(nums[r] ** 2)
        return reversed(squares_nums)

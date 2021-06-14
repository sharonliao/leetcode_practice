class Solution(object):
    # Input: nums = [2,7,11,15], target = 9
    # Output: [0,1]
    # Output: Because nums[0] + nums[1] == 9, we return [0, 1].

    # time complexity O(N)
    # space complexity O(N)


    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remain_dict = {}
        for index,value in enumerate(nums):
            if remain_dict.get(value) is not None:
                # this value is a remainder for a value in the hashmap
                return [index,remain_dict.get(value)]
            else:
                remain_dict[target-value] = index;

nums = [-1,0,1,2,-1,-4]




class Solution(object):
    def twoSum(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remain_dict = {}
        for index1, value1 in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if index1 > index2:
                    if remain_dict.get(value1+value2) is None:
                        remain_dict[value1+value2] = [[index1,index2]]
                    else:
                        # print(f"remain:{remain_dict.get(value1+value2)}")
                        remain_dict.get(value1+value2).append([index1,index2])
        return remain_dict

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        two_sum_dict = self.twoSum(nums)
        result_list = set()
        for index, value in enumerate(nums):
            if two_sum_dict.get(0-value) is not None:
                for twosum in two_sum_dict.get(0-value):
                    if index not in twosum:
                        threeSum = twosum + [index]
                        threeSum = [nums[index] for index in threeSum]
                        result_list.add(tuple(sorted(threeSum)))
        value_result_list = []
        for result in result_list:
            value_result_list.append(list(result))
        return value_result_list

nums = [-1,0,1,2,-1,-4]
result = Solution().threeSum(nums)
print(f"result : {result}")
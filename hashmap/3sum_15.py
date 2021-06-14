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


    def threeSum_set(self, nums):
        res, dups = set(), set()
        for i, val1 in enumerate(nums):
            # 1.sublist问题，只需要考虑第一个for loop的value，作为3个value做的第一个数。
            #   意思就是当for loop到list中的某一个值时，另外两个values只需要从该元素之后的sublist中选出
            #   为什么？因为当前for loop的value，它其实已经作为后两位操作数被list中它之前元素筛选过了。
            #   所以现在轮到他做第一个操作数了，不再需要考虑他之前的value
            seen = set()
            if val1 not in dups:
                dups.add(val1)
                # 2. 第一个操作数重复的话，这个round可以跳过
                #    为什么？最先出现的操作数已经把它sublist中的所有可能性都选出来了，
                #    而后一个出现的重复操作数，他的sublist肯定是前一个sublist的子集，
                #    所以没必要再对一个子集进行重复的查找。
                #    dups set的作用，过滤重复计算
                for j, val2 in enumerate(nums[i + 1:]):
                    complement = -val1 - val2
                    if complement in seen:
                        # 3.这个seen的作用，其实只要是用来完成two sum的
                        #   3sum和2sum不一样的地方在于，3sum不需要返回index，那么我只需要返回子集中符合的value
                        #   所以，seen set 就是用来存当前2sum sublist中的元素的。
                        #   为什么答案用hashmap呢，hashmap和set的查询速度应该都是O(1)？
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen.add(val2)
        return res






nums = [-1,0,1,2,-1,-4]
result = Solution().threeSum(nums)
print(f"result : {result}")
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hashmap
        votes = {}
        max_count = 0
        maj_n = nums[0]
        for n in nums:
            count = votes.get(n, 0)
            votes[n] = count + 1
            if count>max_count:
                max_count = count
                maj_n = n
        return maj_n

    def majorityElement_Boyer_Moore(self,nums):
        # As the majority element is the element that appears more than ⌊n / 2⌋ times
        # so,
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


    #229. Majority Element II
    def majorityElement_229(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
        votes = {}
        results = set()
        length = len(nums)
        for n in nums:
            count = votes.get(n, 0)
            votes[n] = count + 1
            if count + 1 > length/3 :
                results.add(n)
        return list(results)





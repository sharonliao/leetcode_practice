def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    if len(A) == 0:
        return 1
    pre = 0
    for val in A:
        if val < 0:
            pre = 0
        else:
            if val-pre == 1 or val==pre:
                pre = val
            else:
                return pre+1
    if A[-1]<0:
        return 1
    else:
        return A[-1]+1



def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within
         the range [1,...,l+1]
    """
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        # 1.delete nums below 0
        # 2.delete nums greater than n , [1,2,3,4]
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        nums[nums[i]%n]+=n
    for i in range(1,len(nums)):
        if nums[i]/n==0:
            return i
    return n
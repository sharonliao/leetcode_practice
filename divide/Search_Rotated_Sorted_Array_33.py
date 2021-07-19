class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while (right > left + 1):
            mid = (right - left) //2 + left
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[left]:
                if target <= nums[mid] and target >= nums[left]:
                    right = mid
                else:
                    left = mid
            else:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid
                else:
                    right = mid
        if nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        else:
            return -1

    def search2(self, A, target):
        n = len(A)
        left, right = 0, n - 1
        if n == 0: return -1

        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] == target: return mid

            # inflection point to the right. Left is strictly increasing
            if A[mid] >= A[left]:
                if A[left] <= target < A[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # inflection point to the left of me. Right is strictly increasing
            else:
                if A[mid] < target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


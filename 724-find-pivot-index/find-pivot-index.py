class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = 0
        total = 0

        for i in range(len(nums)):
            total += nums[i]

        for i in range(len(nums)):
            right = total - left - nums[i]

            if right == left:
                return i
            left += nums[i]
        
        return -1
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        j = 1
        currSum = nums[0]
        maxSum = nums[0]

        while(j < len(nums)):
            if(nums[j] > nums[j-1]):
                currSum += nums[j]
            else:
                currSum = nums[j]
            
            maxSum = max(currSum, maxSum)
            j+=1
        
        return maxSum


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        def allsubset(nums, comb, i, ans):
            if(i == len(nums)):
                ans.append(comb.copy())
                return
            
            comb.append(nums[i])
            allsubset(nums, comb, i+1, ans)
            comb.pop()
            allsubset(nums, comb, i+1, ans)

        allsubset(nums, [], i, ans)

        return ans

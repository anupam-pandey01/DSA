class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def subset(nums, i, comb, ans):
            nums.sort()
            if(i == len(nums)):
                ans.append(comb.copy())
                return

            comb.append(nums[i])
            subset(nums, i+1, comb, ans)

            idx = i+1
            while(idx < len(nums) and nums[idx] == nums[idx - 1]):
                idx += 1
            
            comb.pop()
            subset(nums, idx, comb, ans)

        subset(nums, 0, [], ans)
        return ans
        
            


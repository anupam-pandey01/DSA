class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def allpermute(nums, comb, ans):
            if(len(nums) == 0):
                ans.append(comb)
                return
            
            for i  in range(len(nums)):
                new_nums = nums[ :i] + nums[i+1: ]
                new_comb = comb + [nums[i]]

                allpermute(new_nums, new_comb, ans)

        allpermute(nums, [], ans)

        return ans
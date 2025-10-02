class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(comb, tar, idx):
            if tar == 0:
                ans.append(comb[:])
                return
            
            if(idx >= len(candidates) or tar < 0):
                return

            comb.append(candidates[idx])
            backtrack(comb, tar - candidates[idx], idx)
            comb.pop()
            backtrack(comb, tar, idx + 1)

        backtrack([], target, 0)
        return ans
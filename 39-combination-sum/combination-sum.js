/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const ans = [];

    function backtrack(idx, tar, combine) {
        // Base case: target reached
        if (tar === 0) {
            ans.push([...combine]);  // push copy
            return;
        }

        // If we reach end or target becomes negative
        if (idx >= candidates.length || tar < 0) {
            return;
        }

        // Include current number
        combine.push(candidates[idx]);
        backtrack(idx, tar - candidates[idx], combine);  // stay at idx (can reuse same number)
        combine.pop();

        // Exclude current number
        backtrack(idx + 1, tar, combine);
    }

    backtrack(0, target, []);
    return ans;
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    res = nums.length;
    for(let i=0; i<nums.length; i++){
        res += i - nums[i]
    }
    return res;
};
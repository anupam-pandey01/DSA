/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let res = -Infinity;
    let currSum = 0;
    for(let i=0; i<nums.length; i++){
        currSum += nums[i];
        res = Math.max(res, currSum);
        if(currSum < 0){
            currSum = 0;
        }
    }
    return res;
};
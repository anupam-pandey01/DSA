/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let sing = nums[0];
    for(let i=1; i<nums.length; i++){
        sing = sing ^ nums[i];
    }
    return sing;
};
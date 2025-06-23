/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function minOperations(nums) {
    const uniqueNumber = new Set();
    for(let i=0; i<nums.length; i++){
        if(nums[i] != 0){
            uniqueNumber.add(nums[i]);
        }
    }
    return uniqueNumber.size;
}

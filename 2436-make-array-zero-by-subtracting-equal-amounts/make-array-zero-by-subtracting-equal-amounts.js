/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function minOperations(nums) {
    const uniqueNum = new Set();
    for(let i=0; i<nums.length; i++){
        if(nums[i] != 0){
            uniqueNum.add(nums[i]);
        }
    }
    return uniqueNum.size;
}

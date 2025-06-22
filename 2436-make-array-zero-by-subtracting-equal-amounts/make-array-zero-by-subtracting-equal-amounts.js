/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function minOperations(nums) {
    const uniqueElement = new Set();
    for(let i=0; i<nums.length; i++){
        if(nums[i] > 0){
            uniqueElement.add(nums[i]);
        }
    }
    return uniqueElement.size;
}

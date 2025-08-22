/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let right=nums.length - 1;
    let left=0;

    while(left <= right){
        let mid = Math.floor((right + left)/2);
        if(nums[mid] == target){
            return mid;
        }
        else if( nums[mid] < target){
            left = mid + 1;
        }
        else{
            right = mid - 1;
        }
    }
    return left;
};
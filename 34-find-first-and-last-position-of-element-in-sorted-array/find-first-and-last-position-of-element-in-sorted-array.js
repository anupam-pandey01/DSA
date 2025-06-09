/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    
    function binarySearch(nums, target, isSearchLeft){
        let left = 0;
        let right = nums.length - 1;
        
        let idx = -1;
        while(left <= right){
            let mid = Math.floor((left + right) / 2);
            if(nums[mid] < target){
                left = mid + 1;
            }
            else if(nums[mid] > target){
                right = mid - 1;
            }
            else{
                idx = mid;
                if(isSearchLeft){
                    right = mid - 1;
                }
                else{
                    left = mid + 1;
                }
            }
        }
        return idx;
    }
    
    let left = binarySearch(nums, target, true);
    let right = binarySearch(nums, target, false);
    return [left, right]; 
};
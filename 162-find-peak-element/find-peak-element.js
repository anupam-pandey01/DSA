/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    let st = 0;
    let end = nums.length - 1;

    while(st < end){
        let mid = Math.floor((st + end)/2);
        
        if(nums[mid] > nums[mid + 1]){
            end = mid;
        }else{
            st = mid + 1;
        }
    }
    return st;
};
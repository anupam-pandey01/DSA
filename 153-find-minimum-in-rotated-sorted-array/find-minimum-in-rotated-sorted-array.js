/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let st = 0;
    let end = nums.length - 1;

    while(st < end){
        let mid = Math.floor((st + end)/2);
        if(nums[mid] > nums[end]){
            st = mid + 1;
        }
        else{
            end = mid;
        }
    }
    return nums[st]
};
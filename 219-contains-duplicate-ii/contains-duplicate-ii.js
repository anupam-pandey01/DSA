/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    let seen = {};
    for(let i=0; i<nums.length; i++){
        let val = nums[i];
        if(seen.hasOwnProperty(val) && i - seen[val] <= k){
            return true;
        }
        seen[val] = i;
    }
    return false;
};
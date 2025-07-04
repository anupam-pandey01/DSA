/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let fr = 1;
    let ans = nums[0];
    nums.sort((a, b) => (a - b));
    for(let i=1; i<nums.length; i++){
        if(nums[i] == nums[i - 1]){
            fr++;
        }
        else{
            fr = 1;
        }
        if(fr > nums.length/2){
            return nums[i];
        }
    }

    return ans;

};
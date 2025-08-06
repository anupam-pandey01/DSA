/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let fr = 0;
    let ans = 0;

    for(let i=0; i<nums.length; i++){
        if(fr == 0){
            ans = nums[i];
        }
        if(ans == nums[i]){
            fr++;
        }else{
            fr--;
        }
    }
    return ans;
};
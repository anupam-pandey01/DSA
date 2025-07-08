/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
   let prefix = []
   let suffix = []
   prefix[0] = 1;
   suffix[nums.length - 1] = 1;
   let ans = []

//    Prefix
   for(let i=1; i<nums.length; i++){
        prefix[i] = prefix[i - 1] * nums[i - 1];
   }

//    suffix
    for(let i=nums.length -2; i>=0; i--){
        suffix[i] = suffix[i + 1] * nums[i + 1];
    }

//   Ans
    for(let i=0; i<nums.length; i++){
        ans[i] = prefix[i] * suffix[i]
    }
    return ans;
};
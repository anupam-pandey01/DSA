/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let XOR = 0;
    let n = nums.length;
    for(let i=0; i<=n; i++){
        XOR ^= i; // XOR of all indics;
        XOR ^= nums[i] // XOR of all nums in array;
    }
    // XOR ^= n
    return XOR;
};
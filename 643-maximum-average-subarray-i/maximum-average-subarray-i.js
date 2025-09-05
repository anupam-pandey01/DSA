/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let sum = 0;
    let maxAvg = -Infinity;
    let i = 0;
    let j = 0;

    while(j<nums.length){
        let avg = 0;
        sum+=nums[j]
        if(j - i + 1 == k){
            avg = sum / k;
            maxAvg = Math.max(maxAvg, avg);
            sum -= nums[i]
            i++;
        }
        j++
    }
    return maxAvg;
};
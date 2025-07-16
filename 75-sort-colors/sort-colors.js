/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let n = nums.length;
    let count0 = 0; 
    let count1 = 0;
    let count2 = 0;
    for(let i=0; i<n; i++){
        if(nums[i]==0){
            count0++;
        }
        else if(nums[i]==1){
            count1++;
        }
        else{
            count2++;
        }
    }
    
    let idx = 0;
    for(let i=0; i<count0; i++){
        nums[idx] = 0;
        idx++;
    }

    for(let i=0; i<count1; i++){
        nums[idx] = 1;
        idx++;
    }

    for(let i=0; i<count2; i++){
        nums[idx] = 2;
        idx++;
    }
};
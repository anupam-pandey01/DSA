/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
  let i = 0;
  let res = [];
  while(i < nums.length){
    let start = nums[i];

    while(i < nums.length-1 && (nums[i] + 1 == nums[i + 1])){
        i += 1;
    }
    if(start != nums[i]){
        res.push(String(start) + "->" + String(nums[i]));
    }
    else{
        res.push(String(nums[i]));
    }
    i++;
  }
  return res;
};
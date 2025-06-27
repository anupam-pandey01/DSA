/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
  let res = []
  let i = 0;
  while(i < nums.length){
    let start = nums[i];
    while((i < nums.length - 1) && (nums[i] + 1 == nums[i + 1])){ 
        i += 1;
    }
    if(start == nums[i]){
        res.push(String(start));
    }
    else{
        res.push(String(start) + "->" + String(nums[i]))
    }
    i++;
  }
  return res
};
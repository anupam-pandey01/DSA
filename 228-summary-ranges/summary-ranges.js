/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
  let l = 0;
  let res = [];
  while(l < nums.length){
    let start = nums[l];
    
    while(l < nums.length-1 && (nums[l] + 1 == nums[l + 1])){
        l+=1;
    }
    if(nums[l] == start){
        res.push(String(start))
    }
    else{
        res.push(String(start) + "->" + String(nums[l]))
    }
    l+=1;
  }
  return res;
};
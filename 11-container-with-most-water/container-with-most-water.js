/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left = 0;
    let right = height.length - 1;
    let maxArea = 0;
    while(left < right){
        let width = right - left;
        let currHeight = Math.min(height[left], height[right]);
        let currArea = currHeight * width;
        maxArea = Math.max(maxArea, currArea);
        if(height[left] < height[right]){
            left++;
        }else{
            right--;
        }
    }
    return maxArea;
};
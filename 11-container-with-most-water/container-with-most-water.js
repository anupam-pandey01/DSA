/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left = 0;
    let right=height.length-1;
    let area=0;

    while(left < right){
        let width = right - left;
        let minHeight = Math.min(height[right], height[left]);
        let currArea = minHeight * width;
        area = Math.max(area, currArea)
        if(height[right] > height[left]){
            left++;
        }else{
            right--;
        }
    }
    return area;
};
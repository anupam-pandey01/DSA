/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if(x < 0) return false;

    const arr = [];
    while(x > 0){
        let val = x % 10;
        x = Math.floor(x / 10);
        arr.push(val);
    }

    let left = 0;
    let right = arr.length - 1;
    while(left < right){
        if(arr[left] != arr[right]){
            return false;
        }
        left++;
        right--;
    }
    return true;
};
/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    let binForm = n;
    if(n < 0){
        x = 1/x;
        binForm = -binForm
    }
    let ans = 1;
    while(binForm > 0){
        if(binForm % 2 == 1){
            ans *= x;
        }
        x *= x;
        binForm = Math.floor(binForm / 2);
    }
    return ans;
};
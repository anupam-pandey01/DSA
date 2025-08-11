/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s = s.replace(/[^a-z0-9]/gi, '').toLowerCase();
    let st = 0;
    let end = s.length -1 ;
    while(st <= end){
        if(s[st] != s[end]){
            return false
        }
        st++;
        end--;
    }
    return true;
};
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let maxLen= 0;
    let set = new Set();
    let left=0;
    for(let i=0; i<s.length; i++){
            while(set.has(s[i])){
                    set.delete(s[left]);
                    left++
            }
            set.add(s[i]);
            maxLen = Math.max(maxLen, i - left + 1);
    }
    return maxLen;
};
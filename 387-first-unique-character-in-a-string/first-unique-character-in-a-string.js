/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    const counter = new Map();

    for(let char of s){
        counter.set(char, (counter.get(char) || 0) + 1);
    }

    for(let i=0; i<s.length; i++){
        if(counter.has(s[i]) && counter.get(s[i]) == 1){
            return i;
        }
    }
    return -1;
};
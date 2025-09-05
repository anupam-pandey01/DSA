/**
 * @param {string} s
 * @return {number}
 */
var countGoodSubstrings = function(s) {
    let freq = {}
    let count = 0;
    let i = 0;
    
    for(let j=0; j<s.length; j++){
        freq[s[j]] = ( freq[s[j]] || 0 ) + 1;

        if(j-i+1 == 3){
            if(Object.keys(freq).length == 3){
                count++
            }
            freq[s[i]]--
            if(freq[s[i]] == 0){
                delete freq[s[i]];
            }
            i++
        }
    }
    return count;
};
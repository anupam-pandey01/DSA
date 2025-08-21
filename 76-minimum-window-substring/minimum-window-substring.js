/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    let map = new Map();
    for(let i=0; i<t.length; i++){
        map.set(t[i], (map.get(t[i]) || 0 ) + 1);
    }

    let count = map.size;
    let i=0;
    let j=0;
    let minLen = Infinity;
    let res = "";

    while(j<s.length){
        if(map.has(s[j])){
            map.set(s[j], map.get(s[j]) - 1)
            if(map.get(s[j]) == 0){
                count--
            }
        }
        while(count == 0){
            let currStr = s.substring(i, j + 1);

            if(currStr.length < minLen){
                minLen = currStr.length;
                res = currStr;
            }

            if(map.has(s[i]) ){
                if(map.get(s[i]) === 0) count++;
                map.set(s[i], map.get(s[i]) + 1)
            }
            i++;
        }
        j++;
    }
    return res;
};
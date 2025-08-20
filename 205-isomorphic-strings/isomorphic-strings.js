/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {

    if(s.length != t.length){
        return false;
    }

    let mapST = new Map();
    let mapTS = new Map();

    for(let i=0; i<s.length; i++){
        let charS = s[i];
        let charT = t[i];

        if(mapST.has(s[i]) && mapST.get(s[i]) != charT){
            return false;
        }
        if(mapTS.has(t[i]) && mapTS.get(t[i]) != charS){
            return false
        }

        mapST.set(charS, charT);
        mapTS.set(charT, charS);
    }
    
    return true;
};
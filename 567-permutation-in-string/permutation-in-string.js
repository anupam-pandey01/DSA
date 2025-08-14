/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    
    function isFreqSame(freq1, freq2){
        for(let i=0; i<26; i++){
            if(freq1[i] != freq2[i]){
                return false;
            }
        }
        return true;
    }

    let freq = new Array(26).fill(0);
    
    for(let i=0; i<s1.length; i++){
        let idx = s1[i].charCodeAt(0) - "a".charCodeAt(0)
        freq[idx]++
    }

    let windSize = s1.length;
    for(let i=0; i<s2.length; i++){
        let windFreq = new Array(26).fill(0);
        let windIdx=0; 
        let idx=i;
       
        while(windIdx < windSize && idx < s2.length){
            let freqIdx = s2[idx].charCodeAt(0) - "a".charCodeAt(0);
            windFreq[freqIdx]++
            windIdx++;
            idx++;
        }

        if(isFreqSame(freq, windFreq)){
            return true;
        }
    }
    return false;
};
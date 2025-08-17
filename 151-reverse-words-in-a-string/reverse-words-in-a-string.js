/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let words = s.split(" ");
    let res = []
    for(let i=0; i<words.length; i++){
        if(words[i] != ""){
            res.push(words[i]);
        }
    }
    let reversed = res.reverse();
    return reversed.join(" ");
};
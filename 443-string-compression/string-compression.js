/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    let idx = 0;
    for(let i=0; i<chars.length; ){
        let ch = chars[i];
        let count = 0;
        while( i < chars.length && chars[i] == ch){
            count++;
            i++;
        }
        if(count == 1) {
            chars[idx] = ch;
            idx++
        }else{
            chars[idx] = ch;
            idx++;
            let str = count.toString();
            for(dig of str){
                chars[idx] = dig;
                idx++;
            }
        }
    }
    return idx;
};
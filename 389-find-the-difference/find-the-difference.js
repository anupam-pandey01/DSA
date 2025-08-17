/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    const counter = new Map();

    for(ch of s){
        counter.set(ch, (counter.get(ch) || 0) + 1)
    }

    for(ch of t){
        if(counter.has(ch) && counter.get(ch) > 0){
            counter.set(ch, counter.get(ch) - 1);
        }
        else if(counter.has(ch) == 0){
            return ch;
        }
        else{
            return ch;
        }
    }
};
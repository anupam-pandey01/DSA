/**
 * @param {string} s
 * @param {string} part
 * @return {string}
 */
var removeOccurrences = function(s, part) {
    while (s.indexOf(part) !== -1) {
        let idx = s.indexOf(part);
        s = s.slice(0, idx) + s.slice(idx + part.length);
    }
    return s;
};

/**
 * @param {string} s
 * @return {string}
 */
var longestPrefix = function(s) {
    let n = s.length;

    // check from longest to shortest prefix
    for (let len = n - 1; len > 0; len--) {
        let prefix = s.substring(0, len);
        let suffix = s.substring(n - len);

        if (prefix === suffix) {
            return prefix;
        }
    }

    return "";
};
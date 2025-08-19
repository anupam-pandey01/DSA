/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    if (s1.length > s2.length) return false;

    let s1Count = new Map();
    let s2Count = new Map();

    // build frequency counts
    for (let i = 0; i < s1.length; i++) {
        s1Count.set(s1[i], (s1Count.get(s1[i]) || 0) + 1);
        s2Count.set(s2[i], (s2Count.get(s2[i]) || 0) + 1);
    }

    if (isEqual(s1Count, s2Count)) return true;

    let left = 0;
    for (let right = s1.length; right < s2.length; right++) {
        // add new character
        s2Count.set(s2[right], (s2Count.get(s2[right]) || 0) + 1);

        // remove old character
        s2Count.set(s2[left], s2Count.get(s2[left]) - 1);
        if (s2Count.get(s2[left]) === 0) {
            s2Count.delete(s2[left]);
        }
        left++;

        if (isEqual(s1Count, s2Count)) return true;
    }

    return false;

    function isEqual(map1, map2) {
        if (map1.size !== map2.size) return false;
        for (let [key, val] of map1) {
            if (map2.get(key) !== val) return false;
        }
        return true;
    }
};

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    const res = [];
    intervals.sort((a, b)=> a[0] - b[0]);
    const merged = [];
    let prev = intervals[0];

    for(let i=1; i<intervals.length; i++){
        let interval = intervals[i]

        if(interval[0] <= prev[1]){
            prev[1] = Math.max(interval[1], prev[1]);
        }else{
            merged.push(prev);
            prev = interval;
        }
    }

    merged.push(prev)
    return merged;
};
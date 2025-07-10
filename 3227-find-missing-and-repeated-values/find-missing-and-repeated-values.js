/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findMissingAndRepeatedValues = function(grid) {
    let s = new Set();
    let a = -1;
    let b = -1;
    let expSum = 0;
    let actualSum = 0;
    let n = grid.length;
    for(let i=0; i<n; i++){
        for(let j=0; j<n; j++){
            actualSum += grid[i][j];
            if(s.has(grid[i][j])){
                a = grid[i][j];
            }
            else{
                s.add(grid[i][j])
            }
        }
    }

    expSum = (n*n) * (n*n + 1) / 2;
    b = expSum - actualSum + a;
    return [a, b];
};
/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findMissingAndRepeatedValues = function(grid) {
    let s = new Set();
    let n = grid.length;
    let a = -1;
    let b = -1;
    let actSum = 0;
    let expSum = 0;
    for(let i=0; i<n; i++){
        for(let j=0; j<n; j++){
            actSum += grid[i][j];
            if(s.has(grid[i][j])){
                a = grid[i][j];
            }else{
                s.add(grid[i][j])
            }
        }
    }
    expSum = (n*n) * (n*n + 1) / 2;
    b = expSum - actSum + a;
    return [a, b]
};
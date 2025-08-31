/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
  let m=matrix.length;
  let n=matrix[0].length;  

  let startRow=0;
  let endRow=m-1;

  function searchInCol(mat, tar, midRow){
    let start=0;
    let end=n-1;

    while(start <= end){
        let mid= Math.floor((start + end)/2)

        if(mat[midRow][mid] === target){
            return true;
        }
        else if(mat[midRow][mid] < tar){
            start = mid+1;
        }else{
            end = mid-1;
        }
    }
    return false;
  }

  while(startRow <= endRow){
    let midRow=Math.floor((startRow + endRow) / 2);

    if(matrix[midRow][0] <= target && matrix[midRow][n-1] >= target){
        // Find the row
        return searchInCol(matrix, target, midRow);
    }
    else if(target >= matrix[midRow][n-1]){
        startRow=midRow+1;
    }
    else{
        endRow=midRow-1;
    }
  }

  return false;
};
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
  let n = matrix.length;
  let m = matrix[0].length; 
  let low = 0; 
  let high = (m * n - 1);

  while (low <= high) {
    let mid = Math.floor((low + high) / 2);
    let row = Math.floor(mid / m);
    let col = mid % m;

    if (matrix[row][col] < target) {
      low = mid + 1;
    } else if (matrix[row][col] > target) {
      high = mid - 1;
    } else {
      return true;
    }
  }

  return false;
};

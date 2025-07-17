var nextPermutation = function(nums) {
    
    // Find the pivot
    let piv = -1;
    let n = nums.length;

    for(let i = n - 2; i >= 0; i--){
        if(nums[i] < nums[i+1]){
            piv = i;
            break;
        }
    }

    if(piv === -1){
        nums.reverse();
        return;
    }

    // Finding the rightmost element
    for(let i = n - 1; i > piv; i--){
        if(nums[i] > nums[piv]){
            [nums[i], nums[piv]] = [nums[piv], nums[i]];
            break;
        }
    }

    // Reverse the suffix
    let i = piv + 1;
    let j = n - 1;
    while (i < j){
        [nums[i], nums[j]] = [nums[j], nums[i]];
        i++;
        j--;
    }
};

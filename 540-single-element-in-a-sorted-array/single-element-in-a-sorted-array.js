/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function(nums) {
    let st = 0;
    let end = nums.length;

    while(st <= end){
        mid = Math.floor((st + end)/2);

        // Return the mid value if is not matched with left and right
        if(nums[mid - 1] != nums[mid] && nums[mid + 1] != nums[mid]){
            return nums[mid];
        }

        // Check that L & R both have even or odd number of element exist

        if(mid % 2 == 0){   // Both L & R is even
            if(nums[mid - 1] == nums[mid]){   // Select the left searching space
                end  = mid - 1;
            }else{                            // Select the right searching space
                st = mid + 1;
            }
        }else{               // Both L & R is Odd
            if(nums[mid - 1] == nums[mid]){
                st = mid + 1;
            }else{
                end = mid - 1;
            }
        }
    }
};
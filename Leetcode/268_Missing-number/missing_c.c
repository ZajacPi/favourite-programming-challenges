int missingNumber(int* nums, int numsSize) {
    int actual=0;
    int expected=0;
    for(int i; i< numsSize+1; i++){
       expected += i;
    }
     for(int i; i< numsSize; i++){
         actual += nums[i];
     }
     return expected-actual

}

int nums = [0, 1, 3];
int numsSize=3;
int missing = missingNumber(nums, numsSize);
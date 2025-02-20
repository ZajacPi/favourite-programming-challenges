//#include<iostream>
//#include <vector>
//class Solution {
//public:
//    int missingNumber(std::vector<int>& nums) {
//        int expected=0;
//        int actual=0;
//        for(int i=0; i<nums.size()+1; i++){
//            expected += i;
//        }
//        for(int i=0; i<nums.size(); i++){
//            actual += nums[i];
//        }
//        return expected-actual;
//    }
//};
//int main(){
//    Solution task;
//    std::vector<int> nums1 = {0, 1, 3};
//    std::vector<int> nums2 = {0, 1};
//    std::vector<int> nums3 = {9,6,4,2,3,5,7,0,1};
//    int missing1 = task.missingNumber(nums1);
//    int missing2 = task.missingNumber(nums2);
//    int missing3 = task.missingNumber(nums3);
//
//    std::cout<<"Missing number: "<<missing1<< "\n";
//    std::cout<<"Missing number: "<<missing2<< "\n";
//    std::cout<<"Missing number: "<<missing3<< "\n";
//}

#include <stdio.h>

int missingNumber(int* nums, int numsSize) {
    int actual=0;
    int expected=0;

    for(int i=0; i< numsSize+1; i++){
        expected += i;
        }
    for(int i=0; i< numsSize; i++){
        actual += nums[i];
        }
    return expected-actual;

    }

int main() {
    int nums[] = {0, 1, 3};  // Correct array declaration
    int numsSize = 3;
    int missing = missingNumber(nums, numsSize);  // Call to function
    printf("The missing number is: %d\n", missing);
    return 0;
}
#include <iostream>
#include <vector>
#include <string>
#include<algorithm>
using namespace  std;
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if(nums1.size() != n+m){
            printf("nums1 should be longer");
        }
        for (int i = 0; i < n; i++) {
            nums1[m+i] = nums2[i];
        }
        std::sort(nums1.begin(), nums1.end());


    }
};

int main() {
    Solution task;
    std::vector<int> nums1 = {1,2,3,0,0,0};
    int m = 3;
    int n = 3;
    std::vector<int> nums2 = {2,5,6};

    task.merge(nums1, m, nums2, n);
    for (int i = 0; i < nums1.size(); i++) {
        cout << nums1[i] << " ";
    }
    return 0;    
}
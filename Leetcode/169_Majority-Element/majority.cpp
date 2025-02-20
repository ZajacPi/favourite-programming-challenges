#include <iostream>
#include <vector>
#include <map>

class Solution {
public:
    int majorityElement(std::vector<int>& nums) {
        std::map<int, int> stats;
        int n = nums.size();
        for(int i=0; i<n; i++){
                stats[nums[i]] ++;
        }
        //finding majority
        if (n%2 != 0){
            n++;
        }
        int thr = n/2;
        for (const auto& pair :stats){
            if (pair.second >= thr)
            {
                return pair.first;
            }
        }
        return 0;
    }
};


int main() {
    Solution task;
    std::vector<int> nums = {2,2,1,1,1,2,2};
    int solution = task.majorityElement(nums);
    std::cout<<solution<<std::endl;
    return 0;
}


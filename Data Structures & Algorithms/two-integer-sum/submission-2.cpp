class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> arr(n);
        for(int i = 0; i < n; i++){
            arr[i]=target - nums[i];
            for(int j = i+1; j < n; j++){
                if (arr[i] == nums[j]){
                    return {i,j};
                }
            }
        }
        
    }
};

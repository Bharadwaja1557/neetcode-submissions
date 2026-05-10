class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> res(2);
        vector<int> arr(n);
        for(int i = 0; i < n; i++){
            arr[i]=target - nums[i];
            for(int j = 0; j < n; j++){
                if (arr[i] == nums[j] && i!=j){
                    res[0]=i;
                    res[1]=j;
                    return res;
                }
            }
        }
        
    }
};

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = size(nums);
        vector <int> ans;
        int count = 2;
        while(count){
            for(int i = 0; i < n; i++){
                ans.push_back(nums[i]);
            }
            count--;
        }
        return ans;
    }
};
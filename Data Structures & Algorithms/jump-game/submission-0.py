class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # Greedy 

        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0

        # DP
        
        dp = [-1] * len(nums)
        dp[-1] = 1

        for i in range(len(nums)-2, -1, -1):
            far = min(i + nums[i], len(nums) - 1)
            for j in range(i+1, far + 1):
                if dp[j] == 1:
                    dp[i] = 1
                    break
        
        return dp[0] == 1

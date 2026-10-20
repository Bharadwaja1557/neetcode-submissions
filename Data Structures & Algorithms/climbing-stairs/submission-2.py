class Solution:
    def climbStairs(self, n: int) -> int:
        one = 0 # when we are at (target) stair, there are 0 ways to reach
        two = 1 # when we are at (target-1) stair, one way to reach, which is "take one step"

        for i in range(n+1):
            temp = one
            one = one + two
            two = temp
        
        return one
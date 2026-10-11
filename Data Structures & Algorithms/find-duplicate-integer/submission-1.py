class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyds Algorithm (dandam ra dootha)
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # initialize slow2 and make it meet slow
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        
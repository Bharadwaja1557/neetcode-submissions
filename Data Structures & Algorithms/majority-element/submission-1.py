class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        thisdict = {}

        if len(set(nums))==1:
            return nums[0]

        for i in range(len(nums)):
            if nums[i] in thisdict:
                thisdict[nums[i]] += 1
                if thisdict[nums[i]] >= len(nums)//2 :
                    return nums[i]
            else:
                thisdict.update({nums[i]: 0})
        print(thisdict)
        return 0
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            n=nums[i]
            diff=target-n

            if diff in h:
                return[h[diff],i]
            h[n]=i




        
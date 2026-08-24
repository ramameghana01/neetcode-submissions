class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen={}

        for i in range(0,len(nums)):
            res=target-nums[i]

            if res in seen:

                return [seen[res],i]
            else:
                seen[nums[i]]=i
            
            


            








        
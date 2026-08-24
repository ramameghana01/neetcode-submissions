class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        diff={}

        for i in range(0,len(nums)):
            if nums[i] in diff:
                if i-diff[nums[i]]<=k:
                    return True
                else:
                    diff[nums[i]]=i

            else:
                diff[nums[i]]=i
        
        return False





# if ele in dic:
#     return dic[ele]
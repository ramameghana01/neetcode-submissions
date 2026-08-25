class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            mid=(l+r)//2
            if target ==nums[mid]:
                return mid 
           #left sorted array
           #[3,4,5,1,2] and targt =1
            if nums[l]<=nums[mid]:
               if target < nums[l] or target > nums[mid]:
                  l=mid+1
               else:
                  r=mid-1
            #right sorted array 
            else:
                if target > nums[r] or target < nums[mid]:
                   r=mid-1
                else:
                   l=mid+1
        return -1
            
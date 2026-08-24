from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #{1,1,1,2,2,3}

        count=Counter(nums)
        #{1:3,2:2,3:1}

        bucket=[[] for i in range(len(nums)+1)]

        for num,freq in count.items():

            bucket[freq].append(num)

        res=[]
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
               res.append(num)
               if len(res)==k:
                   return res
        





        
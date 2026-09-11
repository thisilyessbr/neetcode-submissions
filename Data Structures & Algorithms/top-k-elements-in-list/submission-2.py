class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        order = {}
        result = []

        for num in nums :
            if num not in order :
                order[num] = 1
            else:
                order[num] +=1

        bucket = [[] for _ in range(len(nums)+1)]

        
        for key in order :
            bucket[order[key]].append(key)
        

        for i in range(len(nums),0,-1):
            for num in bucket[i]:
              result.append(num)

            if (len(result) == k):
               return result
            

        
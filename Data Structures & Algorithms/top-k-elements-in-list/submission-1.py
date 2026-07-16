from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        r=[]
        set_list = Counter(nums)
        for key in set_list.keys():
            res.append([set_list[key], key])
        res.sort()
        # print(res)
        for i in range(len(res)):
            print(i)
            r.append(res[i][1])
        r= r[::-1]
        # print(r[:k])
        return r[:k]        
            

        
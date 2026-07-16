class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            res.append(self.prod(nums,i)
            )
        return res

    def prod(self, l,k):
        r=1
        for i in range(len(l)):
            if i != k:
                r=r*l[i]
        return r
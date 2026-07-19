class Solution:
    def maxProfit(self, p: List[int]) -> int:
        i=0
        j=1
        mp=0
        while j<len(p):

            if p[i]>=p[j]:
                i=j
                j=j+1
            else:
                mp = max(mp,p[j]-p[i])
                j=j+1
        return mp
        
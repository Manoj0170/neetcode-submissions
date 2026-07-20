class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        l=0
        res=0
        
        for r in range(len(s)):
            print(s[r],temp)
            while s[r] in temp:
                temp.remove(s[l])
                l=l+1
            temp.add(s[r])
               
                



            
            # sub=s[l:r+1]
            
            res=max(res,r-l+1)
            # print(sub)
        return res

        


        
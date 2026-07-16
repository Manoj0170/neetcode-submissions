class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        reslist = []
        while len(strs)>0:
          
            temp_list=[strs[0]]
            

            for j in range(1,len(strs)):
                if self.isana(strs[0], strs[j]) == True:
                    temp_list.append(strs[j])
              
            reslist.append(temp_list)
            for val in temp_list:
                strs.pop(strs.index(val))
            # print(s÷
        return reslist




    
    
    
    
    def isana(self, a,b):
        if sorted(list(a))==sorted(list(b)):
            return True
        else:
            return False
        
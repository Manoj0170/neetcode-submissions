class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums=list(set(nums))
        nums.sort()
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        # print(nums)
        i,j=0,1
        final_list=[]
        while True:
            # print(i,j)
            if j==len(nums):
                break
            if nums[j]-nums[i] == j-i:
                
                final_list.append(j-i+1)
                # print(final_list)
                j=j+1
            elif j-i==1:
                i+=1
                j+=1
            else:
                i=j-1
        # print(final_list)
        if final_list==[]:
            return 1
        else:
            return max(final_list)

     
            
            
        
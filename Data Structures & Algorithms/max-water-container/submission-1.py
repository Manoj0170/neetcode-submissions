class Solution:
    def findmin(self,i,j,nums):
        return min(nums[i],nums[j])


    def maxArea(self, nums: List[int]) -> int:
        max_area = 0
        i=0
        
        n= len(nums)
        j=n-1
        
        max_left = 0
        max_right=n-1
        while i<j:
            area = self.findmin(i,j,nums)*(j-i)
            max_area=max(area,max_area)
            if nums[i]<nums[j]:
                i=i+1
            else:
                j=j-1
        return max_area

            


        

        
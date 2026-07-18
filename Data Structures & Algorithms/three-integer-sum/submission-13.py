class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        final_list=[]
        for i in range(0,n-2):
            if nums[i]>0:
                break
            
            left=i+1
            right= n-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while left<right :
                current_sum = nums[i]+nums[left]+ nums[right]
                # print(current_sum)
                if current_sum<0:
                    left=left+1
                elif current_sum>0:
                    right = right-1
                else :
                    final_list.append([nums[i] , nums[left] , nums[right]])
                    right=right-1
                    left=left+1
                    while left<right and nums[left]==nums[left-1]:
                        left=left+1
                    while left<right and nums[right] == nums[right+1]:
                        right=right-1

                    # print(final_list)

            

        return final_list


        
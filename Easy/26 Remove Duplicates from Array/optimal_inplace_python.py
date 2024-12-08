class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
    
        len_nums = len(nums)
        k=1
        for i in range(1, len_nums):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k+=1
        
        return k

sol = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]

print(sol.removeDuplicates(nums))

print(nums)
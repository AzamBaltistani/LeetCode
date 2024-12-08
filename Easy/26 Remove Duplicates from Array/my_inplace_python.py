class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
    
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        extra = nums[len_nums-1] + 7
        k=1
        for i in range(len_nums - 1):
            if nums[i] == nums[i+1]:
                nums[i] = extra
            else:
                k+=1
        nums.sort() 
        
        return k

sol = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]

print(sol.removeDuplicates(nums))

print(nums)
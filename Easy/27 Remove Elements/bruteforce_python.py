class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = nums.count(val)
        
        while(count > 0):
            nums.remove(val)
            count -=1
            
        return len(nums)
    

sol = Solution()

nums = [3,2,2,3]
nums = [0,1,2,2,3,0,4,2]

val = 2

print(sol.removeElement(nums,val))

print(nums)
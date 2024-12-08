class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    

sol = Solution()

nums = [3,2,2,3]
# nums = [0,1,2,2,3,0,4,2]

val = 3

print(sol.removeElement(nums,val))

print(nums)
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        
        l = sorted(nums)
        result = []
        for num in nums:
            result.append(l.index(num))
            
        return result
        
        
sol = Solution()


nums = [8,1,2,2,3]
print(sol.smallerNumbersThanCurrent(nums))
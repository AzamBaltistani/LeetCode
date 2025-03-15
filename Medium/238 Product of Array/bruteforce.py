class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [0]*len(nums)
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                product *= nums[j]
            ans[i] = product
        return ans
    
sol = Solution()

nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
nums = [3]*10000
print(len(nums))
ans = sol.productExceptSelf(nums)

# O(n^2)
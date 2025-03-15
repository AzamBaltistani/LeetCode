class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pre = nums.copy()
        
        for i in range(1,n):
            pre[i] = pre[i]*pre[i-1]
        
        print("Pre: ", pre)
        
        suf = nums.copy()
        
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i]*suf[i+1]
        
    
        print("Suf: ", suf)
        
        ans = [0] *n
        
        for i in range(len(nums)):
            if i == 0:
                ans[i] = suf[i+1]
            elif i ==n-1:
                ans[i] = pre[i-1]
            else:
                ans[i] = pre[i-1] * suf[i+1]
        return ans
    
    
sol = Solution()


nums = [1,2,3,4]

print("Ans: ", sol.productExceptSelf(nums))


# O(N+N+N)

# O(N)
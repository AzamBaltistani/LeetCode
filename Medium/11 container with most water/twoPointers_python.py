class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        max_water = 0
        
        left, right = 0, len(height)-1
        
        for i in range(len(height)):
            
            h = min(height[left], height[right])
            w = len(height)-i-1
            
            max_water = max(max_water, h*w)
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
    


sol = Solution()

height = [1,8,6,2,5,4,8,3,7,3]
# height = [1,1]

print(f"Len of Height ({len(height)})")

print(sol.maxArea(height))
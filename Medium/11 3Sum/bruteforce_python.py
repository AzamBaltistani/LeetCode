class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in seen:
                return [seen[sub], i]
            else:
                seen[nums[i]] = i
                
        return 0.1, 0.1
        
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        threeSumSolution = []
        threeSumSeen = {}
        
        # print(f"Original sorted nums: {nums}")
        
        for i in range(len(nums)):
            curr_target = -(nums[i])
            # print(f"Target Variable {curr_target}")
            
            indx1, indx2 = self.twoSum(nums, curr_target)
            # print(f"i={i}, indx1={indx1}, indx2={indx2}")
            
            if i == indx1 or i == indx2:
                # print(f"Same index encountered")
                continue
            
            if nums[i] in threeSumSeen:
                continue
            
            if indx1 == 0.1 and indx2 == 0.1:
                # print(f"No sum found for {curr_target}")
                continue
            
            a, b, c = i, indx1, indx2
            if a > b:
                a, b = b, a
            if a > c:
                a, c = c, a
            if b > c:
                b, c = c, b
            
            # print(f"Two sum for {-curr_target}, {nums[indx1]} and {nums[indx2]}")
            threeSumSeen[nums[i]] = i
            
            
            if [nums[a], nums[b], nums[c]] in threeSumSolution:
                continue
            
            
            threeSumSolution.append([nums[a], nums[b], nums[c]])
            # threeSumSolution.append([nums[i], nums[indx1], nums[indx2]])
            
        return threeSumSolution


sol = Solution()

nums = [-1,0,1,2,-1,-4]
# nums = [1,2,-2,-1]
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]

# nums.sort()


print(sol.threeSum(nums))

print(f"Expected:\n[[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]")
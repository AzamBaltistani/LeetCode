class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        solutions = []
        
        print(nums)

        
        len_num = len(nums)
        
        for i in range(len_num):
            left = i+1
            right = len_num -1
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            
            while left < right:
                
               
                x = nums[i] + nums[left] + nums[right]
                
                if x == 0:                    
                    solutions.append([nums[i], nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    
                if x < 0:
                    left += 1
                    
                else:
                    right -= 1
                
            
            
                
                    
                
                
        return solutions

sol = Solution()
nums = [-1,0,1,2,-1,-4]
# nums = [0, 0, 0]
nums = [-2,0,1,1,2]
nums = [0,0,0,0]
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]

print(sol.threeSum(nums))

print("Expected")
print([[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]])
# print([[-2,0,2],[-2,1,1]])


# dead code


# target = -nums[i]
#             left = i+1
#             right = len(nums)-1
            
#             print(f"\nTarget : {target}")
#             while left < right:
                
#                 x = nums[left] + nums[right]
                
                
#                 if x == target:
#                     s = [nums[i], nums[left], nums[right]]
#                     if s not in solutions:
#                         solutions.append(s)
                        
                    

#                 if x < target:
#                     print(f"left increased")
#                     left += 1
                    
#                     while left < right:
#                         if nums[left] == nums[left -1]:
#                             print(f"Same detected and increased")
#                             left += 1
#                         else:
#                             break
                    
#                 else:
#                     print(f"right decreased")
#                     right -= 1
                    
#                     while left < right:
#                         if nums[left] == nums[left -1]:
#                             print(f"Same detected and decreased")
#                             left += 1
#                         else:
#                             break 
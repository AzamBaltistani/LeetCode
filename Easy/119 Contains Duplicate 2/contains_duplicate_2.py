# using hash table 

class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        table = dict()
        
        for i in range(len(nums)):
            get_value = table.get(nums[i], -1)
            if  get_value != -1 and abs(get_value - i) <= k:
                return True
            table[nums[i]] = i
        return False

sol = Solution()


nums = [1,2,3,1,2,3]
print(sol.containsNearbyDuplicate(nums, 2))
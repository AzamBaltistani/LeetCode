class Solution:
    
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        iterator = dict()
        
        for i in nums:
            iterator[i] = iterator.get(i, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        
        for key, value in iterator.items():
            freq[value].append(key)
            
        ans = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        
sol = Solution()


nums = [1,1,1,1,1,2,2,3,3,3,3]
k = 2

print(sol.topKFrequent(nums, k))
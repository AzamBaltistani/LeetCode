import heapq
class Solution:
    
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = dict()
        h = []
        heapq.heapify(h)
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            
        
        for key, value in freq.items():
            heapq.heappush(h,(-value, key))
        
        
        print(h)

        
sol = Solution()


nums = [1,1,1,1,1,2,2,3,3,3,3]
k = 2

print(sol.topKFrequent(nums, k))
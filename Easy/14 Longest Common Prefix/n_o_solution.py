class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        sorted_list = sorted(strs)
        
        start, end = sorted_list[0], sorted_list[-1]
        
        prefix = ''
        
        for i in range(min(len(start), len(end))):
            if (start[i] == end[i]):
                prefix += start[i]
            else:
                break
            
        return prefix
    
sol = Solution()

print(sol.longestCommonPrefix(["flow","flower", "flight"]))
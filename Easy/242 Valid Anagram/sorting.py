class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(s) == sorted(t) else False
    
    
sol = Solution()

s = "anagram"
t = "nagaram"
print(sol.isAnagram(s, t))
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        
        s_dict = dict()
        t_dict = dict()
        
        
        for s_ele, t_ele in zip(s,t):
            s_dict[s_ele] = s_dict.get(s_ele, 0) + 1
            t_dict[t_ele] = t_dict.get(t_ele, 0) + 1
        
        for ele in s:
            s_count = s_dict.get(ele, 0)
            t_count = t_dict.get(ele, 0)
            
            if s_count != t_count:
                return False
            
        return True
       
            

    
sol = Solution()

s = "anagram"
t = "nagaram"
print(sol.isAnagram(s, t))
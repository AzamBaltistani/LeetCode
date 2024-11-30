def lengthOfLongestSubstring(s):
    # a b c a b c b b
    
    left = 0
    seen = {}
    length = 0
    for right in range(len(s)):
        char = s[right]
        
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
            seen[char] = right
        else:
            seen[char] = right
        
        length = max(length, right - left + 1)
        # print(f"L: {left} R: {right} = Len: {length}")
    
    return length
    
word = "abcabcbb"
word = "bbbbb"
word = ""
word = "kpkwkwkew"
word = "aab"
word = "abcabcbb" 
word = "dvdf"

l = lengthOfLongestSubstring(word)
print(l)



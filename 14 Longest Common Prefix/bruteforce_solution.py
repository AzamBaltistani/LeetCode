def longestCommonPrefix(strs: list[str]) -> str:
        prefix = ''
        min_len_str = len(strs[0])
        for str in strs:
            if len(str) < min_len_str:
                min_len_str = len(str)
        
        for i in range(min_len_str):
            ch = strs[0][i]
            flag = True
            for str in strs:
                if ch != str[i]:
                    return prefix
            
            prefix += ch
        return prefix


print(longestCommonPrefix(["flow","flower", "flight"]))
# print(longestCommonPrefix(["cir","car"]))
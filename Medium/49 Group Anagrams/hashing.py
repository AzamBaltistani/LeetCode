class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashes = []
        anagrams = []
        count = -1
        for string in strs:
            d = dict()
            for s in string:
                d[s] = d.get(s, 0) + 1
            
            if d in hashes:
                ind = hashes.index(d)
                if ind < count:
                    anagrams[ind].append(string)
                else:
                    anagrams[count].append(string)
            else:
                anagrams.append([string])
                count += 1
                hashes.append(d)


        return anagrams



sol = Solution()

strs = ["eat","tea","tan","ate","nat","ba t"]
strs = [""]

print(sol.groupAnagrams(strs))
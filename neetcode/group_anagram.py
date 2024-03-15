from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        for i in range(len(strs)):
            anagrams = []
            for j in range(1, len(strs)):
                occurences_i = {}
                occurences_j = {}
                for letter in strs[i]:
                    occurences_i[letter] = occurences_i.get(letter, 0) + 1

                for letter in strs[j]:
                    occurences_j[letter] = occurences_j.get(letter, 0) + 1

                if occurences_i == occurences_j:
                    anagrams.append([strs[i], strs[j]])
            return anagrams

strs = ["eat","tea","tan","ate","nat","bat"]

print(Solution().groupAnagrams(strs))
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        occurences_s = {}
        occurences_t = {}
        for letter in s:
            occurences_s[letter] = occurences_s.get(letter, 0) + 1

        for letter in t:
            occurences_t[letter] = occurences_t.get(letter, 0) + 1

        return occurences_s == occurences_t

sol = Solution()

s = "anagram"
t = "nagaram"

print(sol.isAnagram(s,t))

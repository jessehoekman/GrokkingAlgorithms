class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = "abcdefghijklmnopqrstuvwxyz1234567890"
        res = [i for i in s if i in a]
        if res == res[::-1]:
            return True
        else:
            return False

s= "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
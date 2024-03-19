from itertools import count


class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        romandict = {
            "M" : 1000,
            "CM" : 900,
            "XC": 90,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "I": 1
        }
        
        for letter in s:
            if letter in romandict:
                return s.count(letter) * romandict.values()


s = "IIIXXX"
print(Solution().romanToInt(s))
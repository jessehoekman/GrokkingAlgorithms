from itertools import count


class Solution:
    def romanToInt(self, string: str) -> int:
        output = 0
        minus = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM" : 900,
        }
        
        plus = {"M" : 1000,
            "V": 5,          
            'X': 10,
            "L": 50,
            "C": 100,
            "D": 500,
            'I': 1
        }
        for letter in string:
            if letter in plus:
                output += plus[letter]
                string = string.replace(letter, '')
            else:
                output += minus[letter]
    
        return output


string = "MCMXCIV"
print(Solution().romanToInt(string))
from typing import List
from operator import itemgetter
 
class Solution:
    def topKFrequent(self, nums: List[int], k) -> List[int]:
        dict_count = {}
        for num in nums:
            if num in dict_count:
                dict_count[num] += 1
            else:
                dict_count[num] = 1
        sorted_counts = sorted(dict_count.items(), key = lambda item: item[1], reverse=True)
        return [num for num, count in sorted_counts[:k]]

nums = [1,1,1,2,2,3]

print(Solution().topKFrequent(nums, 2))


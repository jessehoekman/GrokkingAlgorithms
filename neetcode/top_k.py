from typing import List
import pandas as pd
class Solution:
    def topKFrequent(self, nums: List[int]) -> List[int]:
        dict_count = {}
        for i in range(len(nums)):
            dict_count[nums[i]] = nums.count(nums[i])
        return max(dict_count, key=dict_count.get)

nums = [1,1,1,2,2,3]

print(Solution().topKFrequent(nums))


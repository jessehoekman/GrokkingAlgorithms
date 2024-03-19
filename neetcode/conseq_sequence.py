class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = []
        dist = set(nums)
        arr = sorted(dist)



nums = [100, 4, 200, 1, ]
print(Solution().longestConsecutive(nums))
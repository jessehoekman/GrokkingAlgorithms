class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for j in range(len(nums)):
                for i in range(len(nums)):
                    if j != i:
                        if (nums[i] + nums[j] == target):
                            return [i,j]

target = 10
nums = [2,5,5,11]

print(Solution().twoSum(nums,target))
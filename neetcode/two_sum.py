class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        for i in range(len(nums)):

            for x in range(len(nums)):
                if ((nums[i] + nums[x]) == target):
                    return [i,x]
                else:
                    x += 1
            else: i += 1

target = 9
nums = [11,2,15,7]

print(Solution().twoSum(nums,target))
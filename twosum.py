class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            value = nums[i]
            difference = target - value
            if difference in d:
                return [i, d[difference]]
            d[value] = i
nums = [2, 7, 11, 15]
target = 9
s1 = Solution()
print(s1.twoSum(nums, target))


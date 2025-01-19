from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        paths = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in paths.keys():
                return [paths[difference], i]
            else:
                paths[nums[i]] = i
        return [];
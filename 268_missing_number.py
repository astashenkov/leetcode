"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
"""


class Solution:
    def missing_number(self, nums: List[int]) -> int:
        for num in range(len(nums)):
            if num not in nums:
                return num
        return len(nums)

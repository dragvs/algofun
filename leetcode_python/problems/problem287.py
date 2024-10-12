from typing import List


class Solution:
    """287. Find the Duplicate Number
    See here: https://leetcode.com/problems/find-the-duplicate-number/description/

    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and using only constant extra space.
    """
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0 # we can never go back to the first element -> this is a rho-shaped sequence
        fast = 0
        # Using Hare & Tortoise to find the loop
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Run it one more time to start the loop's entry point
        runner = 0
        while True:
            slow = nums[slow]
            runner = nums[runner]
            if slow == runner:
                break
        return slow

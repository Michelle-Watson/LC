# https://leetcode.com/problems/maximum-subarray/description/
# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """

        # Outer loop: starting index
        for i in range(len(nums)):
            current_sum = 0  # Start sum at zero for each subarray starting at idx1
            # Inner loop: ending index
            for j in range(i, len(nums)):
                current_sum += nums[j]

                max_sum = max(max_sum, current_sum)

        return max_sum

        """


        max_sum = float('-inf')  # Initialize to a very small number
        current_sum = 0  # Start sum at 0
        start_index = 0  # Start index of the subarray

        # Outer loop: Iterate through each element as the starting index
        for i in range(len(nums)):
            current_sum += nums[i]  # Add the current element to the current sum

            # Update max_sum if current_sum is greater
            if current_sum > max_sum:
                max_sum = current_sum

            """

            if current_sum < max_sum:
                Don't do anything, ex. 4 6 7 -1 2, even if the cur sum is lower, it's fine
                It's only if the next numbers completely negate the progress towards curr sum so far, that we would need to reset the subarr
            """

            # If current_sum becomes negative, reset the current sum and start at the next index
            if current_sum < 0:
                current_sum = 0  # Reset the sum
                start_index = i + 1  # Move start index to the next element

        return max_sum






# Test cases
test_cases = [
    # Example 1
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),

    # Example 2
    ([1], 1),

    # Example 3
    ([5, 4, -1, 7, 8], 23),

    # Additional test cases
    ([-1, -2, -3, -4], -1),  # Single negative number
    ([2, 1, 3, 4], 10),  # All positive numbers
    ([0, 0, 0, 0], 0),  # All zeros
    ([-2, -1, -3, 4, -1, 2, 1, -5, 4], 6),  # Subarray with both positive and negative values
    ([-2, 1, -3, 4, -1, 2, 1], 6)  # Another example of mix of positive and negative numbers
]

# Running the test cases
sol = Solution()
for i, (nums, expected) in enumerate(test_cases):
    result = sol.maxSubArray(nums)
    print(f"Test case {i + 1}: {'Pass' if result == expected else 'Fail'}")
    print(f"Expected: {expected}, Got: {result}")

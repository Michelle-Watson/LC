class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Your solution goes here
        max_prod = 0
        return max_prod


# Test cases to run your solution
solution = Solution()

# Example 1:
nums1 = [2, 3, -2, 4]
print("Output:", solution.maxProduct(nums1))  # Expected Output: 6

# Example 2:
nums2 = [-2, 0, -1]
print("Output:", solution.maxProduct(nums2))  # Expected Output: 0

# Additional Test Cases:
# Example 3:
nums3 = [-2, -3, 0, -2, -40]
print("Output:", solution.maxProduct(nums3))  # Expected Output: 80 (Subarray [-2, -40])

# Example 4:
nums4 = [0, 2]
print("Output:", solution.maxProduct(nums4))  # Expected Output: 2

# Example 5:
nums5 = [1, -1, 2, 3]
print("Output:", solution.maxProduct(nums5))  # Expected Output: 6 (Subarray [2, 3])

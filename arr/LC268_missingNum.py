# https://leetcode.com/problems/missing-number/submissions/1573084908/
# https://www.geeksforgeeks.org/find-the-missing-number/
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        missingSum = 0
        runningSum = 0
        expectedSum = 0
        # Your code goes here
        for i in range(n):
            runningSum += nums[i]
            expectedSum += (i+1)
        missingSum = expectedSum - runningSum
        return missingSum


# Test cases to run your solution
solution = Solution()

# Example 1:
nums1 = [3, 0, 1]
print("Output:", solution.missingNumber(nums1))  # Expected Output: 2

# Example 2:
nums2 = [0, 1]
print("Output:", solution.missingNumber(nums2))  # Expected Output: 2

# Example 3:
nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print("Output:", solution.missingNumber(nums3))  # Expected Output: 8

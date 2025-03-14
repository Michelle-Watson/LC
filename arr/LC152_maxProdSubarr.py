# https://leetcode.com/problems/maximum-product-subarray/
# https://www.geeksforgeeks.org/maximum-product-subarray/
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize variables with the first element of the array
        current_max_product = nums[0]  # This will track the maximum product at each step
        current_min_product = nums[0]  # This will track the minimum product at each step
        global_max_product = nums[0]  # This will store the overall maximum product we find

        # Start iterating from the second element since we already initialized with the first one
        for i in range(1, len(nums)):
            # If the current element is negative, swap the current_max_product and current_min_product
            # This is because multiplying a negative number can turn a negative product into a positive one
            if nums[i] < 0:
                current_max_product, current_min_product = current_min_product, current_max_product

            # Update the current_max_product and current_min_product:
            # current_max_product is the max of:
            # 1. The current number itself (nums[i])
            # 2. The product of current_max_product and nums[i]
            current_max_product = max(nums[i], current_max_product * nums[i])

            # current_min_product is the min of:
            # 1. The current number itself (nums[i])
            # 2. The product of current_min_product and nums[i]
            current_min_product = min(nums[i], current_min_product * nums[i])

            # Update the global_max_product to the larger of:
            # 1. The previous global_max_product
            # 2. The current_max_product
            global_max_product = max(global_max_product, current_max_product)

        # Return the final global_max_product, which holds the highest product we found
        return global_max_product


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

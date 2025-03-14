from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # You can implement your solution here using a hashmap (dict) or Counter


        # Placeholder for your code:
        pass


# Test Cases
def test_solution():
    sol = Solution()

    # Example 1
    nums1 = [3, 2, 3]
    print(f"Input: {nums1} => Output: {sol.majorityElement(nums1)}")  # Expected: [3]

    # Example 2
    nums2 = [1]
    print(f"Input: {nums2} => Output: {sol.majorityElement(nums2)}")  # Expected: [1]

    # Example 3
    nums3 = [1, 2]
    print(f"Input: {nums3} => Output: {sol.majorityElement(nums3)}")  # Expected: [1, 2]

    # Additional Test Cases:
    # Test Case 1
    nums4 = [1, 1, 1, 3, 3, 2, 2, 2]
    print(f"Input: {nums4} => Output: {sol.majorityElement(nums4)}")  # Expected: [1, 2]

    # Test Case 2
    nums5 = [5, 5, 5, 6, 6, 7, 7, 7, 8]
    print(f"Input: {nums5} => Output: {sol.majorityElement(nums5)}")  # Expected: [5, 7]

    # Test Case 3
    nums6 = [1, 1, 2, 2, 2, 3]
    print(f"Input: {nums6} => Output: {sol.majorityElement(nums6)}")  # Expected: [2]

    # Test Case 4 (Edge case: Empty list)
    nums7 = []
    print(f"Input: {nums7} => Output: {sol.majorityElement(nums7)}")  # Expected: []


# Running the test cases
test_solution()

from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = Counter(nums)
        print(counter)  # prints Counter Obj {}
        print(counter.items())  # view object that displays the key-value pairs (the items) of the Counter as tuples.
        # ([(3, 2), (2, 1)])
        n = len(nums)
        min_occurrence = n//3

        # Filter the keys where the value (count) is greater than min_occurrence
        result = [key for key, value in counter.items() if value > min_occurrence]

        """
        # LONG WAY
        result = []
        for key, value in counter.items():
            if value > min_occurrence:
                result.append(key)
        """

        return result

        # Using dict to count occurrences
        my_dict = {}
        res = []
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        print(my_dict)
        return res


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

# https://leetcode.com/problems/merge-intervals/description/

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Implement your solution here
        return []

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    intervals_1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print("Test case 1 - Expected: [[1, 6], [8, 10], [15, 18]]")
    print("Output:", solution.merge(intervals_1))

    # Test case 2
    intervals_2 = [[1, 4], [4, 5]]
    print("Test case 2 - Expected: [[1, 5]]")
    print("Output:", solution.merge(intervals_2))

    # Test case 3
    intervals_3 = [[1, 4], [2, 3]]
    print("Test case 3 - Expected: [[1, 4]]")
    print("Output:", solution.merge(intervals_3))

    # Test case 4
    intervals_4 = [[1, 4], [0, 2], [3, 5]]
    print("Test case 4 - Expected: [[0, 5]]")
    print("Output:", solution.merge(intervals_4))

    # Test case 5
    intervals_5 = [[1, 10], [2, 6], [8, 10], [15, 18], [19, 20]]
    print("Test case 5 - Expected: [[1, 10], [15, 18], [19, 20]]")
    print("Output:", solution.merge(intervals_5))

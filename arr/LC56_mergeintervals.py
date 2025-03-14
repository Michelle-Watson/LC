# https://leetcode.com/problems/merge-intervals/description/
# https://www.geeksforgeeks.org/merging-intervals/

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # EDGE: empty arr
        if not intervals:
            return []

        # Sort intervals based on the starting point
        intervals.sort(key=lambda x: x[0])
        # Sorting: O(n log n)

        # Initialize the result with the first interval
        res = [intervals[0]]
        print("res", res)

        # Iterating through intervals: O(n)
        for i in range(1, len(intervals)):
            # Compare the current interval with the last one in the result
            if intervals[i][0] <= res[-1][1]:  # Compare with 'end' of the last interval in the result
                # if end time of last elem in res is less then the start tiem of the interval we're checking, we need to update res
                # There's overlap, merge the intervals = update end time
                res[-1][1] = max(res[-1][1], intervals[i][1])  # Merge by updating the end time
                # end time of last res = max between end time in res and end time in current interval
            else:
                # No overlap, just add the current interval to the result
                res.append(intervals[i])

        return res

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

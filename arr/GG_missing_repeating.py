from collections import Counter
class Solution(object):
    def findMissingAndRepeating(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # The size of the array
        n = len(arr)
        runningSum = 0
        expectedSum = 0

        counter = Counter(arr)
        res = [key for key, value in counter.items() if value > 1]
        # print("res", res)
        repeating = res[0]

        # Sum of the first n natural numbers (expected sum)
        # expectedSum = (n * (n + 1)) // 2

        for i in range(n):
            runningSum += arr[i]
            expectedSum += (i + 1)
        missing = expectedSum - (runningSum - repeating)

        print (repeating, missing)

        return [repeating, missing]

# Test cases
solution = Solution()

# Test case 1
arr1 = [2, 2]
expected1 = [2, 1]
print("Expected Output for Test case 1:", expected1)
print("Test case 1 output:", solution.findMissingAndRepeating(arr1))  # Expected output: [2, 1]

# Test case 2
arr2 = [1, 3, 3]
expected2 = [3, 2]
print("Expected Output for Test case 2:", expected2)
print("Test case 2 output:", solution.findMissingAndRepeating(arr2))  # Expected output: [3, 2]

# Test case 3
arr3 = [4, 3, 6, 2, 1, 1]
expected3 = [1, 5]
print("Expected Output for Test case 3:", expected3)
print("Test case 3 output:", solution.findMissingAndRepeating(arr3))  # Expected output: [1, 5]

# Test case 4
arr4 = [6, 5, 8, 7, 1, 4, 1, 3, 2]
expected4 = [1, 9]
print("Expected Output for Test case 4:", expected4)
print("Test case 4 output:", solution.findMissingAndRepeating(arr4))  # Expected output: [1, 9]
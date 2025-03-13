# naive - O(n^2)
def subArraySum(arr, k):
    for i in range(len(arr)):
        currSum = 0
        for j in range(i, len(arr)):
            currSum += arr[j]
            if currSum == k:
                return True

    return False
# We'll be recomputing a lot of elements at the same time
# explain WHY your solution is slow, don't just say 'this is slow'
# cache? precache the sums?
# https://www.geeksforgeeks.org/check-if-a-subarray-exists-with-sums-as-a-multiple-of-k/

# optimize - O(n)


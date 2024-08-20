class Solution(object):
    def __int__(self):
        self.n = 0

    def rotate_simple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # copy array, copy will be the source of truth
        nums_copy = nums.copy()
        # It looks like you’re seeing unexpected values in nums after the rotation because nums_copy = nums doesn’t create a separate copy of the array. Instead, it just creates a reference to the same array. Thus, when you modify nums, nums_copy also gets modified, leading to unexpected results.
        print(nums_copy)

        # iterate through arr, rotating each element
        for idx, val in enumerate(nums_copy):
            print("cur idx: ", idx, "val: ", val)
            new_idx = (idx + k) % n
            print("new_idx: ", new_idx)
            nums[new_idx] = nums_copy[idx]
            print("val: ", val)

        print(n)
        print(nums)

    def rotate_optmized(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        k = k % n

        # swapping elements
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            print(f"Array after reversing from index {start} to {end}: {nums}")

        # Reverse the entire array
        reverse(0, n-1)

        # Reverse the first k elements
        reverse(0, k - 1)

        # Reverse the remaining n-k elements
        reverse(k, n - 1)

        print(nums)


test1 = Solution()
# test1.rotate_simple([1, 2, 3, 4], 2)
# test1.rotate([1, 2, 3, 4, 5, 6, 7], 2)

# ideal, in place, O1 time?
test1.rotate_optmized([1, 2, 3, 4], 2)

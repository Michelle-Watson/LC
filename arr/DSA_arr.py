# Complexity- O(n^2)
def find_subarrays(arr):
    subarrays = []
    n = len(arr)
    for start in range(n):
        for end in range(start + 1, n + 1):
            subarrays.append(arr[start:end])
    return subarrays

arr = [1, 2, 3, 4]
print(find_subarrays(arr))
# Output will be: [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]

# 2D Array: A list of lists
arr_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(arr_2d[0][1])  # Output will be 2 (first row, second element)

# 3D Array
arr_3d = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

print(arr_3d[1][0][1])  # Output will be 6


def recursive_binary_search(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return target
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)

    return recursive_binary_search(arr, target, left, mid + 1)


arr = sorted([10, 3, 6, 8, 2, 8, 2, 1, 9, 0])
target = 9
index = recursive_binary_search(arr, target, 0, len(arr) - 1)

if index != -1:
    print(f"Target {target} found at index {index}")
else:
    print("Target not found")

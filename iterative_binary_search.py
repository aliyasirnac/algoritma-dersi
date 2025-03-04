def iterative_binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [10, 30, 45, 50, 64, 150, 300, 455, 500, 765, 987]
target = 150

print(iterative_binary_search(arr, target))

import time


def sentinel_linear_search(arr, target):
    start = time.time()
    n = len(arr)
    last = arr[-1]
    arr[-1] = target
    i = 0

    while arr[i] != target:
        i += 1

    arr[-1] = last

    if i < n - 1 or arr[-1] == target:
        end = time.time()
        print(f"search time {end-start}")
        return i

    end = time.time()
    print(f"search time {end-start}")
    return -1


arr = [101, 23, 5, 3, 2, 7, 9, 34, 765, 31, 6, 8, 9, 11]
target = 7
result = sentinel_linear_search(arr, target)
print("element found at index: ", result if result != -1 else "Not found")

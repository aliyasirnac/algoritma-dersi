from time import time


def linear_search(arr, target):
    start = time()
    for i, j in enumerate(arr):
        if j == target:
            end = time()
            print(f"search time {end-start}")
            return i

    end = time()
    print(f"search time {end-start}")
    return -1


arr = [101, 23, 5, 3, 2, 7, 9, 34, 765, 31, 6, 8, 9, 11]
target = 2
result = linear_search(arr, target)
print("element found at index: ", result if result != -1 else "Not found")

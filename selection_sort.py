def selection_sort(arr):
    for i in range(len(arr) - 1):
        smallest_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]


arr = [64, 25, 12, 22, 11]

print("Unsorted array is:", arr)

selection_sort(arr)

print("Sorted array is:", arr)

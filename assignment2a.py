def recursive_binary_search(arr, target, left=0, right=None, count=0):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1, count 

    # Orta elemanın index'i
    mid = (left + right) // 2
    # Iterasyon sayısını artır
    count += 1
    
    if arr[mid] == target:
        # Hedef bulundu
        return mid, count
    elif arr[mid] < target:
        # Hedef sağdaki alt dizide
        return recursive_binary_search(arr, target, mid + 1, right, count)

    # Hedef soldaki alt dizide
    return recursive_binary_search(arr, target, left, mid - 1, count)


arr = [1,2,3,4,5,6,7]
target = int(input("Enter the target: "))
index, count = recursive_binary_search(arr, target)

if index != -1:
    print(f"Target {target} found at index {index} in {count} iterations")
else:
    print("Target not found")

def count_even_recursive(arr):
    if not arr:
        return 0
    head = arr[0]
     # İlk eleman çiftse 1 ekler, değilse 0 ekler ve kalan liste için fonksiyonu tekrar çağırır.
    return (1 if head % 2 == 0 else 0) + count_even_recursive(arr[1:])

even_count = count_even_recursive(arr)
print(f"2c - Total even numbers: {even_count}")
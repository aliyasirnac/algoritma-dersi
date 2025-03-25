def merge(arr, p, q, r):
    n1 = q - p + 1 # Sol alt dizi uzunluğu
    n2 = r - q # Sağ alt dizi uzunluğu

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    # Sol ve sağ alt dizileri doldur
    for i in range(n1):
        L[i] = arr[p + i] # p'den q'ya kadar olan elemanlar

    for j in range(n2):
        R[j] = arr[q + j + 1] # q+1'den r'ye kadar olan elemanlar

    # Sonsuz sentineller, yani dizinin sonuna gelindiğinde karşılaştırma yapabilmek için kullanılır
    L[n1] = float("inf")
    R[n2] = float("inf")

    i = j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)

# 1a - Tüm elemanları 2 ile çarp ve sırala
arr_1a = [4, 1, 6, 10, 3, 7, 2]
print(f"1a - Orijinal dizi: {arr_1a}")
for i in range(len(arr_1a)):
    arr_1a[i] *= 2
merge_sort(arr_1a, 0, len(arr_1a) - 1)
print(f"1a - Tüm elemanlar ikiyle çarpıldıktan sonra sıralı dizi: {arr_1a}")

# 1b - Sadece ilk elemanı 2 ile çarp ve sırala
arr_1b = [4, 1, 6, 10, 3, 7, 2]
print(f"\n1b - Orijinal dizi: {arr_1b}")
arr_1b[0] *= 2
merge_sort(arr_1b, 0, len(arr_1b) - 1)
print(f"1b - Sadece ilk eleman ikiyle çarpıldıktan sonra sıralı dizi: {arr_1b}")

# 1c - Merge sort sonrası çarpım tablosu
arr_1c = [4, 1, 6, 10, 3, 7, 2]
print(f"\n1c - Orijinal dizi: {arr_1c}")
merge_sort(arr_1c, 0, len(arr_1c) - 1)
print(f"1c - Sıralı dizi: {arr_1c}")

def print_multiplication_table(arr):
    print("\n1c - Çarpım Tablosu:")
    for i in arr:
        row = [i * j for j in arr]
        print(row)

print_multiplication_table(arr_1c)
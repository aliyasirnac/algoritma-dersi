def friends(arr):
    i=0
    while i<len(arr):
        print(arr)
        
        if i == 0:
            i+=1
        elif arr[i] >= arr[i-1]:
            i+=1
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]

    return arr

arr = ["Ross", "Joey", "Rachel"]
friends(arr)
print(arr)
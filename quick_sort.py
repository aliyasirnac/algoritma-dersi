def quick_sort(arr): #sequnce is our array parameter
    length=len(arr) # length is number of elemenys in arr
    if length<=1:
        return arr
    pivot=arr.pop() # pop removes and return the element index if it has empy paranthesis it removes the lastelement of the array and return it
   
    left = [x for x in arr if x <= pivot]
    right = [x for x in arr if x > pivot]
 
    return quick_sort(left)+[pivot]+quick_sort(right)
print(quick_sort([0,3,2,5,9,8,7]))
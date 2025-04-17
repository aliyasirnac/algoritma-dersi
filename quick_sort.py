def quick_sort(sequence): #sequnce is our array parameter
    length=len(sequence) # length is number of elemenys in sequence
    if length<=1:
        return sequence
    else:
        pivot=sequence.pop() # pop removes and return the element index if it has empy paranthesis it removes the lastelement of the array and return it

    items_greater=[]
    items_lower=[]
   
    for item in sequence:
        if item>pivot:
            items_greater.append(item) # append adds the item to array
        else:
            items_lower.append(item)
    return quick_sort(items_lower)+[pivot]+quick_sort(items_greater)
print(quick_sort([0,3,2,5,9,8,7]))
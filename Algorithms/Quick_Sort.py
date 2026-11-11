def quick_sort(arr):
    
    if not arr:
        return []
    
    
    pivot = arr[0]
    
    less_than = []
    equal_to = []
    greater_than = []
    
    
    for num in arr:
        if num < pivot:
            less_than.append(num)
        elif num == pivot:
            equal_to.append(num)
        else:
            greater_than.append(num)
            
    
    return quick_sort(less_than) + equal_to + quick_sort(greater_than)


qs = quick_sort([20,3,14,1,5])
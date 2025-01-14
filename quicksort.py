
def quick_sort_lomuto(arr, key_idx, i, f, dec=False):
    if(f>i):
        # partition into two parts
        p = partition_lomuto(arr, key_idx, i, f, dec)
        # make recursion for both parts 
        quick_sort_lomuto(arr, key_idx, i, p-1, dec)
        quick_sort_lomuto(arr, key_idx, p+1, f, dec)

def partition_lomuto(arr, key_idx, left, right, dec):
    pivot = float(arr[left][key_idx])
    storeIndex = left+1 # index of smaller element
    for i in range(left+1, right+1):
        # if the element is smaller than or equal to the pivot
        if (not dec and float(arr[i][key_idx]) < pivot) or (dec and float(arr[i][key_idx]) > pivot):
            #swap values
            swap(arr, i, storeIndex)
            storeIndex+=1
    swap(arr, left, storeIndex-1)
    return storeIndex-1

def swap(arr, a, b):
    tmp = arr[a]
    arr[a]=arr[b]
    arr[b] = tmp



def quick_sort_lomuto(arr, i, f, trocas=0, recursoes=0):
    recursoes +=1
    if(f>i):
        # partition into two parts
        p, trocas = partition_lomuto(arr, i, f, trocas)
        # make recursion for both parts 
        trocas, recursoes = quick_sort_lomuto(arr, i, p-1, trocas, recursoes)
        trocas, recursoes = quick_sort_lomuto(arr, p+1, f, trocas, recursoes)
    return trocas, recursoes

def quick_sort_hoare(arr, i, f, trocas=0, recursoes=0):
    recursoes += 1
    if(f>i):
        # partition into two parts
        p, trocas = partition_hoare(arr, i, f, trocas)
        # make recursion for both parts 
        trocas, recursoes = quick_sort_hoare(arr, i, p-1, trocas, recursoes)
        trocas, recursoes = quick_sort_hoare(arr, p+1, f, trocas, recursoes)
    return trocas, recursoes

def partition_lomuto(arr, left, right, trocas):
    chave = arr[left]
    storeIndex = left+1 # index of smaller element
    for i in range(left+1, right+1):
        # if the element is smaller than or equal to the pivot
        if(arr[i] < chave):
            #swap values
            swap(arr, i, storeIndex)
            trocas+=1
            storeIndex+=1
    swap(arr, left, storeIndex-1)
    trocas+=1
    return storeIndex-1, trocas

def partition_hoare(arr, left, right, trocas):
    chave = arr[left]
    i = left
    j = right + 1
    
    while True:
        i += 1
        while (arr[i] <= chave and i < right):
            i += 1
        
        j -= 1
        while (arr[j] >= chave and j > left):
            j -= 1

        if i >= j:
            break        
        swap(arr, i, j)
        trocas += 1

    swap(arr, left, j)
    trocas += 1

    return j, trocas
    
def swap(arr, a, b):
    tmp = arr[a]
    arr[a]=arr[b]
    arr[b] = tmp


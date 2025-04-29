#Reverse Array (Two Pointers)



arr = [3,4,5,2,1,5,6,4,3]

#reverse arr function

def reverse_arr(arr):
    low = 0
    high = len(arr)-1
    while low<=high:
        tmp = arr[low]
        arr[low] = arr[high]
        arr[high] = tmp
        low+=1
        high -=1
    return arr

print(reverse_arr(arr))

#Check is array is sorted
arr_sorted = [1,5,3,4,2]
def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
        return True
        
def can_be_sorted_in_one_swap(arr):
    bad = []
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            bad.append(i)
    if len(bad) == 0:
        return True
    if len(bad)>2:
        return False
    bad_index = bad[0]
    bad_index_1 = bad[-1]+1 
    arr[bad_index], arr[bad_index_1] = arr[bad_index_1], arr[bad_index]
    print(is_sorted(arr))
    print(arr)
    return(True)


print(can_be_sorted_in_one_swap(arr_sorted))
        

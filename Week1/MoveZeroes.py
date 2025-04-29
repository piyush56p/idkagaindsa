arr = [0,1,0,3,12]


def move_zeroes(arr):
    index_save = []
    i =0
    while i<len(arr):
        if arr[i] == 0:
            arr.pop(i)
            index_save.append(i)
        else:
            i+=1
    zeroes_to_append = [0]*len(index_save)
    arr.extend(zeroes_to_append)
    return arr
    #This is not a good apporaoch, takes extra memory 
    
def better_move_zeros(arr):
    #two pointer appraoch
    low = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[low] = arr[i]
            low+=1 
    while(low<len(arr)):
        arr[low] = 0
        low+=1
    return arr
print(better_move_zeros(arr))

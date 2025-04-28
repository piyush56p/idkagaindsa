#Min and max elemtn in an arr, also the seconds largest or seconds mininum



arr = [3,4,3,2,4,5,6,4,3]
#Convert it to set 
arr_set = set(arr)
print(arr_set)


max_val = arr[0]
min_val = arr[0]
#maximum element
for i in range(len(arr)):
    if arr[i]>max_val:
        max_val = arr[i]
    else:
        continue
#minimum element
for i in range(len(arr)):
    if arr[i]<min_val:
        min_val = arr[i]
    else:
        continue
    
#Second largest element
first = second = float('-inf')
for i in range(len(arr)):
    if arr[i] > first:
        second = first
        first = arr[i]
    elif first>arr[i]>second:
        second = num
    else:
        continue

#Second Smallest element
first = second_small = float('inf')
for i in range(len(arr)):
    if arr[i] < first:
        second_small = first
        first = arr[i]
    elif first<arr[i]<second_small:
        second_small = arr[i]
    else:
        continue
    


print("Second Smalles", second_small)
print("Second Largest", second)
print("Minimum value", min_val)
print("Maximum value",max_val)

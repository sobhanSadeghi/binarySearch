def binary_search(arr,target,low,high):
    if low>high:
        return -1

    mid=(low+high)//2

    if arr[mid] == target:
        return mid 

    elif target<arr[mid]:
        return binary_search(arr,target,low,mid-1)      

    elif target> arr[mid]:
        return binary_search(arr,target,mid+1,high)
    
    else:
        return " not found"



a=[1, 3,4 ,5,6,9,10,20]

tar=4

print(f'target in index {binary_search(a,tar,0,len(a))}')
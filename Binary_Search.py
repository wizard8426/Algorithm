data = [1,2,3,4,5,6,7,8,9]

def binary_search(data, target, low, high):

    if low > high:
        return False
    else:
        mid = round((low+high)/2)
        if target==data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data,target,low,mid-1)
        else:
            return binary_search(data,target,mid+1,high)

print(binary_search(data, 2, 0, 9))



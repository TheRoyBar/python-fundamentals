def binary_search(lst, target):
    low = 0
    high = len(lst)
    mid = int((low+high)/2)

    if (lst[mid] == target):
        return mid
    elif (lst[mid] > target):
        high = mid-1
    else:
        low = mid+1
    
    return -1


def selection_sort(arr):

    for i in range(0,len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if (arr[j] < arr[min_index]):
                min_index = j
        
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i-1
        key = arr[i]
        while(j>=0 and arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def main():
    lst = [1,4,5,6,7,28,9,11,67]
    target = 70

    print("Index is: ", binary_search(lst,target))

    arr = [23,21,434,886,4,32,444]
    arr = insertion_sort(arr)

    print("Displaying all the elements in the SORTED Array: ")
    for i in arr:
        print(i)

main()


                    
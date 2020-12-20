def bubble_sort(arr):
    swapped = True
    while swapped is True:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    return arr

arr = [5, 6, 7, 0, 45, 9, 4]
print(bubble_sort(arr))
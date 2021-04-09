def MergeSort(arr):
    length = len(arr)
    if length>1:
        half = int(length/2)
        left_arr = arr[0:half-1]
        right_arr = arr[half:length-1]
        MergeSort(left_arr)
        MergeSort(right_arr)
        j = half
        i = 0
        for k in range(length):
            if i < half and j < length:
                if left_arr[i] > right_arr[j]:
                    arr[k] = right_arr[j]
                    j += 1
                else:
                    arr[k] = left_arr[i]
                    i += 1


    return arr

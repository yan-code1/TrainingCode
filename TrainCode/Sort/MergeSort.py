import numpy as np
def __merge(arr,start,mid,end):
    aux = arr[start:end+1]
    i = start
    j = mid + 1
    k = start
    while k <= end:
        if i > mid:
            arr[k] = aux[j-start]
            j += 1

        elif j > end:
            arr[k] = aux[i-start]
            i += 1

        elif aux[i - start] < aux[j - start]:
            arr[k] = aux[i-start]
            i += 1

        else :
            arr[k] = aux[j-start]
            j += 1
        k += 1
    #注意千万注意优先判断数组越界，否则报错像下面一样。
    # for k in range(end - start + 1 ):
    #     if (j > end or aux[i - start] < aux[j - start]):
    #         arr[k+start] = aux[i-start]
    #         i += 1
    #     elif (i > mid or aux[i - start] > aux[j - start] ):
    #         arr[k+start] = aux[j-start]
    #         j += 1
    #     else:
    #         return

def __mergeSort(arr,start,end):
    if  start >= end:
        return
    #这里mid注意下
    mid = int((end + start)/2)
    __mergeSort(arr, start, mid)
    __mergeSort(arr, mid+1, end)
    __merge(arr, start, mid, end)

def mergeSort(arr):
    __mergeSort(arr, 0, len(arr)-1)




# def MergeSort(arr):
#     length = len(arr)
#     if length>1:
#         half = int(length/2)
#         left_arr = arr[0:half-1]
#         right_arr = arr[half:length-1]
#         MergeSort(left_arr)
#         MergeSort(right_arr)
#         j = half
#         i = 0
#         for k in range(length):
#             if i < half and j < length:
#                 if left_arr[i] > right_arr[j]:
#                     arr[k] = right_arr[j]
#                     j += 1
#                 else:
#                     arr[k] = left_arr[i]
#                     i += 1
#
#
#     return arr

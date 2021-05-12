import numpy as np
import math
#返回排好序的一个元素的索引
# arr = [start],(start,partIdx],[partIdx+1,end-1]
def _partition(arr,start,end):
     flagCmp = arr[start]
     partIdx = start
     index = start
     while(index <= end):
         if arr[index] < flagCmp:
             temp = arr[partIdx+1]
             arr[partIdx+1] = arr[index]
             arr[index] = temp

             partIdx += 1
         index += 1
     temp = arr[start]
     arr[start] = arr[partIdx]
     arr[partIdx] = temp
     return partIdx
def _quickSort(arr,start,end):
    if start >= end:
        return

    pIdx = _partition(arr,start,end)
    _quickSort(arr,start,pIdx-1)
    _quickSort(arr,pIdx+1,end)

def quickSort(arr):
    _quickSort(arr,0,len(arr)-1)

from Sort.MergeSort import mergeSort
from Sort.QuickSort import quickSort
import random
import sys
sys.setrecursionlimit(100000)
def seqGenerate(length,randomNum):
    array = [i for i in range(length)]
    index = random.sample(array, randomNum)
    temp_index = index[:]
    random.shuffle(temp_index)
    count = 0
    for i in index:
        array[i] = temp_index[count]
        count += 1
    return array

def main():
    arr = seqGenerate(10,5)
    print(arr)
    #mergeSort(arr)
    quickSort(arr)
    print(arr)

if __name__ == "__main__":
    main()
from Sort.MergeSort import MergeSort
import random
def main():
    array = [i for i in range(10)]
    index = random.sample(array,5)
    temp_index = index[:]
    random.shuffle(temp_index)
    for i in index:
        count = 0
        array[i] = temp_index[count]
        count += 1
    print(array)
    print(MergeSort(array))

if __name__ == "__main__":
    main()
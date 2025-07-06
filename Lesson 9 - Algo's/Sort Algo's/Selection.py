"""
    Fetch the smallest element first in the array or data structure.
    After swap numbers between their position for each iteration.

    Time Complexity:
        1. Worst Case: O(n ^ 2) - quadratic time
        
    Best for small data
    Bad for huge data
"""

def SelectionSort(array):
    for i in range(0,len(array) - 1):
        min:int = i

        for j in range(i + 1,len(array)):
            if array[min] > array[j]:
                min = j

        temp:int = array[i]
        array[i] = array[min]
        array[min] = temp
    

unsorted_arr = [9,4,8,7,2,4,1]
SelectionSort(unsorted_arr)
print(unsorted_arr)
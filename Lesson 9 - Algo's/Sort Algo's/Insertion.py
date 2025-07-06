"""
    Time Complexity : O(n ^ 2)
"""

def insertion_sort(array):
    for i in range(1, len(array)):
        temp:int = array[i]
        j = i - 1

        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = temp

array = [4,3,6,5,8,9,7]
insertion_sort(array)
print(array)
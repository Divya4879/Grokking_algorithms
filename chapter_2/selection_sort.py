# Selection Sort Algorithm

def selectionSortInPlace(arr):
    for i in range(len(arr)):
        smallest_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

print(selectionSortInPlace([5, 3, 6, 2, 10]))
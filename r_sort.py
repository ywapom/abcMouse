

def reverse_sort(arr):
    """ sort and reverse the array without .sort method """
    reverse_sorted = []

    while arr:
        max = arr[0]
        for item in arr:
            if item > max:
                max = item
        reverse_sorted.append(max)
        arr.remove(max)
    return reverse_sorted


arr = [1, 6, 10, 9, 8, 2, 4]
print(reverse_sort(arr))

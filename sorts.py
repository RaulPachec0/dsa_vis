def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n- i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print("Swapping:", arr)
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        print("Merging", arr)


if __name__ == "__main__":
    print("Bubble Sort")
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array:", arr)
    sorted_arr = bubble_sort(arr.copy())
    print("Sorted Array:", sorted_arr, "\n")

    print("Merge Sort")
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array:", arr)
    merge_sort(arr)
    print("Sorted Array", arr, "\n")

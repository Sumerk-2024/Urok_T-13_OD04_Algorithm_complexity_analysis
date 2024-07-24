# O(1) - Константная сложность означает, что время выполнения алгоритма
# не зависит от размера входных данных.


def get_element(arr, index):
    return arr[index]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_element(arr, 4))  # выведет 5


# O(n) - Линейная сложность алгоритма означает, что время выполнения алгоритма
# пропорционально количеству входных данных.


def line_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
print(line_search(arr, 30))  # выведет 2
print(line_search(arr, 60))  # выведет -1


# O(log n) = Логарифмическая сложность означает, что время выполнения алгоритма
# увеличивается логарифмически с увеличением размера входных данных.
# Логарифм — это количество шагов, которые требуется проделать для получения результата.


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [0, 10, 15, 20, 30, 35, 40, 50, 55, 60, 70, 75, 80, 90, 95, 100]
print(binary_search(arr, 70))  # выведет 10
print(binary_search(arr, 25))  # выведет -1

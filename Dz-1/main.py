# Код визуализирует практические результаты (время выполнения и использование памяти) и
# теоретические оценки для каждого алгоритма сортировки: пузырьковую сортировку,
# быструю сортировку, сортировку выбором, сортировку вставками и сортировку слиянием.


import time
import tracemalloc
import matplotlib.pyplot as plt
import numpy as np
import random


# Функции сортировки
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Функция для измерения времени и памяти
def measure_performance(sort_function, arr):
    start_time = time.time()  # Начало измерения времени
    tracemalloc.start()  # Начало отслеживания распределения памяти
    sort_function(arr.copy())  # Копируем массив и выполняем сортировку
    current, peak = tracemalloc.get_traced_memory()  # Получаем текущее и пиковое использование памяти
    tracemalloc.stop()  # Останавливаем отслеживание распределения памяти
    end_time = time.time()  # Конец измерения времени
    return end_time - start_time, peak  # Возвращаем время выполнения и пиковое использование памяти


# Создаем массивы разных размеров
sizes = [10, 50, 100, 200, 500, 1000]  # Размеры массивов для тестирования
times_bubble = []
times_quick = []
times_selection = []
times_insertion = []
times_merge = []
memory_bubble = []
memory_quick = []
memory_selection = []
memory_insertion = []
memory_merge = []

# Измеряем производительность каждого алгоритма сортировки для каждого размера массива
for size in sizes:
    arr = [random.randint(-1000, 1000) for _ in range(size)]  # Генерируем случайный массив заданного размера

    # Пузырьковая сортировка
    t, m = measure_performance(bubble_sort, arr)
    times_bubble.append(t)
    memory_bubble.append(m)

    # Быстрая сортировка
    t, m = measure_performance(quick_sort, arr)
    times_quick.append(t)
    memory_quick.append(m)

    # Сортировка выбором
    t, m = measure_performance(selection_sort, arr)
    times_selection.append(t)
    memory_selection.append(m)

    # Сортировка вставками
    t, m = measure_performance(insertion_sort, arr)
    times_insertion.append(t)
    memory_insertion.append(m)

    # Сортировка слиянием
    t, m = measure_performance(merge_sort, arr)
    times_merge.append(t)
    memory_merge.append(m)

# Построение графиков
plt.figure(figsize=(14, 8))

# График времени выполнения
plt.subplot(2, 2, 1)
plt.plot(sizes, times_bubble, label='Bubble Sort', marker='o')
plt.plot(sizes, times_quick, label='Quick Sort', marker='o')
plt.plot(sizes, times_selection, label='Selection Sort', marker='o')
plt.plot(sizes, times_insertion, label='Insertion Sort', marker='o')
plt.plot(sizes, times_merge, label='Merge Sort', marker='o')
plt.xlabel('Размер массива')
plt.ylabel('Время выполнения (секунды)')
plt.title('Время выполнения алгоритмов сортировки')
plt.legend()
plt.grid(True)
plt.yscale('log')  # Логарифмическая шкала для оси Y для лучшего сравнения

# График использования памяти
plt.subplot(2, 2, 2)
plt.plot(sizes, memory_bubble, label='Bubble Sort', marker='o')
plt.plot(sizes, memory_quick, label='Quick Sort', marker='o')
plt.plot(sizes, memory_selection, label='Selection Sort', marker='o')
plt.plot(sizes, memory_insertion, label='Insertion Sort', marker='o')
plt.plot(sizes, memory_merge, label='Merge Sort', marker='o')
plt.xlabel('Размер массива')
plt.ylabel('Используемая память (байты)')
plt.title('Использование памяти алгоритмами сортировки')
plt.legend()
plt.grid(True)
plt.yscale('log')  # Логарифмическая шкала для оси Y для лучшего сравнения

# График теоретической временной сложности
plt.subplot(2, 2, 3)
n_values = np.array(sizes)
plt.plot(sizes, n_values ** 2, label='O(n^2)', linestyle='--')
plt.plot(sizes, n_values * np.log2(n_values), label='O(n log n)', linestyle='--')
plt.xlabel('Размер массива')
plt.ylabel('Теоретическая временная сложность')
plt.title('Теоретическая временная сложность алгоритмов сортировки')
plt.legend()
plt.grid(True)
plt.yscale('log')  # Логарифмическая шкала для оси Y для лучшего сравнения

# График теоретической пространственной сложности
plt.subplot(2, 2, 4)
plt.plot(sizes, [1] * len(sizes), label='O(1)', linestyle='--')
plt.plot(sizes, np.log2(n_values), label='O(log n)', linestyle='--')
plt.plot(sizes, n_values, label='O(n)', linestyle='--')
plt.xlabel('Размер массива')
plt.ylabel('Теоретическая пространственная сложность')
plt.title('Теоретическая пространственная сложность алгоритмов сортировки')
plt.legend()
plt.grid(True)
plt.yscale('log')  # Логарифмическая шкала для оси Y для лучшего сравнения

plt.tight_layout()  # Оптимизация расположения графиков
plt.show()

import random


def bubble_sort(lst, count_swap=False):
    n, cnt = len(lst), 0
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                cnt += 1
    if count_swap:
        return cnt
    return lst


def rock_sort(lst, count_swap=False):
    n, cnt = len(lst), 0
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                cnt += 1
    if count_swap:
        return cnt
    return lst


def select_sort(lst, count_swap):
    n, cnt = len(lst), 0
    for i in range(n - 1):
        mn = i
        for j in range(i + 1, n):
            if lst[j] < lst[mn]:
                mn = j
        lst[i], lst[mn] = lst[mn], lst[i]
        cnt += 1
    if count_swap:
        return cnt
    return lst


def insertion_sort(lst, count_swap):
    n, cnt = len(lst), 0
    for i in range(1, n):
        cur = lst[i]
        j = i - 1
        while j >= 0:
            if cur < lst[j]:
                lst[j + 1] = lst[j]
                lst[j] = cur
                j -= 1
                cnt += 1
            else:
                break
    if count_swap:
        return cnt
    return lst


def quick_sort(lst):
    global cnt
    cnt += 1
    n = len(lst)
    if len(set(lst)) <= 1:
        return lst
    else:
        mid = random.choice(lst)
        left = [x for x in lst if x < mid]
        right = [x for x in lst if x >= mid]
        return quick_sort(left) + quick_sort(right)


def merge_sort(lst):
    global cnt
    cnt += 1
    n = len(lst)
    if n <= 1:
        return lst
    else:
        left = merge_sort(lst[:(n // 2)])
        right = merge_sort(lst[(n // 2):])
        return merge(left, right)


def merge(left, right):
    result = []
    il, ir, lenl, lenr = 0, 0, len(left), len(right)
    while il < lenl and ir < lenr:
        if left[il] <= right[ir]:
            result.append(left[il])
            il += 1
        else:
            result.append(right[ir])
            ir += 1
    return result + left[il:] + right[ir:]


def heapify(lst, n, i):
    largest = i
    il = 2 * i + 1
    ir = 2 * i + 2
    if il < n and lst[i] < lst[il]:
        largest = il
    if ir < n and lst[largest] < lst[ir]:
        largest = ir
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)


def heapSort(arr, count_swap=False):
    lst = arr.copy()
    n = len(lst)
    for j in range(n, -1, -1):
        heapify(lst, n, j)
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
    if count_swap:
        return cnt
    return lst


plst = [[random.randint(1, 1000) for i in range(1000)] for i in range(1000)]
sm = 0
for lst in plst:
    cnt = 0
    quick_sort(lst)
    sm += cnt
# print(plst[0])
# print('quick')
# print(sm/1000)
# sm = 0
# for lst in plst:
#     cnt = 0
#     merge_sort(lst)
#     sm+=cnt
# print(plst[0])
# print('merge')
# print(sm/1000)
print(sum(map(lambda t: bubble_sort(t, count_swap=True), plst)) / 1000)

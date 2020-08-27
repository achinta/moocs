# Uses python3
import sys
import random

def partition3(a, l, r, debug):
    #write your code here
    if debug:
        print(f'sorting {a[l:r+1]}')
    pivot_element = a[l]
    small_end_idx = l
    same_end_idx = small_end_idx
    for current_idx in range(l+1, r+1):
        if a[current_idx] < pivot_element:
            small_end_idx += 1
            same_end_idx += 1
            a[current_idx], a[same_end_idx] = a[same_end_idx], a[current_idx]
            a[same_end_idx], a[small_end_idx] = a[small_end_idx], a[same_end_idx]
        elif a[current_idx] == pivot_element:
            same_end_idx += 1
            a[current_idx], a[same_end_idx] = a[same_end_idx], a[current_idx]
    a[l], a[small_end_idx] = a[small_end_idx], a[l]
    return small_end_idx, same_end_idx

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r, debug=False):
    if l >= r:
        return
    # k = random.randint(l, r)
    # a[l], a[k] = a[k], a[l]
    #use partition3
    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1);
    # randomized_quick_sort(a, m + 1, r);

    small_end_idx, same_end_idx = partition3(a, l, r, debug)
    randomized_quick_sort(a, l, small_end_idx - 1, debug);
    randomized_quick_sort(a, same_end_idx + 1, r, debug);


def test_quick_sort(num_tests):
    for idx in range(num_tests):
        n = random.randint(4,9)
        a = random.choices(range(0, n+10), k=n)
        a_org = a.copy()
        randomized_quick_sort(a, 0, n - 1)
        py_sorted = sorted(a)
        if py_sorted != a:
            print('\n', a_org, py_sorted, a)
            randomized_quick_sort(a, 0, n - 1,debug=True )

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

    # test_quick_sort(1000)

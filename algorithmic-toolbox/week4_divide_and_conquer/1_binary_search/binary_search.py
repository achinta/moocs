# Uses python3
import sys
import logging

def binary_search(a, x):
    left, right = 0, len(a)
    if left == right:
        return -1
    mid = left + (right-left)//2
    # print(f'\n searching for {x} in {a}. mid is {mid} with mid-value - {a[mid]}')
    if a[mid] == x:
        return mid
    if a[mid] > x:
        return binary_search(a[left:mid], x)
    else:
        result = binary_search(a[mid+1:right],x)
        if result != -1:
            result += mid + 1
        return result

def binary_search2(a, x):
    low, high = 0, (len(a) - 1)
    while low <= high:
        mid = low + (high-low)//2

        if a[mid] == x:
            return mid
        elif a[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    if low > high:
        return -1



def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search2(a, x), end=' ')
        # binary_search(a, x)

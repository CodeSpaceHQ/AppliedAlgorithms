
def partition(s, begin, end):
    # Lomuto partition scheme worst case O(n^2)
    pivot = end
    pivot_holder_index = begin
    for i in range(begin, end):
        if s[i][1] < s[pivot][1]:
            s[i], s[pivot_holder_index] = s[pivot_holder_index], s[i]
            pivot_holder_index += 1
    s[pivot_holder_index], s[end] = s[end], s[pivot_holder_index]
    return pivot_holder_index


def quick_sort(s, begin, end):
    # quicksort
    if begin < end:
        pivot = partition(s, begin, end)
        # sort sub array on the left
        quick_sort(s, begin, pivot - 1)
        # sort sub array on the right
        quick_sort(s, pivot + 1, end)
    return s


def schedule(set_of_intervals):
    # Order the intervals by finish time
    set_of_intervals = quick_sort(set_of_intervals, 0, len(set_of_intervals) - 1)

    n = len(set_of_intervals)
    f = -1
    solution = []
    for i in range(0, n):
        if set_of_intervals[i][0] >= f:
            solution.append(set_of_intervals[i])
            f = set_of_intervals[i][1]
    return solution



def main():
    set_of_intervals = [(1, 3),(2, 3), (4, 5), (1, 4), (6, 9)]
    print(schedule(set_of_intervals))


if __name__ == '__main__':
    main()
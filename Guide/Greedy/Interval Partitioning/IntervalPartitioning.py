def partition(s, begin, end):
    # Lomuto partition scheme worst case O(n^2)
    # this version of partition may not be the most efficient in
    # terms of edge cases - but will do for our purpose of demonstration.
    pivot = end
    pivot_holder_index = begin
    for i in range(begin, end):
        if s[i][0] < s[pivot][0]:
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


def adjust(start, released, occupied, R):
    if not R:
        return released, occupied
    else:
        for i in occupied:
            if R[i][-1][-1] < start:
                released.append(i)
                occupied.remove(i)
        return released, occupied


def interval_partition(set_of_jobs):
    released = []
    occupied = []
    R = []
    set_of_jobs = quick_sort(set_of_jobs, 0, len(set_of_jobs) -1)

    for j in set_of_jobs:
        released, occupied = adjust(j[0], released, occupied, R)
        if released:
            m = released[0]
        else:
            m = len(R)
            R.append([])
        occupied.append(m)
        R[m].append(j)
    return R


def main():
    jobs = [(1, 3), (2, 4), (4, 5)]
    print(interval_partition(jobs))

if __name__ == '__main__':
    main()
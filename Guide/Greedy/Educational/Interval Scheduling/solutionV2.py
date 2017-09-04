def partition(s, begin, end):
    """
    Partially sort an array using a pivot value. Everything to the 
    left of the pivot will be less than the pivot. Everything to the right
    will be greater than the pivot.
    :param s: the array to sort
    :param begin: the beginning of the section of the array to sort
    :param end: the end of the section of the array to sort
    :return: the array with sorted section begin-end
    """
    pivot = end  # set the pivot to the end of the array
    pivot_holder_index = begin  # place holder for where the pivot will end up
    for i in range(begin, end):
        if s[i][1] < s[pivot][1]:  # if s[i] < s[pivot]
            # switch s[i] and pivot place holder
            s[i], s[pivot_holder_index] = s[pivot_holder_index], s[i]
            pivot_holder_index += 1  # increase pivot place holder

    # finally, put pivot in its placeholder
    s[pivot_holder_index], s[end] = s[end], s[pivot_holder_index]
    return pivot_holder_index


def quick_sort(s, begin, end):
    """
    Quick sort 
    :param s: the array to sort
    :param begin: the beginning of the array
    :param end: the ending of the array
    :return: the sorted array
    """
    # Quick sort
    if begin < end:
        pivot = partition(s, begin, end)  # find a pivot place
        quick_sort(s, begin, pivot - 1)  # recursive sort sub array on the left
        quick_sort(s, pivot + 1, end)  # recursive sort sub array on the right
    return s


def interval_schedule(set_of_intervals):
    """
    Schedule a set of intervals so that the most requests get scheduled, there
    are no overlapping requests, and the schedule is optimal
    :param set_of_intervals: the set of requests
    :return: an optimal schedule
    """
    # Order the intervals by finish time
    requests = quick_sort(set_of_intervals, 0, len(set_of_intervals) - 1)

    last_finish = -1  # initialize the last finish time
    schedule = []  # the resulting schedule
    for r in requests:
        if r[0] >= last_finish:
            schedule.append(r)  # add to solution
            last_finish = r[1]  # update last finish time to this requests

    return schedule


def main():

    set_of_intervals = [(6, 9), (2, 3), (1, 4), (1, 3), (4, 5)]
    print(interval_schedule(set_of_intervals))


if __name__ == '__main__':
    main()
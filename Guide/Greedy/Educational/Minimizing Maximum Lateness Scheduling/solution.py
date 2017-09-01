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


def minimize_lateness(set_of_requests):
    """
    Make a schedule for a set of requests so that the lateness (the time the request goes
    over it's deadline) is minimized.
    :param set_of_requests: the set of requests to build a schedule for
    :return: the schedule for all of the requests
    """

    # Sort request by deadline in ascending order
    sorted_requests = quick_sort(set_of_requests, 0, len(set_of_requests)-1)
    last_finish_time = 0  # initial finish time
    schedule = []  # initial schedule for requests
    for i in sorted_requests:
        start_time = last_finish_time  # start of requests is last finish time
        finish_time = start_time + i[0]  # this requests finish time
        last_finish_time += i[0]  # update latest finish time
        lateness = finish_time - i[1]  # calculate this requests lateness
        schedule.append([i,(start_time, finish_time), lateness])
    return schedule


def main():
    # Request: (time, deadline)
    requests = [(3, 10), (4, 5), (1, 6), (6, 2), (1, 11)]
    scheduled = minimize_lateness(requests)

    # Pretty print
    print('Request\tStart\tFinish\tLateness')
    for i in scheduled:
        print('{}\t{}\t\t{}\t\t{}'.format(i[0], i[1][0], i[1][1], i[2]))


if __name__ == '__main__':
    main()
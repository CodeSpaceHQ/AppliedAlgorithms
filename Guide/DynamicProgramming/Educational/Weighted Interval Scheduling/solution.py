import bisect


class Request(object):
    """
    Simple object to represent a request
    """

    def __init__(self, start, value, finish, previous=None):
        self.start = start  # start time of the request
        self.value = value  # value/weight of the request
        self.finish = finish  # finish time of the request
        self.previous = previous  # previous compatible request


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
        if s[i].finish < s[pivot].finish:  # if s[i] finish < s[pivot] finish
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


def compute_previous(sorted_requests):
    """
    Computes the previous compatible request's value for each request
    :param sorted_requests: finish-time sorted requests
    :return: requests sorted by finish time with previous information filled
    """
    start = [i.start for i in sorted_requests]
    finish = [i.finish for i in sorted_requests]

    for i in range(0, len(sorted_requests)):
        insert_idx = bisect.bisect_right(finish, start[i]) - 1  # index of p(i)
        # value of request p(i)
        prev_idx = 0 if insert_idx < 0 else insert_idx
        sorted_requests[i].previous = prev_idx  # assign p(i) value to previous

    return sorted_requests


def opt(sorted_requests):
    """
    Compute the result of the optimal combination of scheduled request that
    are compatible together.
    :param sorted_requests: requests sorted by finish time
    :return: m[0...n] where m[i] is the weight of optimal scheduling of
             first i requests
    """
    m = [0] * (len(sorted_requests))  # initialize  m
    for i in range(1, len(sorted_requests)):
        request = sorted_requests[i]  # get current request object
        m[i] = max(request.value + m[request.previous], m[i-1])
    return m


def find_solution(scheduled_requests, m, i):
    """
    Computes the optimal schedule of weighted request where optimal
    is the schedule where the sum of request values is the largest.
    :param scheduled_requests: 
    :param m: an array containing the optimal value of previously scheduled
              requests at index i.
    :param i: 
    :return: the optimal solution for scheduling first i requests
    """
    if i == 0:
        return 0

    r = scheduled_requests[i]

    if r.value + m[r.previous] >= m[i-1]:
        return [find_solution(scheduled_requests, m, r.previous), i]
    return find_solution(scheduled_requests, m , i - 1)


def main():
    x = [Request(1, 2, 3), Request(4, 5, 7), Request(8, 5, 20)]
    x = quick_sort(x, 0, len(x)-1)
    x = compute_previous(x)
    m = opt(x)
    x = find_solution(x, m, len(x) - 1)
    print(x)

if __name__ == '__main__':
    main()

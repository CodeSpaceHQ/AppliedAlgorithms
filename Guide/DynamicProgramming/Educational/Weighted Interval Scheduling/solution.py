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
        insert_idx = bisect.bisect_right(finish, start[i])   # index of p(i)
        # value of request p(i)
        sorted_requests[i].previous = insert_idx  # assign p(i) value to previous
    return sorted_requests


def opt(scheduled_requests):
    m = [0] * (len(scheduled_requests) + 1)
    for i in range(1, len(scheduled_requests) + 1):
        r = scheduled_requests[i-1]
        m[i] = max(r.value + m[r.previous], m[i-1])
    return (m)


def find_solution(scheduled_requests, m, i):

    r = scheduled_requests[i-1]
    if i == 0:
        return []
    if m[i] > m[i-1]:
        return find_solution(scheduled_requests, m, r.previous ) + [i-1]
    return find_solution(scheduled_requests, m, i-1)






def main():
    x = [Request(2, 8, 7),
         Request(0, 10, 2),
         Request(1, 5, 4),
         Request(12, 11, 17),
         Request(5, 3, 10),
         Request(3, 2, 8),
         Request(11, 4, 15),
         Request(7, 7, 11),
         Request(0, 10, 5)
         ]

    x = quick_sort(x, 0, len(x) - 1)
    x = compute_previous(x)
    m = opt(x)
    x = find_solution(x, m, len(m) -1)
    print(x)



if __name__ == '__main__':
    main()

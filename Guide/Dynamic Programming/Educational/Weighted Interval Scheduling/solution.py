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
    :return: requests with p(j) filled
    """
    start = [i.start for i in sorted_requests]
    finish = [i.finish for i in sorted_requests]

    for i in range(0, len(sorted_requests)):
        insert_idx = bisect.bisect_right(finish, start[i])   # index of p(i)
        # value of request p(i)
        sorted_requests[i].previous = insert_idx  # assign p(i) value to previous
    return sorted_requests


def opt(sorted_requests):
    """
    Find a maximum value for a set of requests
    :param sorted_requests: requests sorted by finish time  
    :return: opt[0...n] where opt[i] is value of optimal solution for jobs 1...j
    """
    m = [0] * (len(sorted_requests) + 1)
    for i in range(1, len(sorted_requests) + 1):
        r = sorted_requests[i-1]
        m[i] = max(r.value + m[r.previous], m[i-1])
    return m


def find_solution(sorted_requests, m, i):
    """
    Find an optimal schedule with max sum of values
    :param sorted_requests: requests sorted by finish time    
    :param m: array of optimum values for a schedule 1...j
    :param i: the index of the last item in sorted_requests
    :return: a list of indices
    """
    r = sorted_requests[i-1]  # there is one less request than elements in m
    if i == 0:  # base case
        return []
    elif r.value + m[r.previous] > m[i-1]:  # follow max value result schedule
        return find_solution(sorted_requests, m, r.previous ) + [i-1]
    else:
        return find_solution(sorted_requests, m, i-1)


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

    x = quick_sort(x, 0, len(x) - 1)  # sort by finish time
    x = compute_previous(x)  # compute p(j) for every request
    m = opt(x)  # find max value for scheduling of 1...j
    x = find_solution(x, m, len(x))  # find indices of solution schedule
    print(x)

if __name__ == '__main__':
    main()

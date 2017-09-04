def remove_invalid(s, request):
    """
    Remove all conflicting intervals from rthe set of requests
    :param s: the set of requests
    :param request_index: the index of the request to check for conflicts with
    :return: the resulting requests
    """
    result_set = []  # the set of non-conflicting requests
    for r in s:
        if r[0] >= request[1]:  # if the start of r is after request finish
            result_set.append(r)  # add to the solution set
    return result_set


def get_min_finish_time(s):
    """
    Get the request with the minimum finish time in s
    :param s: the set of requests
    :return: the request with the minimum finish time
    """
    min_request = s[0]
    for r in s:
        if r[1] < min_request[1]:
            min_request = r  # reassign min

    return min_request


def interval_schedule(set_of_intervals):
    """
    Schedule a set of intervals so that the most requests get scheduled, there
    are no overlapping requests, and the schedule is optimal
    :param set_of_intervals: the set of requests
    :return: an optimal schedule
    """
    solution = []
    while set_of_intervals:
        request = get_min_finish_time(set_of_intervals)  # get r with min finish
        solution.append(request)  # add r to the solution
        # remove incompatible requests
        set_of_intervals = remove_invalid(set_of_intervals, request)
    return solution


def main():

    set_of_intervals = [(6, 9), (2, 3), (1, 4), (1, 3), (4, 5)]
    print(interval_schedule(set_of_intervals))


if __name__ == '__main__':
    main()

def remove_invalid(s, request):
    # store the request
    temp = s[request]
    # remove the request
    del s[request]
    # remove all requests incompatible with temp
    for i in s:
        if s[i][0] < temp[1]:
            del s[i]
    return s


def get_min_finish_time(s):
    # initial request with min finish time
    min_request_idx = 0
    for i in s:
        # if there is another request with smaller finish time
        if s[i][1] < s[min_request_idx][1]:
            # let that request be the new minimum
            min_request_idx = i
    return min_request_idx


def schedule(set_of_intervals):
    solution = []
    while set_of_intervals:
        # get the index of the interval with the minimum finish time
        request = get_min_finish_time(set_of_intervals)
        # add that request to the solution
        solution.append(request)
        # remove all incompatible requests, including the request itself
        set_of_intervals = remove_invalid(set_of_intervals, request)
    return solution


def main():

    set_of_intervals = [(1, 3), (2, 3),  (1, 4), (4, 5), (6, 9)]
    print(schedule(set_of_intervals))


if __name__ == '__main__':
    main()
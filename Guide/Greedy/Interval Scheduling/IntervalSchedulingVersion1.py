
def remove_invalid(s, request_index):
    # store the request
    temp = s[request_index]
    # remove the request
    del s[request_index]
    # remove all requests incompatible with temp
    i = 0
    while i < len(s):
        if s[i][0] < temp[1]:
            del s[i]
            i -= 1
        else:
            i += 1
    return s


def get_min_finish_time(s):
    # initial request with min finish time
    min_request_idx = 0
    for i in range(len(s)):
        # if there is another request with smaller finish time
        if s[i][1] < s[min_request_idx][1]:
            # let that request be the new minimum
            min_request_idx = i
    return min_request_idx


def schedule(set_of_intervals):
    solution = []
    while set_of_intervals:
        # get the index of the interval with the minimum finish time
        request_index = get_min_finish_time(set_of_intervals)
        # add that request to the solution
        solution.append(set_of_intervals[request_index])
        # remove all incompatible requests, including the request itself
        set_of_intervals = remove_invalid(set_of_intervals, request_index)
    return solution


def main():

    set_of_intervals = [(6, 9), (2, 3), (1, 4), (1, 3), (4, 5)]
    print(schedule(set_of_intervals))


if __name__ == '__main__':
    main()
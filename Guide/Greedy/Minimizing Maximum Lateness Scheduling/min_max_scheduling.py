
def partition(s, begin, end):
    # Lomuto partition scheme worst case O(n^2)
    # this version of partition may not be the most efficient in
    # terms of edge cases - but will do for our purpose of demonstration.
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


def min_max_lateness(set_of_requests):
    sorted_requests = quick_sort(set_of_requests, 0, len(set_of_requests)-1)
    last_finish_time = 0
    schedule = []
    for i in sorted_requests:
        # start time of this request is the last finish time.
        start_time = last_finish_time
        # finish time of this request is the start time plus the request's
        # duration
        finish_time = start_time + i[0]
        # last finish time is now the previous finish time plus the time it
        # took to complete this task
        last_finish_time += i[0]
        # for fun we will calculate the lateness of the request,
        # the time it ran over its deadline, finish time - deadline
        lateness = finish_time - i[1]
        # append [original request, (start time, finish time)] so we
        # can keep track and print later
        schedule.append([i,(start_time, finish_time), lateness])
    return schedule


def main():
    # requests in form of (time, deadline)
    requests = [(3, 10), (4, 5), (1, 6), (6, 2), (1, 11)]
    scheduled = min_max_lateness(requests)

    # pretty print it all
    print('Request\tStart\tFinish\tLateness')
    for i in scheduled:
        print('{}\t{}\t\t{}\t\t{}'.format(i[0], i[1][0], i[1][1], i[2]))


if __name__ == '__main__':
    main()
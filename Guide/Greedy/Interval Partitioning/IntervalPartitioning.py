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


def adjust(start, released, occupied, r):
    # if there are/have been resources in use
    if r:
        # go through the occupied resources
        for i in occupied:
            # check if any are done with their job
            if r[i][-1][-1] < start:
                # move them from occupied to released
                released.append(i)
                occupied.remove(i)
        return released, occupied
    else:
        # no resources have been used
        return released, occupied


def interval_partition(set_of_jobs):
    released = []  # holds index of resources in r that are free
    occupied = []  # holds index of resources in r that are occupied
    r = []  # holds all resources as lists of jobs that they have

    # sort the jobs by start time
    set_of_jobs = quick_sort(set_of_jobs, 0, len(set_of_jobs) -1)

    for j in set_of_jobs:
        # move all free resources in occupied to released
        released, occupied = adjust(j[0], released, occupied, r)
        if released:
            # if there is a resource that has been previously used but is
            # now free, use it
            m = released[0]
            released.remove(m)
        else:
            # create/use a new resource in r
            m = len(r)
            r.append([])
        # move the resource into occupied
        occupied.append(m)
        # append the job to the resources list of jobs it has in r
        r[m].append(j)
    return r


def main():
    jobs = [(1, 4), (2, 6), (3, 8), (5, 7), (7, 9)]
    schedule = interval_partition(jobs)

    # pretty print
    for resource, jobs in enumerate(schedule):
        print('Resource {}:'.format(resource))
        for job in jobs:
            print('\tJob {}'.format(job))

if __name__ == '__main__':
    main()
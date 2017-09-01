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
        if s[i][0] < s[pivot][0]:  # if s[i] < s[pivot]
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


def adjust(start, released, occupied, r):
    """
    Adjust the status of resources based on if they are being used,
    have been used, or have not been used.
    :param start: the start time of the next job
    :param released: the resources that have been used but are free
    :param occupied: the resources that are currently being used
    :param r: the resources and their scheduled jobs
    :return: the list of released jobs and the list of occupied jobs
    """

    if r:   # if there are/have been resources in use
        for i in occupied:  # check if any in occupied are now done
            if r[i][-1][-1] < start:
                released.append(i)  # move from occupied -> released
                occupied.remove(i)
        return released, occupied  # return the set of resources and their stats
    else:
        # no resources have been used
        return released, occupied


def interval_partition(set_of_jobs):
    """
    Given a set of jobs and assuming an infinite amount of resources,
    schedule all jobs using as few resources as possible
    :param set_of_jobs: an array of tuples representing a job with (s, f)
    :return: the resources and their scheduled jobs
    """
    released = []  # holds index of resources in r that are free
    occupied = []  # holds index of resources in r that are occupied
    resources = []  # holds all resources as lists of jobs that they have

    quick_sort(set_of_jobs, 0, len(set_of_jobs) -1)  # sort jobs by start time
    for j in set_of_jobs:
        # move all free resources in occupied to released
        released, occupied = adjust(j[0], released, occupied, resources)
        if released:
            r = released[0]  # choose a resource that is free
            released.remove(r)  # resource is no longer free
        else:
            r = len(resources)
            resources.append([])  # create a new resource to assign jobs to
        occupied.append(r)  # move the resource into occupied
        resources[r].append(j)  # assign this job to the resource
    return resources


def main():
    jobs = [(1, 4), (3, 8), (5, 7), (7, 9), (2, 6)]
    schedule = interval_partition(jobs)

    # pretty print
    for resource, jobs in enumerate(schedule):
        print('Resource {}:'.format(resource))
        for job in jobs:
            print('\tJob {}'.format(job))

if __name__ == '__main__':
    main()
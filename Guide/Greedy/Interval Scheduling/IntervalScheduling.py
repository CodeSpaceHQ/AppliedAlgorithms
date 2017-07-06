
def sort_by_finish(set_of_intervals):
    pass #do quicksort here

def schedule(set_of_intervals):

    # Order the intervals by finish time
    set_of_intervals = sort_by_finish(set_of_intervals)

    # begin algorithm
    solution = set()
    while set_of_intervals:

        # get interval with earliest finish time
        request = set_of_intervals[0]

        # add it to solution
        solution.add(request)

        # remove all conflicting intervals
        for interval in set_of_intervals.ITEMS():
            if interval[0] >= request[0] or interval[1] <= request[1]:
                del interval


def main():
    set_of_intervals = {(2, 3), (4, 5),
                        (6, 9), (1, 10)}

    optimal_solution = schedule(set_of_intervals)
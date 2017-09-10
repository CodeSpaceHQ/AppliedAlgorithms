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


def main():
    x = [Request(1, 2, 3), Request(4, 5, 2)]
    x = quick_sort(x, 0, 1)
    for r in x:
        print(r.start, r.value, r.finish)


if __name__ == '__main__':
    main()
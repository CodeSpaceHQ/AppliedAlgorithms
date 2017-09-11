class Request(object):
    """
    Simple object to represent a request
    """
    def __init__(self, start, value, finish):
        self.start = start  # start time of the request
        self.value = value  # value/weight of the request
        self.finish = finish  # finish time of the request


def counting_sort(array):
    """
    Counting sort time complexity O(n+k)
    https://en.wikipedia.org/wiki/Counting_sort#The_algorithm
    In this case sorts a collection (A) of integers by incrementing a counter in
    another collection (B) at the index corresponding to a value in in the first
    collection A. Then loops through collection B from beginning to end and 
    places the index into a result array however many times the value of B is at 
    that index.
    :param array: the array of integers to be sorted
    :return: the sorted array
    """

    # initialize array to hold the count of repeating values in original array
    counter = [0] * (max(array) + 1)

    # loop through and increase the value for each repeated value found
    for i in array:
        counter[i] += 1

    array = []

    # place indexes of count array in resulting array x times where x is the
    # value found at count[i]
    for i, count in enumerate(counter):
        array += [i] * count
    return array


def main():
    my_list = [4, 3, 2, 1]
    sorted = counting_sort(my_list)
    print(sorted)


if __name__ == '__main__':
    main()
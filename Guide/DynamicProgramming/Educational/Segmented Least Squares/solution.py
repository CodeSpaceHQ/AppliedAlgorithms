from math import inf

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
        if s[i][0] < s[pivot][0]:  # if s[i] x coord < s[pivot] x coord
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


def compute_err(points):
    n = len(points)  # number of points in segment
    x_cords = [points[p][0] for p in range(0, n)] # all x values for segment
    y_cords = [points[p][1] for p in range(0, n)] # all y values for segment
    xy = map(lambda x, y: x * y, x_cords, y_cords) # xi*yi values for segment
    sum_x = sum(x_cords)  # sum of all x values for segment
    sum_y = sum(y_cords)  # sum of all y values for segment
    # calculate slope of least squared error line
    a_numerator = n * (sum(xy)) - (sum_x * sum_y)
    a_denominator = n * (sum([x ** 2 for x in x_cords])) - (sum_x) ** 2
    a = a_numerator / a_denominator
    # calculate y-intercept of least squared error line
    b = (sum_y - (a*sum_x)) / n
    # calculate SEE using the least squared error line
    e = sum(map(lambda x, y: (y-a*x-b)**2, x_cords, y_cords))
    return e


def segment_least_squares(points, cost):
    size = len(points)
    sorted_points = quick_sort(points, 0, size - 1)

    squared_errors = dict()
    for point_j in range(1, size):
        # compute least square errors eij for p1..pj
        for point_i in range(0, point_j):
            # compute eij for segment pi...pj
            e = compute_err(sorted_points[point_i:point_j + 1])
            squared_errors[(point_i, point_j)] = e

    print(squared_errors)
    m = [0] * size
    opt_seg = [0] * size
    for j in range(1, size): # for each point up to size-1
        min_err = inf
        opt_segment_end = None
        for i in range(0, j): # for each segment in points i to j
            err_of_segment = squared_errors[(i, j)] + cost + m[i-1]
            if err_of_segment < min_err:
                min_err = err_of_segment
                opt_segment_end = i
        m[j] = min_err
        opt_seg[j] = opt_segment_end

    return opt_seg

def main():
    coord_set = [
        (0,0),
        (1,1),
        (2,2),
        (3,3),
        (4,3),
        (5,3),
        (6,3),
        (7,4),
        (8,5),
        (9,6),
        (10,7)
    ]
    s = segment_least_squares(coord_set, 0)
    print(s)


if __name__ == '__main__':
    main()

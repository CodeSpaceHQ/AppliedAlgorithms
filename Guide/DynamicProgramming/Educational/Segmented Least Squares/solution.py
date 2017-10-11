from math import inf
import matplotlib.pyplot as plot


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
    """
    Compute the sum of least squared errors line. The equation for this line can
    be found online.
    :param points: a list of points (x,y) that are sorted by x values
    :return: an error value for the line segment fitting the points
    """
    n = len(points)  # number of points in segment
    x_cords = [p[0] for p in points]  # all x values for segment
    y_cords = [p[1] for p in points]  # all y values for segment
    xy = map(lambda x, y: x * y, x_cords, y_cords)  # xi*yi values for segment
    sum_x = sum(x_cords)  # sum of all x values for segment
    sum_y = sum(y_cords)  # sum of all y values for segment
    # calculate slope of least squared error line
    a_numerator = n * (sum(xy)) - (sum_x * sum_y)
    a_denominator = n * (sum([x ** 2 for x in x_cords])) - (sum_x) ** 2
    a = a_numerator / a_denominator if a_denominator > 0 else inf
    # calculate y-intercept of least squared error line
    b = (sum_y - (a * sum_x)) / n
    # calculate SEE using the least squared error line
    e = sum(map(lambda x, y: (y - a * x - b) ** 2, x_cords, y_cords))
    return e


def segment_least_squares(points, c):
    """
    Given points in a plane and a constant cost > 0, find a squesnce of lines
    that minimizes f(x) = E + cost*L where:
        E is the sum of the sums of the squared errors in each segment
        L is the number of lines
    :param points: list of points where each point is in the format [x, y] 
    :param c: the cost of creating a new segment
    :return:
            A list of accumulated cost values for the optimal solution's
            segments, and a list containing the starting points of each segment
            as its values, with the index of that list being the end points.
            
    """
    size = len(points)
    sorted_points = quick_sort(points, 0, size - 1)
    squared_errors = dict()

    for end in range(1, size):  # end of the segment

        for start in range(0, end):  # start of the segment

            points_in_segment = sorted_points[start:end + 1]
            err = compute_err(points_in_segment)  # compute eij for segment
            squared_errors[(start, end)] = err

    m = [0] * size  # track accumulated cost
    seg_starts = [0] * size  # track start and end points of segments

    for end in range(0, size):  # end of segment
        min_cost = inf

        for start in range(0, end):  # beginning of segment

            cost = squared_errors[(start, end)] + c + m[start - 1]
            if cost < min_cost:
                min_cost = cost  # new minimum cost found
                i = start  # save start point for segment
                seg_starts[end] = start
        m[end] = min_cost  # store min cost for segment ending here

    return m, seg_starts


def plot_points(points):
    """
    Plot points on a graph
    :param points: a list of points where each point is [x, y]
    """
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    plot.plot(xs, ys, 'ro')
    plot.show()


def main():
    cords = [  # make it out of order by x value
        [3, 3],
        [2, 2],
        [1, 1],
        [4, 3],
        [5, 3],
        [6, 3],
        [9, 6],
        [7, 4],
        [8, 5]
    ]

    m, seg_points = segment_least_squares(cords, .5)
    print("Cost of optimal solution: {}".format(m[-1]))  # accumulated cost
    print(seg_points)
    plot_points(cords)


if __name__ == '__main__':
    main()

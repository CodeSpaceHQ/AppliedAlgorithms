import matplotlib.pyplot as plot


def compute_sse(points):
    """
    Compute the minimum sum of the squared error of
    a line through given points.
    :param points: a list of points [[x,y],...]
    :return: the minimum sum of squared error value for the
             line passing through the points
    """
    n = len(points)
    # all x values for segment
    x_cords = [p[0] for p in points]
    # all y values for segment
    y_cords = [p[1] for p in points]
    # xi*yi values for segment
    xy = map(lambda x, y: x * y, x_cords, y_cords)
    # sum of all x values for segment
    sum_x = sum(x_cords)
    # sum of all y values for segment
    sum_y = sum(y_cords)
    a_numerator = n * (sum(xy)) - (sum_x * sum_y)
    a_denominator = n * (sum([x ** 2 for x in x_cords])) - sum_x ** 2
    # slope of line
    a = a_numerator / a_denominator if a_denominator > 0 else float('inf')
    # y-intercept of line
    b = (sum_y - (a * sum_x)) / n  # y-intercept
    # Sum of squared errors of line with slope a y-intercept b going through
    # points (xi, yi)
    err = sum( map(lambda x, y: (y - a * x - b) ** 2, x_cords, y_cords))
    return err


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

    n = len(points)
    # Sort point by x-coordinate
    points.sort(key=lambda k: k[0])
    # Initialize matrix to hold SSE error values
    e = [[0 for x in range(n)] for y in range(n)]

    for j in range(1, n):
        for i in range(0, j):
            # Get all points to try segments on
            included_points = points[i:j + 1]
            # Compute SSE eij for this segment
            error = compute_sse(included_points)
            e[i][j] = error

    # List to track accumulating cost
    m = [0] * n
    # List to track start/end points of segments
    segments = [0] * n
    for j in range(1, n):
        # Initial minimum cost
        min_cost = float('inf')
        for i in range(0, j):
            # compute cost for segment from point i to j
            cost = e[i][j] + c + m[i]
            if cost < min_cost:
                # Save new minimum cost
                min_cost = cost
                # Save new minimum segment
                segments[j] = i
        m[j] = min_cost

    return m[-1], segments


def find_segments(points, seg_starts):
    """
    Find each point included in either end of a segment
    :param points: list of points [x,y]
    :param seg_starts: list of starting points for segments. seg_starts[i] is 
                       the starting point of a segment while i is the end point
    :return: each point in points included in the endpoints of all the segments
    """
    if len(points) == 1:
        # exclude last point, it will always point to itself
        return points
    else:
        included_point = points[-1]
        new_cutoff = seg_starts[-1] + 1
        return find_segments(points[:new_cutoff],
                             seg_starts[:new_cutoff]) + [included_point]


def plot_all(points, segment_points):
    """
    Plot all points and segments in the optimal solution using matplotlib
    :param points: list of points [x,y]
    :param segment_points: list of segment endpoints points [x,y] in points 
    :return: show a graph with all points and segments plotted.
    """
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    plot.plot(xs, ys, 'ro')

    xs = [p[0] for p in segment_points]
    ys = [p[1] for p in segment_points]
    plot.plot(xs, ys)

    plot.show()


def main():
    points = [
        [1, 1],
        [2, 3],
        [4, 4],
        [5, 6],
        [7, 9]
    ]

    cost, segments = segment_least_squares(points, .75)
    print("Total cost of line(s) through points: {}".format(cost))
    endpoints = find_segments(points, segments)
    plot_all(points, endpoints)


if __name__ == '__main__':
    main()

def count_inversions(preference_set):
    """
    Split the preference set up and recursively sort and count each one 
    using the merge function
    :param preference_set: the set of preferences to sort and count
    :return: the number of found inversions and the sorted set
    """

    if len(preference_set) < 2:  # no inversions if size not => 2
        return 0, preference_set

    halfway = len(preference_set) // 2
    first_half = preference_set[:halfway] # first half of the set
    second_half = preference_set[halfway:] # second half of the set

    inv_a, a = count_inversions(first_half)
    inv_b, b = count_inversions(second_half)
    inv_c, solution = merge(a, b)

    return inv_a + inv_b + inv_c, solution


def merge(a, b):
    """
    Merge two lists togethert and count any inversions during the process
    :param a: the first sequence to be merged
    :param b: the second sequence to be merged
    :return: the result of merging a and b above, and the count of inversions
             discovered while merging them
    """
    solution = []  # the sorted solution list
    inversion_count = 0
    while a and b:
        num_a = a[0]
        num_b = b[0]
        if num_a > num_b:
            solution.append(num_b)  # put the smaller number in the solution
            b.remove(num_b)  # remove the number from the original set
            inversion_count += len(a)  # increase the inversion count
        else:
            solution.append(num_a)  # put the smaller number in the solution
            a.remove(num_a)  # remove the number from the original set

    # append the remaining elements in the non-empty list to the solution
    if a:
        solution += a
    else:
        solution += b

    return inversion_count, solution


def main():
    my_prefs = [1, 3, 4, 2, 5, 7, 6, 9, 8]
    inversion_count, sorted_set = count_inversions(my_prefs)
    print("{0} inversions, sorted set: {1}".format(inversion_count, sorted_set))

if __name__ == '__main__':
    main()
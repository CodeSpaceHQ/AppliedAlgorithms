
def stable_marriage(men, women):
    """
    Given a set of men and women where both have ranked each person in the other
    set, find a mapping between the two sets such that each pair is stable.
    :param men: a dict of men with key, value where key is the id and value is
                a list id's representing women where their index is their rank
    :param women: a dict of women with key, value where key is the id and value is
                a list id's representing men where their index is their rank
    :return: a dict of all engaged pairs by wife
    """
    single_men = list(men.keys())  # Initial list of single men
    wives = dict()  # Initial mapping of women to men

    while single_men:
        man = single_men[0]  # get a single man

        preferred_wife = men[man][0]  # get the man's highest ranked woman
        wife_preferences = women[preferred_wife]

        if preferred_wife not in wives:  # if she is single, let man propose
            wives[preferred_wife] = man  # if she is  single, she will accept
            del men[man][0]  # delete this woman from man's preferences
            single_men.remove(man)  # man is no longer single (for now)
        else:
            fiance = wives[preferred_wife]  # get womans current fiance

            rank_of_fiance = wife_preferences.index(fiance)  # get fiance rank
            rank_of_man = wife_preferences.index(man)  # get man rank

            # If man is listed before the fiance on the woman's preferences,
            # then the woman accepts the proposal.
            if rank_of_man < rank_of_fiance:  # if man is ranked higher
                wives[preferred_wife] = man  # man becomes new fiance
                single_men.remove(man)
                single_men.append(fiance)  # old fiance becomes single
            else:
                del men[man][0]  # delete this woman from man's preferences

    return wives  # all engaged pairs (by wife)


def main():

    men = {  # man: [list of women where index is rank]
        1: [2, 3, 4, 1],
        2: [2, 1, 3, 4],
        3: [1, 3, 4, 2],
        4: [1, 2, 3, 4]
    }

    women = {  # woman: [list of men where index is rank]
        1: [2, 4, 1, 3],
        2: [3, 1, 2, 4],
        3: [1, 2, 4, 3],
        4: [1, 2, 4, 3]
    }

    pairs = stable_marriage(men, women)

    # Pretty print
    print('Engagements\n(M, W)')
    for key in pairs:
        print('(' + str(pairs[key]) + ',' + str(key) + ')')


if __name__ == '__main__':
    main()

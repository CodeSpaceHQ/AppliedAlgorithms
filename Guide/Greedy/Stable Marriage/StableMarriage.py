
def stable_marriage(men, women):

    single_men = list(men.keys())  # Initial list of single men
    wives = dict()  # Initial mapping of women to men

    while single_men:
        man = single_men[0]

        # Get man's highest ranked woman
        preferred_wife = men[man][0]
        wife_preferences = women[preferred_wife]

        # Let man propose to her
        if preferred_wife not in wives:
            # if she is free, she will accept
            wives[preferred_wife] = man
            del men[man][0]
            single_men.remove(man)
        else:
            # Otherwise we have to check if she prefers this man
            # over her current man.
            fiance = wives[preferred_wife]

            # Position of both competing men in the woman's preferences
            place_of_fiance = wife_preferences.index(fiance)
            place_of_man = wife_preferences.index(man)

            # If man is listed before the fiance on the woman's preferences,
            # then the woman accepts the proposal.
            if place_of_man < place_of_fiance:
                wives[preferred_wife] = man
                single_men.remove(man)
                single_men.append(fiance)
            else:
                del men[man][0]  # Remove woman from man's preferences

    # Return all engaged pairs
    return wives


def main():
    # Set of men comprised of their preferences
    men = {
        1: [2, 3, 4, 1],
        2: [2, 1, 3, 4],
        3: [1, 3, 4, 2],
        4: [1, 2, 3, 4]
    }

    # Set of women comprised of their preferences
    women = {
        1: [2, 4, 1, 3],
        2: [3, 1, 2, 4],
        3: [1, 2, 4, 3],
        4: [1, 2, 4, 3]
    }

    # Run stable marriage algorithm
    pairs = stable_marriage(men, women)

    print('(M, W) = Engagement')
    for key in pairs:
        print('(' + str(pairs[key]) + ',' + str(key) + ')')


if __name__ == '__main__':
    main()

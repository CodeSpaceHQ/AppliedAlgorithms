
def stable_marriage(men, women):

    single_men = list(men.keys())  # Initial list of single men
    wives = dict()  # Initial mapping of women to men

    while single_men:
        man = single_men[0]

        preferred_wife = men[man][0]
        wife_preferences = women[preferred_wife]

        if preferred_wife not in wives:
            wives[preferred_wife] = man
            del men[man][0]
            single_men.remove(man)
        else:
            fiance = wives[preferred_wife]

            # Position of competing men in the woman's preferences
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
    return wives


def main():
    # Set of men comprised of their preferences
    men = {
        0:[2, 1, 0],
        1:[2, 1, 0],
        2:[2, 1, 0]
    }

    # Set of women comprised of their preferences
    women = {
        0: [1, 0, 2],
        1: [1, 0, 2],
        2: [1, 0, 2]
    }

    pairs = stable_marriage(men, women)
    print('(M, W) = Engagement')
    for engagement in pairs.items():
        print(engagement)


if __name__ == '__main__':
    main()

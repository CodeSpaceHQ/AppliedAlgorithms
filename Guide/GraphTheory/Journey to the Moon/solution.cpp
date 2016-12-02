#include <iostream>
#include <vector>
#include <map>


typedef unsigned long moonType;

int main()
{
    moonType numAsts;       // Number of astronauts (N)
    moonType numPairs;      // Number of pairs (I)
    moonType astOne;        // First astronaut in each input line
    moonType astTwo;        // Second astronaut in each input line
    moonType countryAsts;   // Number of astronauts in a given country
    moonType tempAst;       // Index of current astronaut from 'pairs'
    moonType current;       // Index of current astronaut from 'targetAsts'
    long long result = 0;   // Number of ways to choose pairs of astronauts

    /*
       'pairs' is an adjacency list implemented with a 2D vector. One
       dimension of ‘pairs’ has an entry corresponding to each of the
       astronauts. The second dimension holds all of the astronauts that a
       given astronaut is paired with.
    */
    std::vector<std::vector<moonType> > pairs;

    /*
       ‘countries’ is a vector that holds the number of astronauts for a
       given country.
    */
    std::vector<moonType> countries;

    std::cin >> numAsts >> numPairs;

    // Initializing 2nd dimension of 'pairs'
    for(int i = 0; i < numAsts; i++)
    {
        std::vector<moonType> tempVec;
        pairs.push_back(tempVec);
    }

    // Reading input into 'pairs'
    for(int i = 0; i < numPairs; i++)
    {
        std::cin >> astOne >> astTwo;

        /*
           ‘astTwo’ is added to the second dimension of ‘astOne’ and vice
           versa. This ensures that astronauts paired with ‘astTwo’ but not
           ‘astOne’ are still counted as being in the same country as
           ‘astOne,’ no matter where ‘astOne’ and ‘astTwo’ are in relation to
           each other within 'pairs.'
        */
        pairs.at(astOne).push_back(astTwo);
        pairs.at(astTwo).push_back(astOne);
    }

    // Accounting for countries with a single astronaut
    for(unsigned long i = 0; i < numAsts; i++)
    {
        // If an astronaut is not paired with anyone
        if(pairs.at(i).empty())
            countries.push_back(1);
    }

    // Determining country sizes
    for(unsigned long i = 0; i < numAsts; i++)
    {
        if(!pairs.at(i).empty())
        {
            countryAsts = 0;
            // Used to determine if an astronaut is already in the country
            std::map<moonType, int> tempMap;
            // Stores astronaut entries in 'pairs' that need to be visited
            std::vector<moonType> targetAsts;

            // Add the starting astronaut to 'targetAsts'
            targetAsts.push_back(i);
            // Add the starting astronaut to 'tempMap'
            tempMap.insert(std::pair<moonType, int>(i, 1));
            // Increase country size by one
            countryAsts++;

            /*
               This code searches through entries in ‘pairs’ and performs
               three main operations. The first operation checks if any
               astronauts it finds are already accounted for in the current
               country, if so, they are deleted and the program moves on. If
               not, the other two operations are performed. The second
               operation adds the current astronaut to the vector of
               astronaut entries to be visited. The third operation adds the
               current astronaut to the hash map that accounts for astronaut
               presence in the country. This repeats until 'targetAsts' is
               empty.
            */
            while(!targetAsts.empty())
            {
                // Store the last element of 'targetAsts'
                current = targetAsts.back();
                // Remove the last element of 'targetAsts'
                targetAsts.pop_back();

                // While the current entry isn't empty
                while(!pairs.at(current).empty())
                {
                    // Store the last element of the current entry
                    tempAst = pairs.at(current).back();

                    // If 'tempAst' isn't in 'tempMap'
                    if(tempMap.find(tempAst) == tempMap.end())
                    {
                        targetAsts.push_back(tempAst);
                        tempMap.insert(std::pair<moonType, int>(tempAst, 1));
                        countryAsts++;
                    }

                    // Remove the last element from the current entry
                    pairs.at(current).pop_back();
                }
            }

            countries.push_back(countryAsts);
        }
    }

    /*
       This calculates the number of permutations for the current country
       through the distributive property. ‘numAsts’ represents the number of
       astronauts left to operate on. Subtracting the size of the current
       country from ‘numAsts’ results in the number of astronauts aside from
       the current country. By multiplying the size of the current country
       and the number of remaining astronauts together it is possible to
       avoid having to distribute each entry individually.
    */
    for(unsigned long i = 0; i < countries.size(); i++)
    {
        numAsts -= countries.at(i);
        result += numAsts * countries.at(i);
    }

    std::cout << result << std::endl;

    return 0;
}

#include <iostream>

int main()
{
    long long caseSize;     // Size of list to be operated on (N)
    int operations;         // Number of operations (M)
    long long start;        // Temporary storage for start integer (a)
    long long stop;         // Temporary storage for stop integer (b)
    long long operand;      // Temporary storage for operand (k)
    long long * operands;   // Pointer to array of operands
    long long current = 0;  // Current value at given index of array
    long long max = 0;      // Maximum value for array at given index

    std::cin >> caseSize >> operations;

    /*
       One is added to 'caseSize' because 'operands' will hold both 'start'
       and 'end' values. The 'end' values will be shifted one position to
       the right of their actual end point. This is because 'end' values are
       treated like negatives, but the operation in this problem needs to be
       inclusive.
    */
    caseSize++;
    operands = new long long[caseSize];

    // Initializing the elements of 'operands' to zero
    for(long long i = 0; i < caseSize; i++)
    {
        operands[i] = 0;
    }

    // Reading input into 'operands'
    for(int i = 0; i < operations; i++)
    {
        std::cin >> start >> stop >> operand;

        /*
           Decrementing 'start' accounts for the fact that arrays start at
           zero. The reason that only start is decremented is that stop will
           be shifted to the right anyway.
        */
        start--;

        operands[start] += operand;
        operands[stop] -= operand;
    }

    // Calculating the maximum value
    for(long long i = 0; i < caseSize; i++)
    {
        /*
           'current' acts as an accumulator. 'start' values are positive,
           causing 'current' to increase. 'end' values are negative, causing
           'current' to decrease.
        */
        current += operands[i];

        if(max < current)
            max = current;
    }

    std::cout << max;

    delete [] operands;

    return 0;
}

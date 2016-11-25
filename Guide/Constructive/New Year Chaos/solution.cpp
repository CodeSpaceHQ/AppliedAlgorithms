#include <iostream>
#include <string>

int main() {
  int T; // Number of test cases     1 <= T <= 10
  int N; // Number of people in line 1 <= N <= 10^5

  std::cin >> T;

  for (int t = 0; t < T; t++) { // For each test case
    std::cin >> N;              // Get the number of people
    int n;

    /*
       So we can have a 1-based array as opposed to 0-based, makes things easier
          since n>=1
     */
    int line[N + 1];

    /*
       Flag here so we can check for chaotic while reading in the numbers to
          prevent uneeded calculations in the future
     */
    bool is_chaotic = false;

    /*
       Read in the numbers and store them in the line array.
       This is also where we check for chaotic or not. If by the end of this
          loop we haven't said its chaotic, we never will.

       Note: n=1 Because we are working with 1-based array instead of 0
     */
    for (n = 1; n <= N; n++) {
      int x;
      std::cin >> x;

      /*
         The reason for the flag instead of simply breaking here is because we
            still need to read in all the inputs.
         This condition is the ONLY way for the line to be chaotic.
         If it is chaotic we don't need to waste the time to store the values
       */
      if (x > n + 2) is_chaotic = true;
      else line[n] = x;
    }

    if (is_chaotic) {
      /*
         Now that we have read all the numbers in, we can call it quits now if
            its chaotic
       */
      std::cout << "Too chaotic" << std::endl;
    } else {
      int count = 0; // AKA number of bribes

      /*
         Note we are iterating backwards and arranging people as we go.
         This means that at any point, we can assume everybody behind that point
            is where they are supposed to be.
          This forces the situation where if
            line[i] != i, then either line[i-1] = i or line[i-2] = i
       */
      for (n = N; n > 0; n--) {
        /*
           We only care about 3 people & 3 positions at a time.
           Suppose it starts as follows:
           Person A at position X
           Person B at position Y
           Person C at position Z

           Then the line looks like this:
           Person    : C B A
           Position  : Z Y X

           We want the person at position X to be the greatest value.
           We can assume that anybody behind (to the right) of position X is
              already where they are supposed to be.
           AKA every person after position X has a value greater than every
              person at and before position X.

         */
        int x = line[n]; // Person A

        if (x != n) {
          /*
             A is not supposed to be here, since we know they aren't behind
                posiion n, he must have been bribed!
             The question is, who bribed him? B or C?
           */
          count++;             // They must have bribed at least once
          int y = line[n - 1]; // Person B

          /*
             This is here because if person A isn't where he is supposed to
                be, then no matter whether he was bribed by B or C, A needs to
                be in the middle.
             Now where C & B need to be changes depending on whether it was C or
                B that did the bribing.
           */
          line[n - 1] = x;

          /*
             If we stop here, our line will look like this: CAB
           */

          if (y != n) {
            /*
               Hmm.. person B, was also not supposed to be here, C must have
                  bribed two people!
               We have already incremented once, now just increment once more to
                  reflect that it was 2 bribes, not 1.
                Since we know CBA and CAB were not correct, the correct odering
                   of these three people to make it so the person at position X
                   has the greatest value MUST BE BAC
             */
            count++;

            int z = line[n - 2]; // Person C
            line[n]     = z;
            line[n - 2] = y;
          } else {
            line[n] = y;
          }
        } // else x == n in which case nothing needs to be done
      }
      std::cout << std::to_string(count) << std::endl;
    }
  }

  return 0;
}

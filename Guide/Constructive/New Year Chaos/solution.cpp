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

    bool is_chaotic = false; //To check for chaotic while reading in numbers

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

      for (n = N; n > 0; n--) {
        int x = line[n]; // Person A

        if (x != n) {
          count++;             // They must have bribed at least once
          int y = line[n - 1]; // Person B
          line[n - 1] = x;
          
          if (y != n) {
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

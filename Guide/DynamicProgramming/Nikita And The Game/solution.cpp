#include <iostream>
#include <vector>
#include <iterator>
#include <string> // to_string()

typedef unsigned long long int             seq_var;
typedef unsigned int                       element_var;
typedef std::vector<element_var>::iterator seq_itr;


int countSplits(seq_itr begin, seq_itr end, seq_var sum_goal) {
  seq_var element_sum = 0;

  if ((std::distance(begin, end) < 1) || (sum_goal == 0)) {
    return 0;
  }


  for (seq_itr it = begin; it != end; ++it) {
    element_sum += *it;


    if (element_sum > sum_goal) {
      return 0;
    } else if (element_sum == sum_goal) {
      seq_var newSumGoal = sum_goal / 2;


      int leftPartSum = countSplits(begin, it, newSumGoal);
      ++it;
      int rightPartSum = countSplits(it, end, newSumGoal);

      // Return 1 + MAX(leftPartSum,rightPartSum) aka the greatest amount of
      // splits that can happen
      if (leftPartSum > rightPartSum) {
        return 1 + leftPartSum;
      } else {
        return 1 + rightPartSum;
      }
    }

    // The only condition not checked is if element_sum < sum_goal. In that
    // case, we just want to keep iteratiing through the vector
  }

  return 0;
}

int main() {
  int test_count; // The number of test cases

  std::cin >> test_count;

  // For each test case
  for (int test_index = 0; test_index < test_count; test_index++) {
    int seq_size; // Size of the sequence (array) we are
                  // about to take in.

    std::cin >> seq_size;
    std::string str_test_index = std::to_string(test_index);

    std::vector<element_var> sequence;

    element_var element;
    seq_var     element_sum = 0;

    for (int seq_index = 0; seq_index < seq_size; seq_index++) {
      std::cin >> element;
      element_sum += element;
      sequence.push_back(element);
    }

    // If the sum of the elements is 0, then we have a list of all 0s. For an
    // array with size N, and all values=0, the max amount of splits is N-1.
    if (element_sum == 0) {
      std::cout << (seq_size - 1) << std::endl;
      continue;
    }

    // If the sum of the elements is NOT even then we cannot split the sequence
    // into two partitions of equal sums. So we can stop here, print out 0 and
    // move on to the next test case.
    if (element_sum % 2 != 0) {
      std::cout << 0 << std::endl;
      continue;
    }

    std::cout <<
      countSplits(sequence.begin(), sequence.end(), element_sum / 2) << std::endl;
  }

  return 0;
}

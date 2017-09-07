import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static class HashMemory {
        static int prime = 71327;
        static int currentHash = 1;
        static int tempHash = 1;
        static int currentCount = 1;
        static int tempCount = 1;
        static byte[] hashSet = new byte[prime];

        public HashMemory() {}

        public void clearMemory() {
            currentHash = 1;
            tempHash = 1;
            currentCount = 1;
            hashSet = new byte[prime];
        }

        public void addLowerCase(char start) {
            currentHash = getHash(currentHash, start, currentCount);
            currentCount++;
            hashSet[currentHash] = 1;
        }

        public static int getHash(int current, char next, int currentCount) {
            long newHash = (current * Character.getNumericValue(Character.toLowerCase(next)) * currentCount) % prime;
            return (int)newHash;
        }

        public boolean canClear(char next) {
            return checkIfClearable(next, currentCount);
        }

        public boolean canClearRemainingChar(char next) {
            return checkIfClearable(next, tempCount);
        }

        private boolean checkIfClearable(char next, int count) {
            int temp = getHash(tempHash, next, count);
            return hashSet[temp] == 1;
        }

        public void clearChar(char toClear) {
            clear(toClear);
        }

        public void clearRemainingChar(char toClear) {
            clear(toClear);
            tempCount++;
        }

        public void clear(char toClear) {
            hashSet[getHash(tempHash, toClear, currentCount)] = 0;
            currentCount--;
        }

        public void resetTempHash() {
            tempHash = 1;
        }

        public int getCurrentCount() {
            return currentCount;
        }
    }

    static Solution.HashMemory mem = new Solution.HashMemory();

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int queryCount = in.nextInt();

        for (int i = 0; i < queryCount; i++) {
            int firstIndex = 0;
            int secondIndex = 0;
            String first = in.next();
            String second = in.next();
            boolean fail = false;
            mem = new Solution.HashMemory();

            while (firstIndex < first.length() && secondIndex < second.length()) {
                char start = first.charAt(firstIndex);
                char finish = second.charAt(secondIndex);
                boolean hit = false;

                // if: If the characters match or the character from the first string can be capitalized to match.
                // else if: If they couldn't match and both characters are upper case, check if the HashMemory can
                // find a valid match.
                // else: a match is not possible.
                if (start == finish || Character.toUpperCase(start) == finish) {
                    hit = handleNewChar(start, firstIndex, first, finish);

                    if (!hit) {
                        firstIndex++;
                        secondIndex++;
                    }
                } else if (Character.isUpperCase(start) && Character.isUpperCase(finish)) {
                    
                    // Continue to process upper case characters if they exist and can be cleared.
                    while (Character.isUpperCase(start) && mem.canClear(start)) {
                        if (!(firstIndex < first.length() && secondIndex < second.length()))
                            break;

                        mem.clearChar(start);
                        firstIndex++;
                        hit = true;
                        start = first.charAt(firstIndex);
                    }

                    if (!hit) {
                        if (mem.getCurrentCount() == 1) {
                            fail = true;
                        }

                        firstIndex++;
                    }

                    mem.resetTempHash();
                } else {
                    firstIndex++;
                }
            }

            // If the algorithm has not fully processed the second string, it failed.
            // Else, check if the first string still has characters that need to be processed (capital chars).
            if (secondIndex != second.length()) {
                fail = true;
            } else {
                // Iterate through all characters in the first string.
                while (firstIndex < first.length()) {

                    char nextC = first.charAt(firstIndex);
                    
                    // If the next character is upper case, check if the HashMemory previously satisifed it.
                    if (Character.isUpperCase(nextC)) {
                        if (mem.canClearRemainingChar(Character.toLowerCase(nextC))) {
                            mem.clearRemainingChar(nextC);
                        } else {
                            fail = true;
                            break;
                        }
                    }

                    firstIndex++;
                }
            }

            if (fail)
                System.out.println("NO");
            else
                System.out.println("YES");
        }
    }

    // Whenever there is a new match between final and initial characters, the algorithm must
    // decide if the new character should be added to the hash, the hash cleared, or a repeated character handled.
    public static boolean handleNewChar(char start, int firstIndex, String first, char finish) {
        if (Character.isLowerCase(start)) {
            mem.addLowerCase(start);
        } else {
            if (firstIndex + 1 < first.length() && first.charAt(firstIndex + 1) == finish) {
                return handleRepeatedNextChar(first, firstIndex) != firstIndex;
            } else {
                mem.clearMemory();
            }
        }

        return false;
    }

    // If there's a repeated character then the system should clear a valid previous character if it exists in the
    // HashMemory.
    public static int handleRepeatedNextChar(String first, int firstIndex) {
        char tempChar = first.charAt(firstIndex + 1);
        if (mem.canClear(tempChar)) {
            mem.clearChar(tempChar);
            firstIndex++;
        }

        return firstIndex;
    }
}

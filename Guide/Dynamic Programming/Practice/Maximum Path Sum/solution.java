import java.io.*;
import java.util.*;


public class Solution {


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int cases = scan.nextInt();
        for(int i = 0; i < cases; i++) {

            int n = scan.nextInt();
            int[][] numbers = new int[101][101];

            for(int j = 0; j < n; j++) {
                for(int k = 0; k <= j; k++) {
                    numbers[j][k] = scan.nextInt();
                }
            }

            for(int j = 1; j < n; j++) {
                for(int k = 0; k <= j; k++) {
                    int left;
                    int right;
                    if(k == 0) {
                        left = 0;
                    } else {
                        left = numbers[j-1][k-1];
                    }
                    if(k == j) {
                        right = 0;
                    } else {
                        right = numbers[j-1][k];
                    }

                    numbers[j][k] += Math.max(left, right);
                }
            }

            int max = 0;
            for(int j = 0; j < n; j++) {
                if(numbers[n-1][j] > max) {
                    max = numbers[n-1][j];
                }
            }
            System.out.println(max);
        }
    }

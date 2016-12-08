import java.util.Scanner;

public class KindergartenAdventureOptimised
{
    public static void main(String[] args)
    {
        Scanner reader = new Scanner(System.in);

        int n = reader.nextInt();           //the number of students

        int[] times = new int[n];           //times[i] is the time needed by student i-1
        int[] ranges = new int[2*n + 1];    //range[i] is the number of students that
                                            //would be able to finish if the teacher
                                            //started with student i+1

        /*
            Read in the times for each student into times.
            For each input add one to the starting index and subtract one from the index after the ending index.
            Compute all the numbers in ranges from 1 to n-1.
         */
        for (int i = 0; i < n; i++)
        {
            times[i] = reader.nextInt();
            ranges[i + 1] += 1;
            ranges[(i + 1) + (n - times[i])] -= 1;
            if(i > 0)
            {
                ranges[i] += ranges[i - 1];
            }
        }

        /*
            Compute all the numbers in ranges from n to 2n.
            Find the position for the teacher to start at that would allow the most students to finish.
         */
        int maxPos = 0;     //The first student where the maximum number of students will finish
        for (int i = n; i < 2*n + 1; i++)
        {
            ranges[i] += ranges[i - 1];
            ranges[i - n] += ranges[i];
            if(ranges[i - n] > ranges[maxPos])
            {
                maxPos = i - n;
            }
        }

        //Print the answer.
        System.out.println(maxPos + 1);
    }
}

import java.util.Scanner;

public class KindergartenAdventure
{
    public static void main(String[] args)
    {
        Scanner reader = new Scanner(System.in);

        int n = reader.nextInt();   //the number of students
        int[] times = new int[n];   //times[i] is the time needed by student i-1

        //Read in the time for each student into times.
        for (int i = 0; i < n; i++)
        {
            times[i] = reader.nextInt();
        }

        int[] ranges = new int[2*n + 1];    //range[i] + range[(i + n) % (2n)] is the number of students
                                            //that would be able to finish if the teacher started with student i+1

        //for each input add one to the starting index and subtract one from the index after the ending index.
        for (int i = 0; i < n; i++)
        {
            ranges[i + 1] += 1;
            ranges[(i + 1) + (n - times[i])] -= 1;
        }

        //Compute all the numbers in ranges.
        for (int i = 1; i < 2*n + 1; i++)
        {
            ranges[i] += ranges[i - 1];
        }

        int[] numComplete = new int[n];     //numComplete[i] is the number of students that would be able to
                                            //finish if the teacher started with student i+1

        //Compute all the numbers in numComplete using ranges.
        for (int i = 0; i < n; i++)
        {
            numComplete[i] = ranges[i] + ranges[i + n];
        }

        //Find the maximum number of students that can finish starting with any student and the number of that student.
        int max = numComplete[0];   //The maximum number of students that could finish starting with any student.
        int maxPos = 0;             //The first possition in numComplete where the value max occurs.
        for (int i = 1; i < n; i++)
        {
            if (numComplete[i] > max)
            {
                max = numComplete[i];
                maxPos = i;
            }
        }

        //Print the answer.
        System.out.println(maxPos + 1);
    }
}

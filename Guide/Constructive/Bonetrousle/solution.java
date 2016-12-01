import java.io.*;
import java.util.Scanner;

public class Bonetrousle
{
    /*
        boolean boxOutOfRange(int b, long k, long e, long amountShort)
        This method returns True if the first box, e, is < 1 or the last box,
        (e+b-1) if amountShort == 0 or (e+b) otherwise, is > k and returns
        False otherwise.
     */
    public static boolean boxOutOfRange(int b, long k, long e, long amountShort)
    {
        return e < 1 || ((amountShort == 0)? e+b-1 : e+b) > k;
    }

    /*
        void print(int b, long k, long e, long amountShort)
        This method prints all the boxes in the range [e, e+b]
        if amountShort == 0, prints all the boxes in the range
        [e, e+b+1] with the exception of the box (e - amountShort),
        or prints "-1" if there is going to be a box in the solution that
        is out of the range [1, k].
     */
    public static void print(int b, long k, long e, long amountShort)
    {
        //If the first box or last box will be out of the range [1, k] print -1.
        if(boxOutOfRange(b, k, e, amountShort))
        {
            System.out.println("-1");
        }
        //Else print all the boxes.
        else
        {
            int boxToSkip = (int)(b - amountShort); //The index of the box to skip in the sequence.

            //OutputStream is needed instead of System.out.println() becasue is is much faster.
            OutputStream out = new BufferedOutputStream( System.out );
            long lastNumPrinted = e;

            out.write(("" + lastNumPrinted).getBytes());

            for (int i = 1; i < b; i++)
            {
                if(i == boxToSkip)
                {
                    lastNumPrinted += 2;
                }
                else
                {
                    lastNumPrinted++;
                }

                out.write((" " + lastNumPrinted).getBytes());
            }

            out.write(("\n").getBytes());
            out.flush();
        }
    }

    public static void main(String[] args) throws IOException
    {
        Scanner reader = new Scanner(new File("input.txt"));

        int trips = reader.nextInt(); //Number of times to run the algorithm.

        for (int i = 0; i < trips; i++)
        {
            long n = reader.nextLong(); //Number of noodles to buy.
            long k = reader.nextLong(); //Number of boxes for sale.
            int b = reader.nextInt();   //Number of boxes to buy.

            /*
                The formula for t consecutive boxes is e + (e + 1) + (e + 2) + ... + (e + t-1) = n
                Where e is the value of the first box.
            */

            long numConstants = (long)((b/2.0) * (b-1));    //The number the constants in the formula add up to.

            long amountShort = (n - numConstants) % b;      //How much the current sequence of t boxes starting
                                                            //with e will be short of n.

            long e = (n - numConstants) / b;                //The number for e in the formula.

            print(b, k, e, amountShort);
        }
    }
}

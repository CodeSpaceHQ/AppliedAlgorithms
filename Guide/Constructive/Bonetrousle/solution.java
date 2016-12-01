import java.io.*;
import java.util.Scanner;

/**
 * Created by koepk on 10/3/2016.
 */
public class Bonetrousle
{
    public static void main(String[] args) throws IOException
    {
        Scanner reader = new Scanner(new File("input.txt"));

        int trips = reader.nextInt();

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

            //If the first box or last box will be out of the range [1, k] print -1
            if(e < 1 || ((amountShort == 0)? e+b-1 : e+b) > k )
            {
                System.out.println("-1");
            }
            else
            {
                int boxToSkip = (int)(b - amountShort); //The index of the box to skip in the sequence.

                OutputStream out = new BufferedOutputStream( System.out );
                long lastNumPrinted = e;

                out.write(("" + lastNumPrinted).getBytes());

                for (int j = 1; j < b; j++)
                {
                    if(j == boxToSkip)
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
    }
}

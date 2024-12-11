public class Program
{
    static void Main(string[] args)
    {
        int [] VectInv = { 0, 0, 0, 0, 4, 4, 1, 0, 0 };  //{ 0, 0, 0, 1, 1, 3, 3, 2, 2 } { 0, 0, 0, 3, 4, 3, 5, 6, 1 }
        int [] recover = new int [VectInv.Length];
        int k = 0;
        recover[recover.Length - 1] = VectInv.Length-VectInv[VectInv.Length-1];
        while(Array.Exists(VectInv, x => x == 0))
        { 

            for (int i = VectInv.Length - 1; i >= 0; i--)
            {
                if (VectInv[i] == 0)
                {
                    recover[i] = VectInv.Length - k;
                    k++;
                    for (int j = VectInv.Length - 1; j >= i; j--)
                    {
                            VectInv[j]--;
                    }
                    break;
                }                
            }            
        }
        
        for (int i = 0; i < recover.Length; i++)
        {
            Console.Write(recover[i] + " ");
        }        
    }
}
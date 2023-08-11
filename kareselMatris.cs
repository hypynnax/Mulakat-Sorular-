using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KareselMatris {

    class Program {

        static void Main(string[] args) {
            int n = 0;
            int[,] desen = new int[n,n];
            int tekrar = 0;
            for (int k = 0; k < n/2+1; k++) {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (desen[i,j] == 0) {
                            if (i == tekrar || i == n-1-tekrar || j == tekrar || j == n-1-tekrar) {
                                desen[i, j] = tekrar + 1;
                            }
                        }
                    }
                }
                tekrar += 1;
            }

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    Console.Write(desen[i,j]+"  ");
                }
                Console.WriteLine();
                Console.WriteLine();
            }
            Console.ReadKey();
        }
    }
}

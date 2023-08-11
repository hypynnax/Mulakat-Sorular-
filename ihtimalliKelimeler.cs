using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace Sifreleme {
    class Program {
        static void degerArttirma(int[] dizi, int sinir) {
            for (int i = dizi.Length - 1; i > 0; i--) {
                if (dizi[i] % sinir == 0 && dizi[i] != 0) {
                    dizi[i] = 0;
                    dizi[i - 1] += 1;
                }
            }
        }
        static void Main(string[] args) {
            Stopwatch watch = new Stopwatch();
            watch.Start();
            char[] harfler = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ı', 'i', 'k', 'l' };
            int kelimeUzunlugu = 10;
            int[] basamkDegeri = new int[kelimeUzunlugu];
            while (true) {
                string kelime = "";
                bool sonMu = true;
                for (int i = (kelimeUzunlugu - 1); i >= 0; i--) {
                    kelime = harfler[basamkDegeri[i]] + kelime;
                }
                string fileName = "C: \\Users\\hypyn\\source\\repos\\Sifreleme\\olusankelimeler.txt";
                FileStream fs = new FileStream(fileName, FileMode.Open, FileAccess.Write);
                fs.Close();
                File.AppendAllText(fileName, kelime + "\n");
                foreach (int basamak in basamkDegeri) {
                    if (basamak != harfler.Length - 1) {
                        sonMu = false;
                    }
                }
                if (sonMu) {
                    break;
                }
                basamkDegeri[kelimeUzunlugu - 1] += 1;
                degerArttirma(basamkDegeri, harfler.Length);
            }
            watch.Stop();
            Console.WriteLine("Bağlantı kurulma süresi: {0}", watch.Elapsed.Milliseconds);
            Console.ReadKey();
        }
    }
}

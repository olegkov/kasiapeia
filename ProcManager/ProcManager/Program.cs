using System;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;

namespace ProcManager
{
    class Program
    {
        static void Main(string[] args)
        {
            MonitorProcessesAsync();
            Console.ReadLine();
           // Syn.

           // SpeechRecognitionEngine
        }

        private static async Task MonitorProcessesAsync()
        {
            var originalProcessSet = Process.GetProcessesByName("chrome").ToList();

            // Create a new SpeechRecognizer instance.
           // SpeechRecognizer sr = new SpeechRecognizer();

            while (true)
            {
                var processes = Process.GetProcessesByName("chrome").ToList();
                foreach (var proc in processes)
                {
                    if (!originalProcessSet.Any(p => p.Id == proc.Id))
                    {
                        proc.Kill();
                        proc.Close();
                        Console.WriteLine("Process killed!");
                    }
                }

                await Task.Delay(5000);
            }
        }
    }
}

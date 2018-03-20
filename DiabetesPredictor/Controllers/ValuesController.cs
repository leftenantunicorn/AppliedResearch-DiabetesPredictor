using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Reflection;
using System.Text;
using System.Web.Http;
using DiabetesPredictor.Models;

namespace DiabetesPredictor.Controllers
{
    public class ValuesController : ApiController
    {
        // GET api/values/5
        [HttpPost()]
        public string Post([FromBody] DiabetesRecord modelRecord)
        {
            string result;

            string fileName = "bayespredictor.py";
            string dataName = "pima-data.csv";
            string pathPy = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"python\", fileName);
            string pathCsv = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"python\", dataName);


            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = @"C:\Users\bradleye\Anaconda3\python.exe";
            start.Arguments = string.Format("{0} {1} {2}", pathPy, pathCsv, modelRecord.PropertiesAsCsv());
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {

                    result = reader.ReadToEnd();
                }
            }

            return result;
        }

    }
}

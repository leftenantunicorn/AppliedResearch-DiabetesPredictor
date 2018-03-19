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
            //string.Format("{0},{1},{2},{3},{4},{5},{6},{7}", modelRecord.num_preg, modelRecord.glucose_conc, modelRecord.diastolic_bp,
            //    modelRecord.thickness, modelRecord.insulin, modelRecord.bmi, modelRecord.diab_pred, modelRecord.age);
            start.Arguments = string.Format("{0} {1} {2}", pathPy, pathCsv, modelRecord.ToString());
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

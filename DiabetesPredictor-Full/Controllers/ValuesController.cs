using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Web.Http;
using Python.Runtime;

namespace DiabetesPredictor.Controllers
{
    [System.Web.Mvc.Route("api/[controller]")]
    public class ValuesController : ApiController
    {
        // GET api/values/5
        [HttpGet()]
        public string Get(DiabetesRecord modelRecord)
        {
            string result;

            string fileName = "bayespredictortwo.py";
            string dataName = "pima-data.csv";
            string pathPy = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"python\", fileName);
            string pathCsv = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"python\", dataName);


            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = @"C:\Users\bradleye\Anaconda3\python.exe";
            var record = string.Format("{0},{1},{2},{3},{4},{5},{6},{7}", modelRecord.num_preg, modelRecord.glucose_conc, modelRecord.diastolic_bp,
                modelRecord.thickness, modelRecord.insulin, modelRecord.bmi, modelRecord.diab_pred, modelRecord.age);
            start.Arguments = string.Format("{0} {1} {2}", pathPy, pathCsv, record);
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

    public class DiabetesRecord
    {
        public Double num_preg { get; set; }
        public Double glucose_conc { get; set; }
        public Double diastolic_bp { get; set; }
        public Double thickness { get; set; }
        public Double insulin { get; set; }
        public Double bmi { get; set; }
        public Double diab_pred { get; set; }
        public Double age { get; set; }
    }
}

using System;
using System.Collections.Generic;
using System.Configuration;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Web;

namespace Predictor.Helpers
{
    public static class PythonScriptHelpers
    {
        public static string ExecutePythonScript(string fileName, string dataName, params string[] args)
        {
            var pythonInstallationLocation = ConfigurationManager.AppSettings["pythonPathErin"];

            string result;
            string pathPy = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"python\", fileName);
            string pathCsv = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"python\", dataName);

            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = pythonInstallationLocation;
            var argumentsBuilder = new StringBuilder().AppendFormat("{0} {1}", pathPy, pathCsv);
            foreach (string arg in args)
            {
                argumentsBuilder.AppendFormat(" {0}", arg);
            }
            start.Arguments = argumentsBuilder.ToString();
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
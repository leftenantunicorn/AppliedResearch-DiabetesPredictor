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
        // GET api/values
        [HttpGet]
        public IEnumerable<string> Get()
        {
            string result;

            string fileName = "test.py";
            string path = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"python\", fileName);


            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = @"C:\Users\bradleye\Anaconda3\python.exe";
            var args = new string[] {"arg1","arg2"};
            start.Arguments = string.Format("{0} {1}", path, args);
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    result = reader.ReadToEnd();
                }
            }

            return new string[] { result };

        }

        // GET api/values/5
        [HttpGet()]
        public string Get(int id)
        {
            return "value";
        }

        // POST api/values
        [HttpPost]
        public void Post([FromBody]string value)
        {
        }

        // PUT api/values/5
        [HttpPut()]
        public void Put(int id, [FromBody]string value)
        {
        }

        // DELETE api/values/5
        [HttpDelete()]
        public void Delete(int id)
        {
        }
    }
}

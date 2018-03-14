using System;
using System.Collections.Generic;
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
            var path = $"{Environment.GetEnvironmentVariable("Path", EnvironmentVariableTarget.Machine)};{@"C:\Users\Erin\Anaconda3\"}";

            Environment.SetEnvironmentVariable("Path", path, EnvironmentVariableTarget.Process);

            //PythonEngine.PythonHome = @"C:\Users\Erin\Anaconda3\";
            //PythonEngine.Initialize();
            string result = "defualt";

            using (Py.GIL())
            {
                dynamic np = Py.Import("numpy");
                Console.WriteLine(np.cos(np.pi * 2));

                dynamic sin = np.sin;
                Console.WriteLine(sin(5));

                double c = np.cos(5) + sin(5);
                Console.WriteLine(c);
                result = c.ToString();
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

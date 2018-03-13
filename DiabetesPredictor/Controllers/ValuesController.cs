using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace DiabetesPredictor.Controllers
{
    [Route("api/[controller]")]
    public class ValuesController : Controller
    {
        // GET api/values
        [HttpGet]
        public IEnumerable<string> Get()
        {

            double[] record = new double[] { 6 , 148, 72, 35, 0, 33.6, 0.627, 50 };

            // host python and execute script
            var engine = IronPython.Hosting.Python.CreateEngine();
            var scope = engine.CreateScope();

            var paths = engine.GetSearchPaths();
            paths.Add(@"C:\Users\Erin\Miniconda3\Lib\site-packages");
            engine.SetSearchPaths(paths);

            engine.ExecuteFile(@"python/Naive-BayesPredictor.py", scope);

            // get function and dynamically invoke
            var predict = scope.GetVariable("predictSingleRecord");
            var result = predict(record);

            return new string[] { result };
        }

        // GET api/values/5
        [HttpGet("{id}")]
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
        [HttpPut("{id}")]
        public void Put(int id, [FromBody]string value)
        {
        }

        // DELETE api/values/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}

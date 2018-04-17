using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using Predictor.Helpers;

namespace Predictor.Controllers
{
    [RoutePrefix("api/model")]
    public class ModelController : ApiController
    {
        [HttpGet()]
        [Route("metrics")]
        public string GetMetrics()
        {
            string fileName = "bayesModelData.py";
            string dataName = "pima-data.csv";

            return PythonScriptHelpers.ExecutePythonScript(fileName, dataName);
        }


        [HttpGet]
        [Route("nu-values")]
        public string GetPredictionMatrix()
        {
            string fileName = "hyperparams.py";
            string dataName = "pima-data.csv";
            var x = PythonScriptHelpers.ExecutePythonScript(fileName, dataName);
            return x;
        }

    }
}
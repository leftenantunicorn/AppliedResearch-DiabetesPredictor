using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using Predictor.Helpers;
using Predictor.Models;

namespace Predictor.Controllers
{
    [RoutePrefix("api/prediction")]
    public class PredictionController : ApiController
    {
        [HttpPost()]
        [Route("")]
        public string PostToPrediction([FromBody] DiabetesRecord modelRecord)
        {
            string fileName = "bayespredictor.py";
            string dataName = "pima-data.csv";

            return PythonScriptHelpers.ExecutePythonScript(fileName, dataName, modelRecord.PropertiesAsCsv());
        }

        [Route("trainingset")]
        [HttpPost()]
        public bool PostToTrainingSet([FromBody] DiabetesRecord modelRecord)
        {
            string dataName = "pima-data-test.csv";

            if (File.Exists(dataName)) File.AppendAllText(dataName, Environment.NewLine + modelRecord.PropertiesAsCsv());
            else return false;

            return true;
    }
    }
}

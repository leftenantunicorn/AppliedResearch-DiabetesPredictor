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
        public bool PostToTrainingSet([FromBody] DiabetesOutcomeRecord modelRecord)
        {
            string dataName = "pima-data-test.csv";
            string pathCsv = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"python\", dataName);

            if (File.Exists(pathCsv)) File.AppendAllText(pathCsv, Environment.NewLine + modelRecord.PropertiesAsCsv());
            else return false;

            return true;
        }
    }
}

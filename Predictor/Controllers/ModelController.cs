﻿using System;
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
        [Route("sensitivity")]
        public IEnumerable<string> GetSensitivity()
        {
            return new string[] { "value1", "value2" };
        }

        [HttpGet()]
        [Route("specificity")]
        public IEnumerable<string> GetSpecificity()
        {
            return new string[] { "value3", "value4" };
        }

        [HttpGet()]
        [Route("data")]
        public IEnumerable<string> GetData()
        {
            string fileName = "bayesModelData.py";
            string dataName = "pima-data.csv";

            var thing =  PythonScriptHelpers.ExecutePythonScript(fileName, dataName);

            return thing.Split(',');
        }

        // POST api/<controller>
        public void Post([FromBody]string value)
        {
        }

        // PUT api/<controller>/5
        public void Put(int id, [FromBody]string value)
        {
        }

        // DELETE api/<controller>/5
        public void Delete(int id)
        {
        }
    }
}
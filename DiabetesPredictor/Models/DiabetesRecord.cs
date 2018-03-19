using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Web;

namespace DiabetesPredictor.Models
{
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

    public override string ToString()
    {
        return string.Join(", ", this.GetType().GetProperties().Select(x => x.GetValue(this)));
    }
}
}
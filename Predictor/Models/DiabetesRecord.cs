using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace Predictor.Models
{
    public class DiabetesRecord
    {
        [Order(1)]
        public double num_preg { get; set; }
        [Order(2)]
        public double glucose_conc { get; set; }
        [Order(3)]
        public double diastolic_bp { get; set; }
        [Order(4)]
        public double thickness { get; set; }
        [Order(5)]
        public double insulin { get; set; }
        [Order(6)]
        public double bmi { get; set; }
        [Order(7)]
        public double diab_pred { get; set; }
        [Order(8)]
        public double age { get; set; }

        public String PropertiesAsCsv()
        {
            var filter = new List<string>() { "diastolic_bp", "thickness", "insulin", "age"};
            var sortedProperties = this.GetType().GetProperties().OrderBy(x => (x.GetCustomAttributes(typeof(Order), true).Single() as Order).OrderNumber);
            var filteredProperties = sortedProperties.Where(x => !filter.Contains(x.Name));
            return string.Join(",", filteredProperties.Select(x => x.GetValue(this)));
        }

        public String PropertiesAsCsvFull()
        {
            var sortedProperties = this.GetType().GetProperties().OrderBy(x => (x.GetCustomAttributes(typeof(Order), true).Single() as Order).OrderNumber);
            return string.Join(",", sortedProperties.Select(x => x.GetValue(this)));
        }
    }

    public class DiabetesOutcomeRecord : DiabetesRecord
    {
        [Order(9)]
        public int outcome { get; set; }
    }

    public class Order : Attribute
    {
        public Order(int number)
        {
            OrderNumber = number;
        }
        public int OrderNumber { get; set; }
    }
}
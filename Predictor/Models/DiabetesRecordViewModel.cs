using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace Predictor.Models
{
    public class DiabetesRecordViewModel
    {
        [Required]
        [Display(Name = "Number of Pregnancies:")]
        public double num_preg { get; set; }
        [Required]
        [Display(Name = "Glucose Concentration:")]
        public double glucose_conc { get; set; }
        [Required]
        [Display(Name = "Diastolic Blood Pressure:")]
        public double diastolic_bp { get; set; }
        [Required]
        [Display(Name = "Thickness:")]
        public double thickness { get; set; }
        [Required]
        [Display(Name = "Insulin:")]
        public double insulin { get; set; }
        [Required]
        [Display(Name = "Body Mass Index:")]
        public double bmi { get; set; }
        [Required]
        [Display(Name = "Diabetes Pedigree Function:")]
        public double diab_pred { get; set; }
        [Required]
        [Display(Name = "Age:")]
        public double age { get; set; }

        [Display(Name = "Patient is diabetic:")]
        public bool outcome { get; set; }
    }
}
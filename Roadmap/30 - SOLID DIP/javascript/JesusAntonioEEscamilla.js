/** #30 - JavaScript -> Jesus Antonio Escamilla */

/**
 * Este principio establece dos reglas clave:
 * 1-. Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones (interfaces).
 * 2-. Las abstracciones no deben depender de detalles. Los detalles deben depender de abstracciones.
 */

//---EJERCIÓ---
//INCORRECTO
// Creamos un modelo para usarlo
class PdfReport__{
   generate(content){
      console.log(`Generating PDF report with content: ${content}`);
   }
}

// Creamos un objeto
class ReportGenerator__{
   constructor(pdfReport){
      this.pdfReport = pdfReport;
   }

   generateReport(content){
      this.pdfReport.generate(content);
   }
}

// El uso Incorrecto de DIP
const pdfReport__ = new PdfReport__();
const reportGenerator__ = new ReportGenerator__(pdfReport__);
reportGenerator__.generateReport("Annual Financial Report");


//CORRECTO
// Interfaz del Report
class IReport{
   generate(content){
      throw new Error("Method 'generate()' must be implemented");
   }
}

// Implementación Correcta de DIP
class PdfReport extends IReport{
   generate(content){
      console.log(`Generating PDF report with content: ${content}`);
   }
}

class HtmlReport extends IReport{
   generate(content){
      console.log(`Generating HTML report with content: ${content}`);
   }
}

class ReportGenerator{
   constructor(report){
      // Dependencia de la abstraction
      if (!(report instanceof IReport)) {
         throw new Error("Invalid report service");
      }
      this.report = report;
   }

   generateReport(content){
      this.report.generate(content);
   }
}

// El uso Correcto de DIP
const pdfReport = new PdfReport();
const htmlReport = new HtmlReport();

const reportGenerator = new ReportGenerator(pdfReport);
reportGenerator.generateReport("Monthly Financial Report");

const htmlReportGenerator = new ReportGenerator(htmlReport);
htmlReportGenerator.generateReport("Weekly Financial Report")



/**-----DIFICULTAD EXTRA-----*/

// Pendiente

/**-----DIFICULTAD EXTRA-----*/
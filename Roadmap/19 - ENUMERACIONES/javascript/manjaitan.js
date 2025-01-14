
let day = 0;

const DiasDeLaSemana = {

   LUNES: 1,
   MARTES: 2,
   MIERCOLES: 3,
   JUEVES: 4,
   VIERNES: 5,  
   SABADO: 6,
   DOMINGO: 7, 

}

function greetdia(day) {
  
    if (day === DiasDeLaSemana.LUNES) {
        console.log('Se ha seleccionado el día Lunes');
    }  else if (day === DiasDeLaSemana.MARTES) {
        console.log('Se ha seleccionado el día Martes');
    } else if (day === DiasDeLaSemana.MIERCOLES) {
        console.log('Se ha seleccionado el día Miercoles');
    } else if (day === DiasDeLaSemana.JUEVES) {
        console.log('Se ha seleccionado el día Jueves');
    } else if (day === DiasDeLaSemana.VIERNES) {
        console.log('Se ha seleccionado el día Viernes');
    } else if (day === DiasDeLaSemana.SABADO) {
        console.log('Se ha seleccionado el día Sabado');
    } else if (day === DiasDeLaSemana.DOMINGO) {
        console.log('Se ha seleccionado el día Domingo');
    }
    else 
        {
        console.log('Dia seleccionado erróneo, rango de datos insertables del 1 al 7,')
        };

 }


greetdia(7)
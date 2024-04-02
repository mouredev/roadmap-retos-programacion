// 1º Ejercicio

    let fechaActual : Date = new Date();    // Cojemos la fecha entera

    console.log(fechaActual);   // Mostramos la fecha

    let fechaNacimiento: Date = new Date(2004, 10, 3, 3, 30, 0); // (año, mes, día, hora, minuto, segundo)
    // En TS y JS los meses empiezan en el 0 y acaban en el 11, por lo cual Noviembre es el 10.

    console.log(fechaNacimiento);   // Mostramos la fecha

    let diferenciaAnhos : number = fechaActual.getFullYear() - fechaNacimiento.getFullYear();

    console.log(diferenciaAnhos);

// Ejercicio Extra

    // 1º Mostrando Día, mes y año
    // El +1 es importante en el 'getMonth()' debido a que los meses en TS empiezan en el 0
    console.log(`${fechaNacimiento.getDay()}/${fechaNacimiento.getMonth() +1 }/${fechaNacimiento.getFullYear()}`);

    // 2º Mostrando Hora, minuto y segundo.
    console.log(`${fechaNacimiento.getHours()}/${fechaNacimiento.getMinutes() +1 }/${fechaNacimiento.getSeconds()}`);

    // 3º Mostrar por Día de año
    function diaDelAnho(fecha: Date): number {
        let anhoPorDefecto = new Date(fecha.getFullYear(), 0, 0);
        let diferencia = (fecha.getTime() - anhoPorDefecto.getTime()) + ((anhoPorDefecto.getTimezoneOffset() - fecha.getTimezoneOffset()) * 60 * 1000);
        let dia = 1000 * 60 * 60 * 24;
        return Math.floor(diferencia / dia);
    }
    console.log(`${diaDelAnho(fechaNacimiento)}`);

    // 4º Mostrar por Día de la semana.
    function nombreDiaSemana(dia: number): string {
        let diasSemana: string[] = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
        return diasSemana[dia];
    }
    console.log(`${nombreDiaSemana(fechaNacimiento.getDay())}`);

    // 5º Mostrar por Nombre del mes.
    function obtenerNombreMes(mes: number): string {
        let meses: string[] = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
        return meses[mes];
    }
    console.log(`${obtenerNombreMes(fechaNacimiento.getMonth())}`);

    // 6º Mostrar FECHA de nacimiento en forma de String
    console.log(fechaNacimiento.toLocaleDateString());

    // 7º Mostrar HORA de nacimiento en forma de String
    console.log(fechaNacimiento.toLocaleTimeString());

    // 8º Mostrar Día de la semana y día del mes
    // Con este formato le podemos especificar más parámetros y como los queremos
    console.log(`${fechaNacimiento.toLocaleDateString('es-ES', { weekday: 'long' })}, ${fechaNacimiento.getDate()}`);

    // 9º Mostrar Nombre del mes, día del mes y año
    console.log(`${fechaNacimiento.toLocaleDateString('es-ES', { month: 'long' })} ${fechaNacimiento.getDate()}, ${fechaNacimiento.getFullYear()}`);

    // 10º Mostrar Día de la semana, día del mes, nombre del mes y año abreviados
    console.log(`${fechaNacimiento.toLocaleDateString('es-ES', { weekday: 'short', month: 'short' })} ${fechaNacimiento.getDate()}, ${fechaNacimiento.getFullYear()}`);
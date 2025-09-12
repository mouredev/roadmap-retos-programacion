// Ejercicio 1

    let funcionAsincrona : (nombre : string, segundos : number) => Promise<void> = async(nombre, segundos) => {
        console.log('Se inicia la ejecución');
        console.log(`Duración de ${nombre} - ${segundos} segundos`);

        await new Promise<void>(res => {
            setTimeout(res, segundos * 1000)
        });

        console.log('Se acaba la ejecución');
    }

    let ejercicio1: () => Promise<void> = async () => {
        let promesa1: Promise<void> = funcionAsincrona('Función 1', 5)
        let promesa2: Promise<void> = funcionAsincrona('Función 2', 10)
        await Promise.all([promesa1, promesa2]);
    }

    ejercicio1();

// EJERCICIO EXTRA

    let funcionC: () => Promise<void> = async () => {
        console.log('Inicia la ejecución de la funcion C');

        await new Promise<void>(res => {
          setTimeout(res, 3000)
        });
    
        console.log('Finaliza la ejecución de la funcion C después de 3 segundos');
    }

    let funcionB: () => Promise<void> = async () => {
        console.log('Inicia la ejecución de la funcion B');

        await new Promise<void>(res => {
          setTimeout(res, 2000)
        });
    
        console.log('Finaliza la ejecución de la funcion B después de 2 segundos');
    }

    let funcionA: () => Promise<void> = async () => {
        console.log('Inicia la ejecución de la funcion A');

        await new Promise<void>(res => {
          setTimeout(res, 1000)
        });
    
        console.log('Finaliza la ejecución de la funcion A después de 1 segundos');
    }

    let funcionD: () => Promise<void> = async () => {
        console.log('Inicia la ejecución de la funcion D');

        await new Promise<void>(res => {
          setTimeout(res, 1000)
        });
    
        console.log('Finaliza la ejecución de la funcion D después de 1 segundos');
    }

    let ejercicioExtra: () => Promise<void>  = async () => {
        let respuestaC: Promise<void> = funcionC();
        let respuestaB: Promise<void> = funcionB();
        let respuestaA: Promise<void> = funcionA();
    
        await Promise.all([respuestaC, respuestaB, respuestaA])
    
        let respuestaD: void = await funcionD();
    }

    ejercicioExtra();
// 1º Ejercicio
    // Array
        // Pilas (STACKS - LIFO)
        /**
         * Se les llama LIFO (Last In First Out) porque
         * el último elemento agregado, es el primero en salir
        */
            // Creamos un Array con el que vamos a trabajar.
                let aprobados : string[] = ['Adrian', 'IgleDev'];
            // Añadimos uno nuevo a la lista
                aprobados.push('Mouredev');
            // Comprobamos la lista y el tamaño
                console.log(aprobados.length + ' - ' + aprobados);
            // Ahora tendremos que sacarlo
                aprobados.pop();
            // Comprobamos la lista y el tamaño
                console.log(aprobados.length + ' - ' + aprobados);

        // Colas (QUEUE  - FIFO)
        /**
         * Se les llama FIFO (First In First Out) porque
         * el primer elemento agregado, es el primero en salir
        */
            // Creamos un Array con el que vamos a trabajar.
                let coladelBanco : string[] = ['Adrian', 'IgleDev'];
            // Añadimos uno nuevo a la lista
                coladelBanco.push('Mouredev');
            // Comprobamos la lista y el tamaño
                console.log(coladelBanco.length + ' - ' + coladelBanco);
            // Ahora tendremos que sacar al 1º
                coladelBanco.shift();
            // Comprobamos la lista y el tamaño
                console.log(coladelBanco.length + ' - ' + coladelBanco);
    // Listas
            // Pilas (STACKS - LIFO)
            /**
             * Se les llama LIFO (Last In First Out) porque
             * el último elemento agregado, es el primero en salir
            */
                // Creamos un Array con el que vamos a trabajar.
                    let aprobadosLista : Array<string> = ['Adrian', 'IgleDev'];
                // Añadimos uno nuevo a la lista
                    aprobadosLista.push('Mouredev');
                // Comprobamos la lista y el tamaño
                    console.log(aprobadosLista.length + ' - ' + aprobadosLista);
                // Ahora tendremos que sacarlo
                    aprobadosLista.pop();
                // Comprobamos la lista y el tamaño
                    console.log(aprobadosLista.length + ' - ' + aprobadosLista);

            // Colas (QUEUE  - FIFO)
            /**
             * Se les llama FIFO (First In First Out) porque
             * el primer elemento agregado, es el primero en salir
            */
                // Creamos un Array con el que vamos a trabajar.
                    let coladelBancoLista : Array<string> = ['Adrian', 'IgleDev'];
                // Añadimos uno nuevo a la lista
                    coladelBancoLista.push('Mouredev');
                // Comprobamos la lista y el tamaño
                    console.log(coladelBancoLista.length + ' - ' + coladelBancoLista);
                // Ahora tendremos que sacar al 1º
                    coladelBancoLista.shift();
                // Comprobamos la lista y el tamaño
                    console.log(coladelBancoLista.length + ' - ' + coladelBancoLista);
// Ejercicio Extra
    // Ejercicio de Pila (STACKS - LIFO)
        class Navegador {
            historial: string[];
            actual: string;
        
            constructor() {
                this.historial = [];
                this.actual = '';
            }
        
            navegar(url: string) {
                if (url === 'atras') {
                    if (this.historial.length > 0) {
                        this.actual = this.historial.pop()!;
                        console.log('Navegando hacia atrás a:' + this.actual);
                    } else {
                        console.log('No hay páginas para retroceder.');
                    }
                } else if (url === 'adelante') {
                    console.log('No se puede navegar hacia adelante sin haber retrocedido previamente.');
                } else {
                    this.historial.push(this.actual);
                    this.actual = url;
                    console.log('Navegando a:' + this.actual);
                }
            }
        }

        let navegador = new Navegador();

        navegador.navegar("google.com");
        navegador.navegar("wikipedia.org");
        navegador.navegar("atras");
        navegador.navegar("adelante");
        navegador.navegar("facebook.com");

    // Ejercico Cola
        class Impresora {
            cola: string[];
        
            constructor() {
                this.cola = [];
            }
        
            recibirDocumento(documento: string) {
                this.cola.push(documento);
                console.log('Documento:' + documento);
            }
        
            imprimir() {
                if (this.cola.length > 0) {
                    let documento = this.cola.shift()!;
                    console.log('Imprimiendo documento:' + documento);
                } else {
                    console.log('No hay documentos en la cola para imprimir.');
                }
            }
        }
        
        let impresora = new Impresora();
        
        impresora.recibirDocumento("Documento1.txt");
        impresora.recibirDocumento("Documento2.pdf");
        impresora.imprimir();
        impresora.imprimir();
        impresora.imprimir();
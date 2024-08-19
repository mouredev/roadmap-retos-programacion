// Clases

class Nacionalidad
{
    constructor(pais, ciudad)
    {
        this.pais = pais
        this.ciudad = ciudad
    }

    mostrarNacionalidad() 
    {
        console.log(`Soy de ${this.pais} y vivo en la ciudad de ${this.ciudad}`);
    }
}


let miNacionalidad = new Nacionalidad("República Dominicana", "Santo Domingo")

miNacionalidad.mostrarNacionalidad()

// DIFICULTAD EXTRA

class Pilas
{
    constructor(pila)
    {
        this.pila = pila
    }

    push(nuevo) 
    {
        this.pila.push(nuevo)
    }

    pop()
    {
        if(this.pila.length !== 0)
        {
            this.pila.pop()
        }
        else
        {
            console.log("La pila esta vacia");
        }
    }

    peek()
    {
        if(this.pila.length !== 0)
        {
            console.log(this.pila[this.pila.length-1]);
        }
        else
        {
            console.log("La pila esta vacia");
        }
    }

    isEmpty()
    {
        console.log(this.pila.length === 0);
    }

    length()
    {
        console.log(this.pila.length);
    }

    print()
    {
        console.log(this.pila);
    }
}

let miPila = new Pilas([1, 2, 3])

miPila.push(5)
miPila.pop()
miPila.peek()
miPila.isEmpty()
miPila.length()
miPila.print()


class Colas
{
    constructor(cola)
    {
        this.cola = cola
    }

    enqueue(nuevo) 
    {
        this.cola.push(nuevo)
    }

    dequeue()
    {
        if(this.cola.length !== 0)
        {
            this.cola.shift()
        }
        else
        {
            console.log("La cola esta vacia");
        }
    }

    front()
    {
        
        if(this.cola.length !== 0)
        {
            console.log(this.cola[0]);
        }
        else
        {
            console.log("La cola esta vacia");
        }
    }

    isEmpty()
    {
        console.log(this.cola.length === 0);
    }

    length()
    {
        console.log(this.cola.length);
    }

    print()
    {
        console.log(this.cola);
    }
}

let miCola = new Colas([1, 2, 3])

miCola.enqueue(4)
miCola.dequeue()
miCola.front()
miCola.isEmpty()
miCola.length()
miCola.print()
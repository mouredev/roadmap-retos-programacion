program miguelex;

{$mode objfpc}{$H+}

// Clase

type 
    // Clase
    TVehiculo = class
        private
            nombre: string;
            numRuedas: integer;
        public
            // Constructor
            constructor create(nom: string; ruedas: integer);
            procedure MostrarInformacion;
    end;

    TPila = class
        private
            pila: array[1..100] of integer;
            tope: integer;
        public
            constructor create;
            procedure push(valor: integer);
            function pop: integer;
            procedure mostrar;
    end;

    TCola = class
        private
            cola: array[1..100] of integer;
            inicio: integer;
            fin: integer;
        public
            constructor create;
            procedure push(valor: integer);
            function pop: integer;
            procedure mostrar;
    end;

// Constructor
constructor TVehiculo.create(nom: string; ruedas: integer);
begin
    nombre := nom;
    numRuedas := ruedas;
end;

procedure TVehiculo.MostrarInformacion;
begin
  writeln('Nombre: ', nombre);
  writeln('Número de ruedas: ', numRuedas);
end;

constructor TPila.create;
begin
    tope := 0;
end;

procedure TPila.push(valor: integer);
begin
    tope := tope + 1;
    pila[tope] := valor;
end;

function TPila.pop: integer;
begin
    pop := pila[tope];
    tope := tope - 1;
end;

procedure TPila.mostrar;
var i: integer;
begin
    for i := 1 to tope do
        write(pila[i], ' ');
    writeln;
end;

constructor TCola.create;
begin
    inicio := 1;
    fin := 0;
end;

procedure TCola.push(valor: integer);
begin
    fin := fin + 1;
    cola[fin] := valor;
end;

function TCola.pop: integer;
begin
    pop := cola[inicio];
    inicio := inicio + 1;
end;

procedure TCola.mostrar;
var i: integer;
begin
    for i := inicio to fin do
        write(cola[i], ' ');
    writeln;
end;

var
    // Crear objeto
    coche: TVehiculo;
    bicicleta: TVehiculo;
    pila: TPila;
    cola: TCola;

begin

    // Crear objeto
    coche := TVehiculo.create('Coche', 4);
    bicicleta := TVehiculo.create('Bicicleta', 2);
    pila := TPila.create;
    cola := TCola.create;

    // Mostrar
    coche.MostrarInformacion;
    bicicleta.MostrarInformacion;
    
    // Liberar memoria
    coche.free();
    bicicleta.free();

    // Pila

    pila.push(1);
    pila.push(2);
    pila.push(3);

    pila.mostrar;

    pila.pop();
    pila.mostrar; 

    cola.push(1);
    cola.push(2);
    cola.push(3);

    cola.mostrar;

    cola.pop();
    cola.mostrar;

    pila.free();
    cola.free();

end.
program Enumerado;
Uses Crt;

type
    DiasSemana = (Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo);
    EstadoPedido = (PENDIENTE, ENVIADO, ENTREGADO, CANCELADO);
    Pedido = object
    private
        id : Integer;
        estado : EstadoPedido;
    public
        constructor Iniciar(Identificador: Integer);
        procedure EnviarPedido;
        procedure EntregarPedido;
        procedure CancelarPedido;
        procedure MostrarEstadoPedido;
    end;

var
    Dia: DiasSemana;
    numDia: Byte;
    pedido1, pedido2, pedido3, pedido4: Pedido;
    ids : String;

constructor Pedido.Iniciar(Identificador: Integer);
begin
    id := Identificador;
    estado := PENDIENTE
end;

procedure Pedido.EnviarPedido();
begin
    if estado = PENDIENTE then
    begin
        estado := ENVIADO;
        Str(id, ids); WriteLn('Pedido ' + ids + ' Enviado')
    end
    else
        WriteLn('No se puede enviar el pedido')
end;

procedure Pedido.EntregarPedido();
begin
    if estado = ENVIADO then
    begin
        estado := ENTREGADO;
        Str(id, ids); WriteLn('Pedido ' + ids + ' Entregado')
    end
    else
        WriteLn('No se puede entregar un pedido que no se ha enviado')
end;

procedure Pedido.CancelarPedido();
begin
    if estado = ENTREGADO then
        Writeln('No se puede cancelar el pedido porque ya fue entregado')
    else
    begin
        estado := CANCELADO;
        Str(id, ids); WriteLn('Pedido ' + ids + ' Cancelado')
    end
end;

procedure Pedido.MostrarEstadoPedido();
begin
    Str(id, ids);
    Write('Pedido ' + ids);
    case estado of
        PENDIENTE: Writeln(' : Pendiente');
        ENVIADO: WriteLn(' : Enviado');
        ENTREGADO: WriteLn(' : Entregado');
        CANCELADO: WriteLn(' : Cancelado');
    end;
end;

function getDia(const dia: Byte):DiasSemana;
begin
    getDia := DiasSemana(dia - 1);
end;

begin
    ClrScr();
    Write('Digite el numero del dia: ');
    ReadLn(numDia);
    if not (numDia in [1, 2, 3, 4, 5, 6, 7]) then
    begin
        WriteLn('El numero debe ser un numero entre 1 y 7');
        exit
    end;
    Dia := getDia(numDia);
    Write('Corresponde a: ');
    case Dia of
        Lunes: Writeln('Lunes');
        Martes: Writeln('Martes');
        Miercoles: Writeln('Miercoles');
        Jueves: Writeln('Jueves');
        Viernes: Writeln('Viernes');
        Sabado: Writeln('Sabado');
        Domingo: Writeln('Domingo');
    end;

    Writeln('');
    WriteLn('Reto Extra');
    Delay(1000);

    WriteLn('');
    WriteLn('Iniciando Pedidos');
    pedido1.Iniciar(101);
    pedido2.Iniciar(102);
    pedido3.Iniciar(103);
    pedido4.Iniciar(104);

    WriteLn('');
    WriteLn('Movimiento de Pedidos');
    pedido1.EnviarPedido();
    pedido2.EnviarPedido();
    pedido3.EntregarPedido();
    pedido4.EntregarPedido();
    pedido1.EntregarPedido();
    pedido2.EntregarPedido();
    pedido3.CancelarPedido();
    pedido1.CancelarPedido();

    WriteLn('');
    WriteLn('Tras realizar movimientos');
    pedido1.MostrarEstadoPedido();
    pedido2.MostrarEstadoPedido();
    pedido3.MostrarEstadoPedido();
    pedido4.MostrarEstadoPedido();
end.
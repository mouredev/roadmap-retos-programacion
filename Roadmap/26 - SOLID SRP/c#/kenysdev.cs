#pragma warning disable CA1050 //namespace
/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
-------------------------------------------------
* SOLID: PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP)
-------------------------------------------------
# Se centra en la claridad, la cohesión y la separación de intereses.
# Cada clase debe tener una única razón para cambiar.
# Los metodos de una clase deben estar estrechamente relacionadas.

__________________________________
* EJERCICIO:
* Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
* Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
* de forma correcta e incorrecta.
*/

// # SIN APLICAR EL PRINCIPIO:
using System.Collections.Generic;

public class NoSRP {
    private readonly List<string> customers;
    private readonly List<string> suppliers;

    public NoSRP() {
        customers = [];
        suppliers = [];
    }

    public void AddCustomer(string name) {
        customers.Add(name);
    }

    public void AddSupplier(string name) {
        suppliers.Add(name);
    }

    public void RemoveCustomer(string name) {
        customers.Remove(name);
    }

    public void RemoveSupplier(string name) {
        suppliers.Remove(name);
    }
}

// _______________________________________
// APLICANDO EL PRINCIPIO:

public class Customers {
    private readonly List<string> customers;

    public Customers() {
        customers = [];
    }

    public void Add(string name) {
        customers.Add(name);
    }

    public void Remove(string name) {
        customers.Remove(name);
    }
}

public class Suppliers {
    private readonly List<string> suppliers;

    public Suppliers() {
        suppliers = [];
    }

    public void Add(string name) {
        suppliers.Add(name);
    }

    public void Remove(string name) {
        suppliers.Remove(name);
    }
}

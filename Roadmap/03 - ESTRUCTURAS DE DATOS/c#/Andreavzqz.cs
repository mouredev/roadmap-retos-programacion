using System;
using System.Collections.Generic;


class Program
{
    static void Main (string[] args)
    {
        //LISTA
        List<int> myList = new List<int> { 3, 1, 4, 1, 5, 9 };
        myList.Add(2);  // Insercion
        myList.Remove(1); // Borrado (elimina la primera aparicion del 1)
        myList[2] = 8; // Actualizacion
        myList.Sort(); // Orientacion
        console.WriteLine("Lista " + string.Join(", " , myList));

        //CONJUNTO(hashSet)
        HashSet<int> mySet = new HashSet<int> { 3, 1, 4, 1, 5, 9};
        mySet.Add(2); // Insercion
        mySet.Remove(1); //Borrado 
        // Los conjuntos no tienen una actualización directa, se puede eliminar y volver a agregar
        mySet.Remove(9);
        mySet.Add(9);
        // Ordenación no aplicable directamente a conjuntos, pero podemos convertir a lista para ordenación
        List<int> sortedSet = new List<int>(mySet);
        sortedSet.Sort();
        console.WriteLine("Conjunto " + string.Join(", ", sortedSet));

        //PILA
        Stack<int> myStack = new Stack<int>();
        myStack.Push(3); // Insercion
        myStack.Push(1); 
        myStack.Push(4);
        int top = myStack.Pop(); // Borrado
        console.WriteLine("Pila: " + string.Join(", ", myStack));

        //COLA
        Queue<int> myQueue = new Queue<int>();
        myQueue.Enqueue(3); // Insercion
        myQueue.Enqueue(1);
        myQueue.Enqueue(4);
        int front = myQueue.Dequeue(); // Borrado
        console.WriteLine("Cola: " + string.Join(", ", myQueue));

        //DICCIONARIO
        Dictionary<string, int> myDict = new Dictionary<string, int>();
        myDict["a"] = 3; // Insercion
        myDict["b"] = 1;
        myDict["c"] = 4;
        myDict["d"] = 8; // Actualizacion
        myDict.Remove("b"); // Borrado
        foreach (var kvp in myDict)
        {
            console.WriteLine("Diccionario: {0} = {1}", kvp.Key, kvp.Value);
        }

        //ARRAY
        int[] myArray = {3, 1, 4, 1, 5, 9};
        Array.Sort(myArray); // Ordenacion
        myArray[2] = 8; // Actualizacion
        console.WriteLine("Array: " + string.Join(", ", myArray));

        //LINKEDLIST
        LinkedList<int> myLinkedList = new LinkedList<int>(new int[] { 3, 1, 4, 1, 5, 9});
        myLinkedList.AddLast(2); // Insercion
        myLinkedList.Remove(1); // Borrado
        var node = myLinkedList.Find(4);
        if (node != null)
        {
            myLinkedList.AddAfter(node, 8); // Actualizacion simulada
        }
        // LinkedList no tiene un metodo de ordenacion nativo
        myList<int> sortedLinkedList = new myList<int>(myLinkedList);
        sortedLinkedList.Sort();
        console.WriteLine("LinkedList: " + string.Join(", ", sortedLinkedList));

    }

/*
Explicación:

List:
Inserción: Add
Borrado: Remove
Actualización: Acceder por índice y asignar
Ordenación: Sort

HashSet:
Inserción: Add
Borrado: Remove
Actualización: No aplicable directamente, se simula con Remove y Add
Ordenación: Convertir a List y usar Sort

Stack:
Inserción: Push
Borrado: Pop

Queue:
Inserción: Enqueue
Borrado: Dequeue

Dictionary:
Inserción: Asignación a una clave
Borrado: Remove
Actualización: Asignación a una clave

Array:
Actualización: Acceder por índice y asignar
Ordenación: Array.Sort

LinkedList:
Inserción: AddLast
Borrado: Remove
Actualización: No aplicable directamente, se simula con AddAfter
Ordenación: Convertir a List y usar Sort
*/

}

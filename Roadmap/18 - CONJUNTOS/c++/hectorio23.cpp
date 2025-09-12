// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23
#include <iostream>
#include <algorithm>
#include <iterator>
#include <set>
#include <vector>
#include <map>

/*
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
*/

// Funcion lambda que permite imprimir los elementos
// que confirman un SET
auto print = [](std::set<int> &conjunto) -> void {
    int counter = 0;
    for (auto &elemento : conjunto) {

        if (counter != conjunto.size() - 1) std::cout << elemento << ", ";
        else std::cout << elemento << ".";
        counter++;
    }
    std::cout << "\n";
};

// Clase custom que permite operar los set como en Python, es decir, 
// nos habilita para realizar ciertas operaciones usando operadores 
// especiales en lugar de usar métodos
class SetCustom {
public:
    std::set<int> values;

    /********************************
    ********* CONSTRUCTORES *********
    *********************************/
    SetCustom(){};
    SetCustom(int value) { values.insert(value); };
    SetCustom(std::set<int> new_set): values(new_set) {  };
    SetCustom(std::vector<int> items) {
        for (auto &element : items)
        values.insert(element);
    };

    /********************************
    ************* MÉTODOS ***********
    *********************************/

    void insert(int value) { values.insert(value); };
    void insert(std::vector<int> items) {
        for (auto &element : items)
        values.insert(element);
    };

    // Calcular la diferencia del subset
    SetCustom operator-(SetCustom &other) {
        std::vector<int> result;
        int index, counter = 0;
        SetCustom tmp;

        // Se encarga de comparar cada elemento de un Set con todos los elementos
        // del segundo set con el objetivo de verificar que no se repita en el segundo, 
        // cuando un elemento no se repite, lo guarda en un vector.
        for (auto &element : other.values) {
            counter = 0;
            for (auto &item : this->values) {

                if (element == item) break;
                counter++;

                if (counter == values.size() - 1) {
                    result.push_back(element);
                    index++;
                }
            }
        }

        if (result.size() != 0) tmp.insert(result);

        // Retorna un objeto de la clase SetCustom con los valores que no se interceptan
        // del primer Set de datos del operando 
        return tmp;
    }

    // Realiza la union de los conjuntos y los retorna empaquetados
    // en el objeto SetCustom
    SetCustom operator+(SetCustom &other) {
        std::set<int> tmp_set { this->values };
        tmp_set.merge(other.values);

        return SetCustom(tmp_set);
    }

    // Realiza la interseccion de los conjuntos y los retorna empaquetados
    // en el objeto SetCustom
    SetCustom operator&(SetCustom &other) {
        std::set<int> intersection;
        std::set_intersection(other.values.begin(), other.values.end(), this->values.begin(), this->values.end(), 
        std::inserter(intersection, intersection.begin()));

        return SetCustom(intersection);
    }

    // Realiza la diferencia simétrica de los conjuntos y los retorna empaquetados
    // en el objeto SetCustom
    SetCustom operator^(SetCustom &other) {
        std::set<int> symmetric_difference;
        std::set_symmetric_difference(this->values.begin(), this->values.end(), other.values.begin(), other.values.end(), std::inserter(symmetric_difference, symmetric_difference.begin()));

        return SetCustom(symmetric_difference);
    }
};

int main() {
    std::map<int, int> myMap;

    // Añade un elemento al final
    myMap[1] = 10;

    // Añade un elemento al principio
    myMap[0] = 5;

    // Añade varios elementos en bloque al final
    std::map<int, int> additionalMap = {{2, 20}, {3, 30}};
    myMap.insert(additionalMap.begin(), additionalMap.end());

    // Añade varios elementos en bloque en una posición concreta
    std::map<int, int> blockInsertMap = {{4, 40}, {5, 50}};
    myMap.insert({56, 9, });

    // Elimina un elemento en una posición concreta
    myMap.erase(3);

    // Actualiza el valor de un elemento en una posición concreta
    myMap[2] = 25;

    // Comprueba si un elemento está en un conjunto
    if (myMap.find(4) != myMap.end()) {
        std::cout << "El elemento 4 está en el conjunto." << std::endl;
    } else {
        std::cout << "El elemento 4 no está en el conjunto." << std::endl;
    }

    // Elimina todo el contenido del conjunto
    myMap.clear();
    
    // Se crean los objetos con los que se va a estar trabajando a lo largo del ejercicio
    // Setcustom es una clase custom que nos permite operar con conjutnos de una manera más flexible
    SetCustom value1 = std::vector<int>{1, 2, 4, 5, 6, 7};
    SetCustom value2 = std::vector<int>{1, 2, 46, 5, 6, 7};

    // Se imrpimen el SET1 antes de ser modificado
    std::cout << "Set1 antes de ser modificado: \n";
    print(value1.values);

    // insertar un dato al final del SET1
    std::cout << "Set1 despues de agregar un elemento al final: \n";
    value1.insert(239);
    print(value1.values);

    // Insertar varios elementos al final del SET2
    std::cout << "Set1 despues de agregar un conjunto de elementos al final: \n";
    value1.insert({ 500, 674, 786, 8493 });
    print(value1.values);

    std::cout << "\n****** CONJUNTOS A {1, 2, 4, 5, 6, 7} y B {1, 2, 46, 5, 6, 7} *******\n\n";

    std::cout << "* Diferencia de conjuntos A y B: -> ";
    SetCustom value3 = value1 - value2;
    print(value3.values);

    std::cout << "* Union de conjuntos A y B: -> ";
    value3 = value1 + value2;
    print(value3.values);

    std::cout << "* Interseccion de conjuntos A y B: -> ";
    value3 = value1 & value2;
    print(value3.values);

    std::cout << "* Diferencia simetrica de conjuntos A y B: -> ";
    value3 = value1 ^ value2;
    print(value3.values);

    return 0;
}
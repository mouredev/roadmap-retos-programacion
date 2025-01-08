/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* CONJUNTOS
-----------------------------------------
*/

use std::collections::HashSet;
fn main() {
    // Conjuntos
    // Son una colección desordenada de elementos únicos.
    let mut my_set: HashSet<i32> = vec![1, 2, 3, 0].into_iter().collect();

    // EJERCICIO #1:
    // Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
    // operaciones (debes utilizar una estructura que las soporte):

    // NOTA: - Algunas operaciones del ejercicio no pueden realizarse utilizando 'HashSet'.

    let mut my_list: Vec<String> = vec![
        "a".to_string(), 
        "b".to_string(), 
        "c".to_string()
    ];

    // Añade un elemento al final.
    my_list.push("d".to_string());

    // Añadir un elemento al principio
    my_list.insert(0, "-".to_string());

    // Añadir varios elementos en bloque al final
    my_list.extend(vec!["e".to_string(), "f".to_string()]);

    // Añadir varios elementos en bloque en una posición concreta
    my_list.splice(4..4, vec!["-".to_string(), ">".to_string()]);

    // Eliminar un elemento en una posición concreta
    my_list.remove(5);

    // Actualizar el valor de un elemento en una posición concreta
    my_list[2] = "-b".to_string();

    // Mostrar la lista
    println!("Elementos de la lista:");
    println!("{:?}", my_list);

    // Comprueba si un elemento está en un conjunto
    println!("4 en conjunto: {}", my_set.contains(&4));

    println!("'c' en lista: {}", my_list.contains(&"c".to_string()));

    // Elimina todo el contenido del conjunto y la lista.
    my_set.clear();
    my_list.clear();

    // EJERCICIO #2:
    // Muestra ejemplos de las siguientes operaciones con conjuntos:
    // - Unión.
    // - Intersección.
    // - Diferencia.
    // - Diferencia simétrica.

    let set1: HashSet<i32> = vec![1, 2, 3, 4].into_iter().collect();
    let set2: HashSet<i32> = vec![3, 4, 5, 6].into_iter().collect();

    println!(
        "\n* set_1: {:?} - set_2: {:?}",
        set1, set2
    );

    // Unión
    // Elementos que están en al menos uno de los conjuntos.
    let union: HashSet<i32> = set1.union(&set2).cloned().collect();
    println!("\n- Union: {:?}", union);

    // Intersección
    // Elementos que están en ambos conjuntos.
    let intersection: HashSet<i32> = set1.intersection(&set2).cloned().collect();
    println!("\n- Intersection: {:?}", intersection);

    // Diferencia
    // Elementos que están en set_1 pero no en set_2
    let difference: HashSet<i32> = set1.difference(&set2).cloned().collect();
    println!("\n- Difference: {:?}", difference);

    // Diferencia simétrica
    // Elementos que están en uno de los conjuntos pero no en ambos.
    let symmetric_diff: HashSet<i32> = set1.symmetric_difference(&set2).cloned().collect();
    println!("\n- Symmetric Difference: {:?}", symmetric_diff);
}

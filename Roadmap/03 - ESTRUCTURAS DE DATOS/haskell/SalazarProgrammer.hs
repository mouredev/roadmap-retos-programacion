{-
 * EJERCICIO:
 * - Estructuras de datos soportadas por defecto
 * - Operaciones: inserción, borrado, actualización, ordenación
-}

module Main where

import Data.List (sort, delete, insert, nub)
import Data.Map (Map)
import qualified Data.Map as Map
import qualified Data.Set as Set
import Control.Monad (forever)
import System.Exit (exitSuccess)

-- 1. LISTAS (la estructura más común en Haskell)
ejemploListas :: IO ()
ejemploListas = do
    putStrLn "\n=== LISTAS ==="
    let lista = [1, 2, 3, 4, 5]
    putStrLn $ "Lista original: " ++ show lista

    -- Inserción
    let listaInsertada = 0 : lista  -- Al inicio
    putStrLn $ "Inserción al inicio: " ++ show listaInsertada

    let listaInsertada2 = lista ++ [6]  -- Al final
    putStrLn $ "Inserción al final: " ++ show listaInsertada2

    let listaInsertada3 = insert 3 lista  -- En posición ordenada
    putStrLn $ "Inserción ordenada: " ++ show listaInsertada3

    -- Borrado
    let listaBorrada = delete 3 lista  -- Elimina primera ocurrencia
    putStrLn $ "Borrado del 3: " ++ show listaBorrada

    -- Actualización (las listas son inmutables, creamos una nueva)
    let listaActualizada = take 2 lista ++ [99] ++ drop 3 lista
    putStrLn $ "Actualización (posición 2 a 99): " ++ show listaActualizada

    -- Ordenación
    let listaDesordenada = [5, 2, 8, 1, 9]
    putStrLn $ "Ordenación: " ++ show (sort listaDesordenada)

-- 2. TUPLAS
ejemploTuplas :: IO ()
ejemploTuplas = do
    putStrLn "\n=== TUPLAS ==="
    let tupla = (1, "Hola", True)
    putStrLn $ "Tupla: " ++ show tupla

    -- Las tuplas son inmutables, no se pueden modificar directamente
    -- Se crean nuevas tuplas para "actualizar"
    let tuplaActualizada = (fst tupla + 1, snd tupla, not (thrd tupla))
        where thrd (_, _, x) = x
    putStrLn $ "Tupla 'actualizada': " ++ show tuplaActualizada

-- 3. CONJUNTOS (Set)
ejemploConjuntos :: IO ()
ejemploConjuntos = do
    putStrLn "\n=== CONJUNTOS ==="
    let conjunto = Set.fromList [1, 2, 3, 3, 2, 1]  -- Elimina duplicados
    putStrLn $ "Conjunto: " ++ show (Set.toList conjunto)

    -- Inserción
    let conjuntoInsertado = Set.insert 4 conjunto
    putStrLn $ "Inserción del 4: " ++ show (Set.toList conjuntoInsertado)

    -- Borrado
    let conjuntoBorrado = Set.delete 2 conjunto
    putStrLn $ "Borrado del 2: " ++ show (Set.toList conjuntoBorrado)

-- 4. MAPAS/DICCIONARIOS (Map)
ejemploMapas :: IO ()
ejemploMapas = do
    putStrLn "\n=== MAPAS ==="
    let mapa = Map.fromList [("Juan", 25), ("Maria", 30), ("Pedro", 35)]
    putStrLn $ "Mapa: " ++ show (Map.toList mapa)

    -- Inserción
    let mapaInsertado = Map.insert "Ana" 28 mapa
    putStrLn $ "Inserción de Ana: " ++ show (Map.toList mapaInsertado)

    -- Borrado
    let mapaBorrado = Map.delete "Juan" mapa
    putStrLn $ "Borrado de Juan: " ++ show (Map.toList mapaBorrado)

    -- Actualización
    let mapaActualizado = Map.adjust (+1) "Maria" mapa
    putStrLn $ "Actualización de Maria (+1): " ++ show (Map.toList mapaActualizado)

    -- Búsqueda
    case Map.lookup "Pedro" mapa of
        Just edad -> putStrLn $ "Edad de Pedro: " ++ show edad
        Nothing -> putStrLn "Pedro no encontrado"

-- 5. ARRAYS (menos comunes, pero disponibles)
ejemploArrays :: IO ()
ejemploArrays = do
    putStrLn "\n=== ARRAYS ==="
    -- Los arrays son inmutables y de tamaño fijo
    let array = listArray (0, 4) [10, 20, 30, 40, 50] :: Array Int Int
    putStrLn $ "Array: " ++ show (elems array)

    -- "Actualización" creando nuevo array
    let arrayActualizado = array // [(2, 99)]
    putStrLn $ "Array actualizado (posición 2): " ++ show (elems arrayActualizado)

-- DIFICULTAD EXTRA: Agenda de contactos
type Agenda = Map.Map String String

agendaContactos :: IO ()
agendaContactos = do
    putStrLn "\n=== AGENDA DE CONTACTOS ==="
    putStrLn "Operaciones disponibles:"
    putStrLn "1. Buscar contacto"
    putStrLn "2. Insertar contacto"
    putStrLn "3. Actualizar contacto"
    putStrLn "4. Eliminar contacto"
    putStrLn "5. Mostrar todos los contactos"
    putStrLn "6. Salir"

    let loop agenda = do
            putStr "\nSelecciona una operación (1-6): "
            opcion <- getLine

            case opcion of
                "1" -> buscarContacto agenda >>= loop
                "2" -> insertarContacto agenda >>= loop
                "3" -> actualizarContacto agenda >>= loop
                "4" -> eliminarContacto agenda >>= loop
                "5" -> mostrarContactos agenda >>= loop
                "6" -> putStrLn "¡Hasta luego!" >> exitSuccess
                _   -> putStrLn "Opción no válida" >> loop agenda

    loop Map.empty

buscarContacto :: Agenda -> IO Agenda
buscarContacto agenda = do
    putStr "Nombre a buscar: "
    nombre <- getLine
    case Map.lookup nombre agenda of
        Just telefono -> putStrLn $ nombre ++ ": " ++ telefono
        Nothing -> putStrLn "Contacto no encontrado"
    return agenda

insertarContacto :: Agenda -> IO Agenda
insertarContacto agenda = do
    putStr "Nombre: "
    nombre <- getLine
    putStr "Teléfono: "
    telefono <- getLine

    if validarTelefono telefono then do
        if Map.member nombre agenda
            then putStrLn "¡El contacto ya existe! Usa actualizar."
            else putStrLn "Contacto agregado."
        return $ Map.insert nombre telefono agenda
    else do
        putStrLn "Teléfono no válido. Debe ser numérico y tener 10 dígitos."
        return agenda

actualizarContacto :: Agenda -> IO Agenda
actualizarContacto agenda = do
    putStr "Nombre a actualizar: "
    nombre <- getLine
    if Map.member nombre agenda then do
        putStr "Nuevo teléfono: "
        telefono <- getLine
        if validarTelefono telefono then do
            putStrLn "Contacto actualizado."
            return $ Map.insert nombre telefono agenda
        else do
            putStrLn "Teléfono no válido."
            return agenda
    else do
        putStrLn "Contacto no encontrado."
        return agenda

eliminarContacto :: Agenda -> IO Agenda
eliminarContacto agenda = do
    putStr "Nombre a eliminar: "
    nombre <- getLine
    if Map.member nombre agenda then do
        putStrLn "Contacto eliminado."
        return $ Map.delete nombre agenda
    else do
        putStrLn "Contacto no encontrado."
        return agenda

mostrarContactos :: Agenda -> IO Agenda
mostrarContactos agenda = do
    if Map.null agenda then
        putStrLn "La agenda está vacía."
    else do
        putStrLn "\n--- CONTACTOS ---"
        mapM_ (\(nombre, telefono) -> putStrLn $ nombre ++ ": " ++ telefono)
              (Map.toList agenda)
    return agenda

validarTelefono :: String -> Bool
validarTelefono telefono =
    length telefono == 10 && all (`elem` "0123456789") telefono

-- Función principal
main :: IO ()
main = do
    -- Ejemplos de estructuras de datos
    ejemploListas
    ejemploTuplas
    ejemploConjuntos
    ejemploMapas
    ejemploArrays

    -- Ejecutar agenda de contactos
    agendaContactos

-- Fin del programa

## 23 - SINGLETON
'''
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */
'''
## refactoring -- guru

## SINGLETON: unica instancia de una clase
'''
Ejercicio
'''


class Singleton:

    _instance = None

    def __new__(cls):
        # Estructura común para implementar Singleton
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance
    
singleton_1 = Singleton()
singleton_2 = Singleton()

print(singleton_1 is singleton_2) # Es la misma clase




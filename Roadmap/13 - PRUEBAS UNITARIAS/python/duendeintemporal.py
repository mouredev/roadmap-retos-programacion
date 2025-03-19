#13 { Retos para Programadores } PRUEBAS UNITARIAS

# Bibliography reference
# Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
#Python Notes for Professionals. 800+ pages of professional hints and tricks (GoalKicker.com) (Z-Library)
# Additionally, I use GPT as a reference and sometimes to correct or generate proper comments.

"""  
* EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos. 
 
 """

from datetime import datetime

# Short for print
log = print

def assert_condition(condition, message, errors):
    """Custom assert function that logs an error instead of throwing."""
    if not condition:
        log(message)
        errors.append(message)  # Collect the error message

def sum_numbers(a, b):
    """Returns the sum of two numbers, raises TypeError if arguments are not numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Both arguments must be numbers')
    return a + b

def test_sum(errors):
    """Tests the sum_numbers function."""
    assert_condition(sum_numbers(2, 3) == 5, 'Error: 2 + 3 should be 5', errors)
    assert_condition(sum_numbers(-1, 1) == 0, 'Error: -1 + 1 should be 0', errors)
    assert_condition(sum_numbers(0, 0) == 0, 'Error: 0 + 0 should be 0', errors)

    try:
        sum_numbers(2, '3')  # Caught an error: Both arguments must be numbers
    except Exception as e:
        log('Caught an error:', e)  # Log the caught error
        assert_condition(isinstance(e, TypeError), 'Error: Invalid argument type not handled', errors)
        assert_condition(str(e) == 'Both arguments must be numbers', 'Error: Argument type mismatch', errors)

    log('All sum tests have been executed.') # All sum tests have been executed.

personal_info = {
    "name": "Niko Zen",
    "age": 41,
    "birth_date": "1983/08/08",
    "programming_languages": ["JavaScript", "Python", "Rust", "Ruby", "Java"]
}

def test_personal_info(obj, errors):
    """Tests the personal information object."""
    if not obj:
        log('The obj is empty, skipping personal info tests.')
        return

    # Check that all fields exist
    assert_condition('name' in obj, 'Missing field "name"', errors)
    assert_condition('age' in obj, 'Missing field "age"', errors)
    assert_condition('birth_date' in obj, 'Missing field "birth_date"', errors)
    assert_condition('programming_languages' in obj, 'Missing field "programming_languages"', errors)

    # Check data types
    assert_condition(isinstance(obj['name'], str), '"name" must be a string', errors)
    assert_condition(isinstance(obj['age'], (int, float)), '"age" must be a number', errors)

    # Check if birth_date is a valid date
    try:
        birth_date = datetime.strptime(obj['birth_date'], '%Y/%m/%d')
        assert_condition(birth_date is not None, '"birth_date" must be a valid Date', errors)
    except ValueError:
        assert_condition(False, '"birth_date" must be a valid Date', errors)

    assert_condition(isinstance(obj['programming_languages'], list), '"programming_languages" is not an array', errors)

    # Validate each programming language
    for lang in obj['programming_languages']:
        assert_condition(isinstance(lang, str), 'Each language must be a string', errors)

    # Check fields are not empty
    assert_condition(len(obj['name']) > 0, '"name" cannot be empty', errors)
    assert_condition(obj['age'] > 0, '"age" must be greater than 0', errors)
    assert_condition(len(obj['birth_date']) > 0, '"birth_date" cannot be empty', errors)
    assert_condition(len(obj['programming_languages']) > 0, '"programming_languages" should have at least one language', errors)

    log('All personal info tests have been executed.') # All personal info tests have been executed.

nikita_info = {}

errors = []
test_sum(errors)
test_personal_info(personal_info, errors)  # Should pass
test_personal_info(nikita_info, errors)  # The obj is empty, skipping personal info tests.

# Log all collected errors at the end
if errors:
    log('Errors encountered during tests:')
    for error in errors:
        log(error)
else:
    log('No errors encountered during tests.') # No errors encountered during tests.

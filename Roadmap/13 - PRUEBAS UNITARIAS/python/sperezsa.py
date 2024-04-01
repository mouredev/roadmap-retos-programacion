#13 - PRUEBAS UNITARIAS

def sum(a,b):
    assert(type(a) == int)
    assert(type(b) == int)
    return a+b

def test_sum_invalid_type_number():
    sum(3,'c')

def test_sum_invalid_result():
    assert(sum(3,2)==6)

# test OK 
print(sum(2,3))

# test KOs
test_sum_invalid_type_number()
test_sum_invalid_result()


"""
Extra
"""

datos = {
    "nombres": "Sergio",
    "edad": 44,
    "fx_nacimiento": "08/09/1979",
    "lenguajes": ["Python", "Java", "JavaScript"]
    }

def test_exist_fields(datos): 
    claves = ["nombre", "edad", "fx_nacimiento", "lenguajes"]
    for clave in claves:
      if clave not in datos:
        return False
    return True

def test_exist_data():
    assert not (datos["nombre"] is None)
    assert not (datos["edad"] is None)
    assert not (datos["fx_nacimiento"] is None)
    assert not (datos["lenguajes"] == [])

def test_correct_type_data():
    assert (isinstance(datos["nombre"], str))
    assert (isinstance(datos["edad"], int))
    assert (isinstance(datos["fx_nacimiento"], str))    
    assert (isinstance(datos["lenguajes"], list))


# test para revisar si las claves están presentes en el diccionario
assert (test_exist_fields(datos))

# test para revisar que los campos no están vacíos
assert not (test_exist_data())

# test para revisar que los campos tienen el tipo de dato correcto
assert not (test_correct_type_data())
    


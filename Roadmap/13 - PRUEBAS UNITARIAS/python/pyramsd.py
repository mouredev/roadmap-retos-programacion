# Correr en consola:
# pytest pyramsd.py

def suma_nums(a, b):
    return a + b


def test_sumas():
        assert suma_nums(1, 2) == 3
        assert suma_nums(-1, 4) == 3
        assert suma_nums(4, -7) == -3
        assert suma_nums(-4, -3) == -7
        assert suma_nums(1.5, 1.5) == 3


'''
EXTRA
'''

def diccionario(name, age, birth_date, programming_languages):
      return dict(name=name, age=age, birth_date=birth_date, programming_languages=programming_languages)


def test_existen_campos():
      datos = diccionario('Sergio', 18, '07/12/2005', ['Python', 'Java', 'C++'])
      assert 'name' in datos
      assert 'age' in datos
      assert 'birth_date' in datos
      assert 'programming_languages' in datos

def test_datos_correctos():
      name = 'Sergio'
      age = 18
      birth_date = '07/12/2005'
      programming_languages = ['Python', 'Java', 'C++']
      datos = diccionario('Sergio', 18, '07/12/2005', ['Python', 'Java', 'C++'])
      assert datos['name'] == name
      assert datos['age'] == age
      assert datos['birth_date'] == birth_date
      assert datos['programming_languages'] == programming_languages

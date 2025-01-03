#  * EJERCICIO:
#  * Crea una función que se encargue de sumar dos números y retornar
#  * su resultado.
#  * Crea un test, utilizando las herramientas de tu lenguaje, que sea
#  * capaz de determinar si esa función se ejecuta correctamente.
def sum(a, b)
  a + b
end

require 'test/unit'
class TestMethod < Test::Unit::TestCase
  def test_sum
    assert_equal(4, sum(2, 2))
  end

  def test_fail
    assert_equal(5, sum(2, 2))
  end
end

require 'minitest/autorun'

class TestSum < Minitest::Test
  def test_suma
    assert_equal 5, sum(2, 3)
    assert_equal 0, sum(-1, 1)
    assert_equal 0, sum(0, 0)
    assert_equal 10, sum(3, 3)
  end
end

#  * DIFICULTAD EXTRA (opcional):
#  * Crea un diccionario con las siguientes claves y valores:
#  * "name": "Tu nombre"
#  * "age": "Tu edad"
#  * "birth_date": "Tu fecha de nacimiento"
#  * "programming_languages": ["Listado de lenguajes de programación"]
#  * Crea dos test:
#  * - Un primero que determine que existen todos los campos.
#  * - Un segundo que determine que los datos introducidos son correctos.

# Doc MiniTest: https://www.rubydoc.info/github/seattlerb/minitest/Minitest/Assertions

require 'date'
class TestPersonalInformation < Minitest::Test
  def setup
    @personal_information = { name: "Joen Doe",
                              age: 28,
                              birth_date: Date.parse("01-01-1995"),
                              programming_languages: ["Ruby", "Python", "JavaScript"] }
  end

  def test_information_exists
    assert_includes @personal_information, :name
    assert_includes @personal_information, :age
    assert_includes @personal_information, :birth_date
    assert_includes @personal_information, :programming_languages
  end

  def test_information_is_correct
    assert_instance_of String, @personal_information[:name]
    assert_instance_of Integer, @personal_information[:age]
    assert_instance_of Date, @personal_information[:birth_date]
    assert_instance_of Array, @personal_information[:programming_languages]
  end
end

#  * EJERCICIO:
#  * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
#  * implemente una superclase Animal y un par de subclases Perro y Gato,
#  * junto con una función que sirva para imprimir el sonido que emite cada Animal.
class Animal
  def initialize(name)
    @name = name
  end

  def sound
    "#{@name} says:"
  end
end


class Dog < Animal
  def sound
    puts super + " Woof!"
  end
end

class Cat < Animal
  def sound
    puts super + " Meow!"
  end
end

class Pig < Animal
  def sound
    puts super + " Oink!"
  end
end

my_dog = Dog.new('Firulais')
my_dog.sound
my_cat = Cat.new('Garfield')
my_cat.sound
my_pig = Pig.new('Porky')
my_pig.sound

#  * DIFICULTAD EXTRA (opcional):
#  * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
#  * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
#  * Cada empleado tiene un identificador y un nombre.
#  * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
#  * actividad, y almacenan los empleados a su cargo.

class Employee
  attr_accessor :id, :name

  def initialize(id, name)
    @id = id
    @name = name
    @employees = []
  end

  def add_employee(employee)
    @employees << employee
  end

  def print_employees
    puts "Employees of #{name}"
    @employees.each do |employee|
      puts "Employee: #{employee.id} - #{employee.name}"
    end
  end
end

class Manager < Employee
  def cordinate_project
    puts "#{@name} is coordinating the projects"
  end
end

class ProjectManager < Employee
  def initialize(id, name, project)
    super(id, name)
    @project = project
  end

  def cordinate_project
    puts "#{@name} is coordinating the #{@project} project"
  end
end

class Programmer < Employee
  def initialize(id, name, lenguage)
    super(id, name)
    @lenguage = lenguage
  end

  def write_code
    puts "#{@name} is writing code in #{@lenguage}"
  end

  def add_employee(employee)
    puts "Programmers can't add employees #{employee.name}"
  end

  def print_employees
    puts "Programmers can't have employees"
  end
end

manager = Manager.new(1, 'John Doe')
project_manager = ProjectManager.new(4, 'Jack Doe', 'Alpha')
programmer = Programmer.new(7, 'Jane Doe', 'Ruby')
programmer2 = Programmer.new(8, 'Elmer Doa', 'Python')

manager.cordinate_project
manager.add_employee(project_manager)

project_manager.cordinate_project
project_manager.add_employee(programmer)
project_manager.add_employee(programmer2)

programmer.write_code
programmer.add_employee(programmer2)
programmer2.write_code

manager.print_employees
project_manager.print_employees
programmer.print_employees
'''
Original file is located at
    https://colab.research.google.com/drive/1WALB50MrWbmuH-8tQuNXw4bC2UJEqNha

/*
 * EJERCICIO:
 * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026!
 * ¿Alguien se entera de todas las relaciones de parentesco
 * entre personajes que aparecen en la saga?
 * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
 * Requisitos:
 * 1. Estará formado por personas con las siguientes propiedades:
 *    - Identificador único (obligatorio)
 *    - Nombre (obligatorio)
 *    - Pareja (opcional)
 *    - Hijos (opcional)
 * 2. Una persona sólo puede tener una pareja (para simplificarlo).
 * 3. Las relaciones deben validarse dentro de lo posible.
 *    Ejemplo: Un hijo no puede tener tres padres.
 * Acciones:
 * 1. Crea un programa que permita crear y modificar el árbol.
 *    - Añadir y eliminar personas
 *    - Modificar pareja e hijo
 * 2. Podrás imprimir el árbol (de la manera que consideres).
 *
 * NOTA: Ten en cuenta que la complejidad puede ser alta si
 * se implementan todas las posibles relaciones. Intenta marcar
 * tus propias reglas y límites para que te resulte asumible.
 */
'''

import uuid

#clase familia
class Familia:
  def __init__(self, apellido):
    self.apellido = apellido
    self.miembros = []
    self.id = str(uuid.uuid4())

  def agregar_miembro(self, miembro):
    self.miembros.append(miembro)

  def total_miembros(self):
    return len(self.miembros)

  def parentesco(self, afinidad, person):
    self.relaciones[afinidad].append(person)

#clase person
class Person(Familia):
  def __init__(self, nombre, apellido_paterno, apellido_materno, edad, sexo, vivo):
    super().__init__(apellido_paterno)
    self.nombre = nombre
    self.apellido_paterno = apellido_paterno
    self.apellido_materno = apellido_materno
    self.edad = edad
    self.sexo = sexo
    self.vivo = vivo
    self.relaciones = {
        "padre":[],
        "madre":[],
        "hijos":[],
        "esposas":[],
        "hijas":[],
        "hermanos":[]
    }
    self.id = str(uuid.uuid4())

  def vive(self, estado):
    self.vivo = estado

  def informacion_personal(self):
    data = {
        "nombres":self.nombre,
        "primer apellido":self.apellido_paterno,
        "segundo apellido":self.apellido_materno,
        "edad":self.edad,
        "sexo":self.sexo,
        "vive": "vive" if self.vivo == 1 else "muerto",
        "hijos": [f'{h.nombre} {h.apellido_paterno}' for h in self.relaciones['hijos']],
        "esposas": [f'{e.nombre} {e.apellido_paterno}' for e in self.relaciones['esposas']],
        "hermanos": [f'{her.nombre} {her.apellido_paterno}' for her in self.relaciones['hermanos']],

    }
    return data

title_header = '''
    HOUSE OF THE DRAGON
  =======================
    Familia TARGARYEN
  =======================
'''

#primer rey the conquest
p1 = Person('aergon','targaryen','',23,'hombre',1)
p1.agregar_miembro(p1)
#hermanas
p2 = Person('rhaenys','targaryen','',19,'mujer',1)
p3 = Person('visenya','targaryen','',19,'mujer',1)
p1.parentesco('hermanos',p2)
p1.parentesco('hermanos',p3)
p1.agregar_miembro(p2)
p1.agregar_miembro(p3)
#esposas
p1.parentesco('esposas',p2)
p1.parentesco('esposas',p3)

#hijos con rhaenys targaryen
p4 = Person('aenys I','targaryen','',19,'hombre',1)
p1.parentesco('hijos', p4)
p4.parentesco('madre',p2)
p1.agregar_miembro(p4)
#esposa de aenys I targaryen
p6 = Person('alyssa','velaryon','',16,'mujer',1)
p4.parentesco('esposas',p6)
p1.agregar_miembro(p6)
#hijos de aenys I targaryen y alyssa velaryon
p7 = Person('rhaena','targaryen','velaryon',18,'mujer',1)
p8 = Person('aegon','targaryen','velaryon',16,'hombre',0)
p9 = Person('viserys','targaryen','velaryon',14,'hombre',0)
p10 = Person('jaehaerys I','targaryen','velaryon',14,'hombre',1)
p11 = Person('alysanne','targaryen','velaryon',15,'mujer',1)
for hijo in [p7,p8,p9,p10,p10]:
  p4.parentesco('hijos', hijo)
  p6.parentesco('hijos', hijo)
  hijo.parentesco('padre', p4)
  hijo.parentesco('madre', p6)
  p1.agregar_miembro(hijo)

#hermanos
hijos = [p7,p8,p9,p10,p10]
for person in hijos:
  for hermano in hijos:
    if person != hermano:
      person.parentesco('hermanos',hermano)
    else:
      continue

#esposa de jaehaerys I targaryen
p10.parentesco('esposas',p11)
p1.agregar_miembro(p10)
#hijos d ejaehaerys I targaryen y alysanne targaryen velaryon

#hijos con visenya targaryen
p5 = Person('maegob I','targaryen','',19,'hombre',1)
p1.parentesco('hijos',p5)
p5.parentesco('madre',p3)
p1.agregar_miembro(p5)

print(title_header)
p1.informacion_personal()

p1.total_miembros()

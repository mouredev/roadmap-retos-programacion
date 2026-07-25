# 34 ÁRBOL GENEALÓGICO DE LA CASA DEL DRAGÓN

from abc import ABC, abstractmethod
import uuid
import json
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import requests
from PIL import Image
from io import BytesIO


class IRegistroPersonas(ABC):
    @abstractmethod
    def registrar_persona(self, nombre, genero, id_padre=None, id_madre=None, conyugue=None, hijos=None, imagen=None):
        pass

    @abstractmethod
    def buscar_persona(self, nombre):
        pass

    @abstractmethod
    def actualizar_relacion_hijo(self, hijo, padre_o_madre):
        pass

    @abstractmethod
    def validar_numero_padres(self, persona):
        pass

    @abstractmethod
    def actualizar_persona(self,  id_persona, padre=None, madre=None, conyugue=None):
        pass

    @abstractmethod
    def eliminar_persona(self, id):
        pass


class IMostrarArbol(ABC):
    @abstractmethod
    def construir_arbol(self, id_raiz):
        pass

    @abstractmethod
    def mostrar_arbol(self, arbol):
        pass


class RegistroPersonas(IRegistroPersonas):
    def __init__(self):
        self.personas = {}

    def registrar_persona(self, nombre, genero, padre=None, madre=None, conyugue=None, hijos=None, imagen_url=''):
        if nombre is None or genero is None:
            raise ValueError("Nombre y género son requeridos.")

        id_unico = str(uuid.uuid4())

        if padre == id_unico or madre == id_unico or conyugue == id_unico:
            raise ValueError(
                "Una persona no puede ser su propio padre, madre o cónyuge.")

        if conyugue:
            conyugue_persona = self.personas.get(conyugue)
            if conyugue_persona:
                if conyugue_persona.get("conyugue"):
                    raise ValueError(
                        f"{conyugue_persona['nombre']} ya está casada con otra persona.")
                conyugue_persona["conyugue"] = id_unico

        persona = {
            'id_unico': id_unico,
            'nombre': nombre.lower(),
            'genero': genero.lower(),
            'padre': padre,
            'madre': madre,
            'conyugue': conyugue,
            'hijos': [],
            'imagen': imagen_url
        }
        self.personas[id_unico] = persona
        return persona

    def buscar_persona(self, nombre):
        for clave, valor in self.personas.items():
            if valor["nombre"].lower() == nombre.lower():
                return clave, valor["nombre"], valor["id_unico"]
        return None, None

    def actualizar_relacion_hijo(self, hijo, padre_o_madre):
        if hijo not in self.personas[padre_o_madre]["hijos"]:
            self.personas[padre_o_madre]["hijos"].append(hijo)

    def validar_numero_padres(self, persona):
        padres = 0
        if persona.get("padre"):
            padres += 1
        if persona.get("madre"):
            padres += 1
        if padres > 2:
            raise ValueError("La persona tiene más de dos padres.")

    def actualizar_persona(self, id_persona, padre=None, madre=None, conyugue=None, hijo=None):
        persona = self.personas.get(id_persona)
        if not persona:
            raise ValueError("La persona con este ID no existe.")

        if padre == id_persona or madre == id_persona or conyugue == id_persona:
            raise ValueError(
                "Una persona no puede ser su propio padre, madre o cónyuge.")

        self.validar_numero_padres(persona)

        if conyugue:
            conyugue_persona = self.personas.get(conyugue)
            if conyugue_persona:
                if conyugue_persona.get("conyugue") and conyugue_persona["conyugue"] != id_persona:
                    raise ValueError(
                        f"{conyugue_persona['nombre']} ya está casada con otra persona.")
                # Actualiza el cónyuge en ambas personas
                conyugue_persona["conyugue"] = id_persona
            persona["conyugue"] = conyugue

        persona.update({'padre': padre, 'madre': madre})

        if hijo:
            self.actualizar_relacion_hijo(hijo, id_persona)
        if padre:
            self.actualizar_relacion_hijo(id_persona, padre)
        if madre:
            self.actualizar_relacion_hijo(id_persona, madre)

    def eliminar_persona(self, nombre):
        for clave, valor in list(self.personas.items()):
            if valor["nombre"].lower() == nombre.lower():
                del self.personas[clave]
                print(f"Persona con nombre {nombre} eliminada.")
                return
        print("Nombre no encontrado.")


class MostrarArbol(IMostrarArbol):
    def __init__(self, registro_personas):
        self.registro_personas = registro_personas
        self.arbol = {}

    def construir_arbol(self, id_raiz):
        def construir_diccionario(id_persona):
            persona = self.registro_personas.personas.get(id_persona)
            if not persona:
                return None

            padre = self.registro_personas.personas.get(persona.get("padre"))
            madre = self.registro_personas.personas.get(persona.get("madre"))
            conyugue = self.registro_personas.personas.get(
                persona.get("conyugue"))

            diccionario = {
                "id": id_persona,
                "nombre": persona.get("nombre"),
                "imagen": persona.get("imagen"),
                "padre": {
                    "nombre": padre.get("nombre") if padre else None,
                    "imagen": padre.get("imagen") if padre else None
                } if padre else None,
                "madre": {
                    "nombre": madre.get("nombre") if madre else None,
                    "imagen": madre.get("imagen") if madre else None
                } if madre else None,
                "conyugue": {
                    "nombre": conyugue.get("nombre") if conyugue else None,
                    "imagen": conyugue.get("imagen") if conyugue else None
                } if conyugue else None,
                "hijos": [
                    {
                        "nombre": hijo.get("nombre"),
                        "imagen": hijo.get("imagen")
                    }
                    for hijo in (self.registro_personas.personas.get(hijo_id) for hijo_id in persona.get("hijos") if hijo_id in self.registro_personas.personas)
                ]
            }
            return diccionario

        self.arbol = construir_diccionario(id_raiz)
        return self.arbol

    def mostrar_arbol(self, arbol):
        print(json.dumps(arbol, indent=4))


# Uso del código
registro = RegistroPersonas()
id_jaehaerysI = registro.registrar_persona(
    "Jaehaerys I Targaryen", "Masculino", imagen_url="https://es.digitaltrends.com/wp-content/uploads/2024/07/1-Jaehaerys-I-Targaryen.jpg?fit=720%2C480&p=1")
id_alysanne = registro.registrar_persona(
    "Alysanne Targaryen", "Femenino", imagen_url="https://static.wikia.nocookie.net/hieloyfuego/images/5/55/Alysanne.jpg/revision/latest?cb=20171022174856")
id_aemon = registro.registrar_persona(
    "Aemon Targaryen", "Masculino", padre=id_jaehaerysI["id_unico"], madre=id_alysanne['id_unico'], imagen_url="")
id_baelon = registro.registrar_persona(
    "Baelon Targaryen", "Masculino", padre=id_jaehaerysI["id_unico"], madre=id_alysanne['id_unico'], imagen_url="")
id_alysa = registro.registrar_persona(
    "Alysa Targaryen", "Femenino", padre=id_jaehaerysI["id_unico"], madre=id_alysanne['id_unico'], conyugue=id_baelon["id_unico"], imagen_url="")
id_joselyne = registro.registrar_persona(
    "Jocelyne Baratheon", "Femenino", conyugue=id_aemon["id_unico"], imagen_url="")
id_daemon = registro.registrar_persona("Daemon Targaryen", "Masculino", padre=id_baelon["id_unico"], madre=id_alysa[
                                       'id_unico'], imagen_url="https://i2-prod.mirror.co.uk/news/uk-news/article33141854.ece/ALTERNATES/s1200b/0_daemon-targaryen.jpg")
id_viserysI = registro.registrar_persona("Viserys I Targaryen", "Masculino", padre=id_baelon["id_unico"], madre=id_alysa['id_unico'],
                                         imagen_url="https://static.wikia.nocookie.net/hieloyfuego/images/f/fa/Paddy_Considine_como_Viserys_I_HBO.jpg/revision/latest?cb=20231201142723")
id_aemma = registro.registrar_persona(
    "Aemma Arryn", "Femenino", imagen_url="https://static.wikia.nocookie.net/hieloyfuego/images/1/1d/Aemma_Arryn_HBO.png/revision/latest?cb=20220818134257")
id_rhea = registro.registrar_persona(
    "Rhea Royce", "Femenino", imagen_url="https://static.wikia.nocookie.net/hieloyfuego/images/7/7e/Rhea_Royce_HBO.jpeg/revision/latest?cb=20220915180910")

registro.actualizar_persona(
    id_viserysI["id_unico"], conyugue=id_aemma["id_unico"])
registro.actualizar_persona(
    id_daemon["id_unico"], conyugue=id_rhea["id_unico"])
registro.actualizar_persona(
    id_jaehaerysI["id_unico"], conyugue=id_alysanne["id_unico"])
registro.actualizar_persona(
    id_jaehaerysI["id_unico"], hijo=id_alysa["id_unico"])
registro.actualizar_persona(
    id_jaehaerysI["id_unico"], hijo=id_aemon["id_unico"])
registro.actualizar_persona(
    id_jaehaerysI["id_unico"], hijo=id_baelon["id_unico"])
registro.actualizar_persona(
    id_alysanne["id_unico"], conyugue=id_jaehaerysI["id_unico"])
registro.actualizar_persona(id_alysanne["id_unico"], hijo=id_alysa["id_unico"])
registro.actualizar_persona(id_alysanne["id_unico"], hijo=id_aemon["id_unico"])
registro.actualizar_persona(
    id_alysanne["id_unico"], hijo=id_baelon["id_unico"])
registro.actualizar_persona(id_baelon["id_unico"], hijo=id_daemon["id_unico"])
registro.actualizar_persona(
    id_baelon["id_unico"], hijo=id_viserysI["id_unico"])
registro.actualizar_persona(
    id_baelon["id_unico"], padre=id_jaehaerysI["id_unico"], madre=id_alysanne["id_unico"])

personaje_buscado = registro.buscar_persona("Rhea Royce")
print(personaje_buscado)
registro.eliminar_persona("Rhea Royce")

# Mostrar árbol genealógico como diccionario
mostrar = MostrarArbol(registro)
arbol = mostrar.construir_arbol(id_baelon["id_unico"])
mostrar.mostrar_arbol(arbol)

# Extra: Mostrar árbol genealógico como un grafo
# Función para cargar imágenes desde un enlace


def obtener_imagen(url):
    if not url or not url.startswith(('http://', 'https://')):
        print(f"URL no válida: {url}. Se usará la imagen por defecto.")
        url = default_image_url
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return OffsetImage(img, zoom=0.03)
    except Exception as e:
        print(f"Error al cargar la imagen desde {url}: {e}")
        return OffsetImage(Image.open(BytesIO(requests.get(default_image_url).content)), zoom=0.08)


# Configuración de imágenes por defecto
default_image_url = "https://mundo-ghibli.com/wp-content/uploads/2023/10/sin-rostro-chihiro.jpg.webp"

# Crear el grafo dirigido
G = nx.DiGraph()

# Agregar nodos y aristas usando nombres como identificadores
# Verificar si el padre existe y agregar nodo y arista si es así
if arbol.get("padre") and arbol["padre"].get("nombre"):
    G.add_node(arbol["padre"]["nombre"],
               imagen=arbol["padre"].get("imagen", default_image_url))
    G.add_node(arbol["nombre"], imagen=arbol.get("imagen", default_image_url))
    G.add_edge(arbol["padre"]["nombre"], arbol["nombre"])

# Verificar si la madre existe y agregar nodo y arista
if arbol.get("madre") and arbol["madre"].get("nombre"):
    G.add_node(arbol["madre"]["nombre"],
               imagen=arbol["madre"].get("imagen", default_image_url))
    G.add_edge(arbol["madre"]["nombre"], arbol["nombre"])

# Verificar si el cónyuge existe y agregar nodo y arista
if arbol.get("conyugue") and arbol["conyugue"].get("nombre"):
    G.add_node(arbol["conyugue"]["nombre"],
               imagen=arbol["conyugue"].get("imagen", default_image_url))
    G.add_edge(arbol["nombre"], arbol["conyugue"]["nombre"])

# Verificar si hay hijos y agregar nodos y aristas
for hijo in arbol.get("hijos", []):
    if hijo.get("nombre"):  # Evitar nodos sin nombre
        # Usar imagen del hijo o predeterminada
        G.add_node(hijo["nombre"], imagen=hijo.get(
            "imagen", default_image_url))
        G.add_edge(arbol["nombre"], hijo["nombre"])

# Posiciones para una mejor visualización
pos = {
    arbol["nombre"]: (0, 0),  # El nodo principal en el centro
}

# Posición del padre si existe
if arbol.get("padre") and arbol["padre"].get("nombre"):
    # Posicionamos al padre a la izquierda arriba
    pos[arbol["padre"]["nombre"]] = (-1, 1)

# Posición de la madre si existe
if arbol.get("madre") and arbol["madre"].get("nombre"):
    # Posicionamos a la madre a la derecha arriba
    pos[arbol["madre"]["nombre"]] = (1, 1)

# Posición del cónyuge si existe
if arbol.get("conyugue") and arbol["conyugue"].get("nombre"):
    # Posicionamos al cónyuge a la derecha del nodo principal
    pos[arbol["conyugue"]["nombre"]] = (1, 0)

# Distribuir la posición de los hijos
for idx, hijo in enumerate(arbol.get("hijos", [])):
    if hijo.get("nombre"):
        # Calculamos la posición horizontal de cada hijo
        # Los hijos se posicionan debajo del nodo principal
        pos[hijo["nombre"]] = (idx - len(arbol["hijos"]) / 2, -1)

# Dibujar el grafo
fig, ax = plt.subplots()

# Verifica si el nodo existe y no es None
try:
    padre_nombre = arbol.get("padre", {}).get("nombre", None)
except AttributeError:
    padre_nombre = None
try:
    madre_nombre = arbol.get("madre", {}).get("nombre", None)
except AttributeError:
    madre_nombre = None
try:
    conyugue_nombre = arbol.get("conyugue", {}).get("nombre", None)
except AttributeError:
    conyugue_nombre = None

# Definir tamaños de los nodos
node_sizes = {
    padre_nombre: 1200 if padre_nombre else 0,
    madre_nombre: 1200 if madre_nombre else 0,
    arbol["nombre"]: 2000,
    conyugue_nombre: 2000 if conyugue_nombre else 0,
    **{hijo["nombre"]: 1000 for hijo in arbol.get("hijos", []) if hijo.get("nombre")}
}

# Definir colores de los nodos
node_colors = {
    padre_nombre: "grey" if padre_nombre else 'white',
    madre_nombre: "grey" if madre_nombre else 'white',
    arbol["nombre"]: "blue",
    conyugue_nombre: "purple" if conyugue_nombre else 'white',
    **{hijo["nombre"]: "lightblue" for hijo in arbol.get("hijos", []) if hijo.get("nombre")}
}

# Dibuja el grafo con aristas
nx.draw(
    G, pos, with_labels=False, arrows=True,
    node_size=[node_sizes.get(node, 500) for node in G.nodes()],
    node_color=[node_colors.get(node, 'white') for node in G.nodes()],
    font_size=10, font_weight='bold', ax=ax
)

# Añadir los nombres por encima de los nodos
for nodo, (x, y) in pos.items():
    ax.text(x + 0.1, y + 0.15, nodo, fontsize=10, ha='center',
            color='black')  # Ajustar posición del texto

# Añadir las imágenes a los nodos
for nodo, (x, y) in pos.items():
    if nodo in G.nodes():
        imagen_url = G.nodes[nodo].get('imagen', default_image_url)
        try:
            # Obtener la imagen del diccionario
            img = obtener_imagen(imagen_url)
            ab = AnnotationBbox(img, (x, y), frameon=False)
            ax.add_artist(ab)
        except Exception as e:
            print(f"No se pudo cargar la imagen para {nodo}: {e}")

plt.title("Árbol Genealógico de la Casa del Dragón",
          fontsize=14, fontweight='bold', y=1.05)
plt.axis('off')
plt.show()

""" 
# 50 - Planificador de ano nuevo 
"""
# Programa un gestor de objetivos con las siguientes características:
    # Permite añadir objetivos (máximo 10)
    # Calcular el plan detallado
    # Guardar la planificación
# Cada entrada de un objetivo está formado por (con un ejemplo):
    # Meta: Leer libros
    # Cantidad: 12
    # Unidades: libros
    # Plazo (en meses): 12 (máximo 12)
# El cálculo del plan detallado generará la siguiente salida:
   # Un apartado para cada mes
   # Un listado de objetivos calculados a cumplir en cada mes
   # (ejemplo: si quiero leer 12 libros, dará como resultado
   # uno al mes)
   # Cada objetivo debe poseer su nombre, la cantidad de
   # unidades a completar en cada mes y su total. Por ejemplo:
   # Enero:
   # [ ] 1. Leer libros (1 libro/mes). Total: 12.
   # [ ] 2. Estudiar Git (1 curso/mes). Total: 1.
   # Febrero:
   # [ ] 1. Leer libros (1 libro/mes). Total: 12.
   # ...
   # Diciembre:
   # [ ] 1. Leer libros (1 libro/mes). Total: 12.
   # Si la duración es menor a un año, finalizará en el mes
   # correspondiente.
# Por último, el cálculo detallado debe poder exportarse a .txt


class Objetivo:
    def __init__(self, meta, cantidad, unidades, plazo):
        self.meta = meta
        self.cantidad = cantidad
        self.unidades = unidades
        self.plazo = min(plazo, 12)  # Máximo 12 meses
        self.cantidad_mensual = self.cantidad / self.plazo

class Planificador:
    def __init__(self):
        self.objetivos = []
        self.meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                      "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    def anadir_objetivo(self, meta, cantidad, unidades, plazo):
        if len(self.objetivos) >= 10:
            print("¡Has alcanzado el máximo de 10 objetivos!")
            return False
        
        try:
            cantidad = float(cantidad)
            plazo = int(plazo)
            
            if cantidad <= 0 or plazo <= 0 or plazo > 12:
                print("La cantidad debe ser mayor que 0 y el plazo entre 1 y 12 meses.")
                return False
            
            objetivo = Objetivo(meta, cantidad, unidades, plazo)
            self.objetivos.append(objetivo)
            print(f"Objetivo '{meta}' añadido correctamente.")
            return True
        except ValueError:
            print("Error: Los valores de cantidad y plazo deben ser números.")
            return False
    
    def calcular_plan(self):
        if not self.objetivos:
            print("No hay objetivos para calcular el plan.")
            return None
        
        plan = {}
        for mes_idx, mes in enumerate(self.meses):
            plan[mes] = []
            for obj in self.objetivos:
                if mes_idx < obj.plazo:
                    plan[mes].append(obj)
        
        return plan
    
    def mostrar_plan(self):
        plan = self.calcular_plan()
        if not plan:
            return ""
        
        resultado = []
        for mes, objetivos in plan.items():
            if not objetivos:
                continue
                
            resultado.append(f"{mes}:")
            for i, obj in enumerate(objetivos, 1):
                cantidad_mensual = obj.cantidad_mensual
                # Formatear cantidad mensual sin decimales si es un número entero
                if cantidad_mensual == int(cantidad_mensual):
                    cantidad_mensual = int(cantidad_mensual)
                
                resultado.append(f"[ ] {i}. {obj.meta} ({cantidad_mensual} {obj.unidades}/mes). "
                                f"Total: {obj.cantidad}.")
        
        return "\n".join(resultado)
    
    def exportar_plan(self, nombre_archivo="plan_anual.txt"):
        plan_texto = self.mostrar_plan()
        if not plan_texto:
            print("No hay plan para exportar.")
            return False
        
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                archivo.write("PLAN DE OBJETIVOS ANUALES\n")
                archivo.write("=========================\n\n")
                archivo.write(plan_texto)
            print(f"Plan exportado correctamente a '{nombre_archivo}'.")
            return True
        except Exception as e:
            print(f"Error al exportar el plan: {str(e)}")
            return False

def menu_principal():
    planificador = Planificador()
    
    while True:
        print("\n==== PLANIFICADOR DE OBJETIVOS DE AÑO NUEVO ====")
        print("1. Añadir objetivo")
        print("2. Ver plan detallado")
        print("3. Exportar plan a archivo .txt")
        print("4. Salir")
        
        opcion = input("\nSelecciona una opción (1-4): ")
        
        if opcion == "1":
            if len(planificador.objetivos) >= 10:
                print("Ya has alcanzado el máximo de 10 objetivos.")
                continue
                
            print("\n-- NUEVO OBJETIVO --")
            meta = input("Meta: ")
            cantidad = input("Cantidad: ")
            unidades = input("Unidades: ")
            plazo = input("Plazo (en meses, máximo 12): ")
            
            planificador.anadir_objetivo(meta, cantidad, unidades, plazo)
            
        elif opcion == "2":
            print("\n-- PLAN DETALLADO --")
            plan = planificador.mostrar_plan()
            if plan:
                print(plan)
            else:
                print("No hay objetivos para mostrar.")
                
        elif opcion == "3":
            nombre_archivo = input("Nombre del archivo (o Enter para usar 'plan_anual.txt'): ")
            if not nombre_archivo:
                nombre_archivo = "plan_anual.txt"
            planificador.exportar_plan(nombre_archivo)
            
        elif opcion == "4":
            print("¡Gracias por usar el Planificador de Objetivos!")
            break
            
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

if __name__ == "__main__":
    menu_principal()
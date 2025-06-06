import pandas as pd

cvs_file = "D:\\Programacion\\registros.csv"

df = pd.read_csv(cvs_file)

print("Participantes:")
print(df)

emails_activos = df[df["status"] == "activo"][["id", "email"]]

ganadores = emails_activos.sample(3)
categorias = ["ganador de una suscripción", "ganador de un descuento", "ganador de un libro"]

print("\nGanadores:")

for index, (row, categoria) in enumerate(zip(ganadores.iterrows(), categorias)):
    _, ganador = row
    print(f"ID: {ganador['id']}, Email: {ganador['email']} -> {categoria}")

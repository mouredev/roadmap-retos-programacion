import zipfile

def compress_file(file_path, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, arcname=file_path.split("/")[-1])

file = "D:\\Programacion\\comandos importantes de git.txt"
output = "archivo.zip"

compress_file(file, output)
print(f"Archivo comprimido creado: {output}")

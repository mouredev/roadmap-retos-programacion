#41 { Retos para Programadores } CAMISETA RAR 

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""
 * EJERCICIO:
 * ¿Has visto la camiseta.rar?
 * https://x.com/MoureDev/status/1841531938961592740
 *
 * Crea un programa capaz de comprimir un archivo 
 * en formato .zip (o el que tú quieras).
 * - No subas el archivo o el zip.

"""

log = print

# zipfile module to create and manipulate ZIP files
import zipfile
import os

# Function to compress a file
def compress_file(input_file_path, output_zip_path):
    # Create a ZipFile object in write mode
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Read the file to be compressed
        zipf.write(input_file_path, os.path.basename(input_file_path))
    
    log(f'File compressed and saved as {output_zip_path}')

# Specify the input file path and output zip file name
input_file_path = 'C:/Users/Niko Zen/Documents/a Nany.docx'  # Replace with the file path to compress
output_zip_path = 'test_output.zip'  # Desired output zip file name

# Compress the file and handle any potential errors
try:
    compress_file(input_file_path, output_zip_path)
    log('Compression complete!')
except Exception as e:
    log('Error during compression:', e)

# Possible output: 
# File compressed and saved as test_output.zip
# Compression complete!

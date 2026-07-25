import java.io.*;
import java.util.Scanner;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

public class miguelex {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Selecciona lo que quieres comprimir:");
        System.out.println("1. Archivo");
        System.out.println("2. Directorio");
        int tipoSeleccionado = Integer.parseInt(scanner.nextLine());

        String tipo;
        if (tipoSeleccionado == 1) {
            tipo = "archivo";
        } else if (tipoSeleccionado == 2) {
            tipo = "directorio";
        } else {
            System.out.println("Selección no válida");
            return;
        }

        System.out.println("Introduce la ruta del " + tipo + " que deseas comprimir:");
        String inputPath = scanner.nextLine();

        System.out.println("Selecciona el formato de compresión:");
        System.out.println("1. ZIP");
        int formatoSeleccionado = Integer.parseInt(scanner.nextLine());

        if (formatoSeleccionado != 1) {
            System.out.println("Formato no válido");
            return;
        }

        System.out.println("Introduce el nombre de salida (sin la extensión):");
        String nombreSalida = scanner.nextLine() + ".zip";

        try {
            FileOutputStream fos = new FileOutputStream(nombreSalida);
            ZipOutputStream zos = new ZipOutputStream(fos);

            File inputFile = new File(inputPath);
            if (tipo.equals("archivo")) {
                agregarArchivoAlZip(inputFile, zos);
            } else {
                agregarDirectorioAlZip(inputFile, inputFile.getName(), zos);
            }

            zos.close();
            fos.close();
            System.out.println("Archivo/directorio comprimido con éxito en " + nombreSalida);
        } catch (IOException e) {
            System.out.println("Error al comprimir: " + e.getMessage());
        }
    }

    private static void agregarArchivoAlZip(File archivo, ZipOutputStream zos) throws IOException {
        FileInputStream fis = new FileInputStream(archivo);
        ZipEntry zipEntry = new ZipEntry(archivo.getName());
        zos.putNextEntry(zipEntry);

        byte[] buffer = new byte[1024];
        int length;
        while ((length = fis.read(buffer)) >= 0) {
            zos.write(buffer, 0, length);
        }

        zos.closeEntry();
        fis.close();
    }

    private static void agregarDirectorioAlZip(File carpeta, String nombreBase, ZipOutputStream zos) throws IOException {
        File[] archivos = carpeta.listFiles();
        if (archivos != null) {
            for (File archivo : archivos) {
                if (archivo.isDirectory()) {
                    agregarDirectorioAlZip(archivo, nombreBase + "/" + archivo.getName(), zos);
                } else {
                    FileInputStream fis = new FileInputStream(archivo);
                    ZipEntry zipEntry = new ZipEntry(nombreBase + "/" + archivo.getName());
                    zos.putNextEntry(zipEntry);

                    byte[] buffer = new byte[1024];
                    int length;
                    while ((length = fis.read(buffer)) >= 0) {
                        zos.write(buffer, 0, length);
                    }

                    zos.closeEntry();
                    fis.close();
                }
            }
        }
    }
}

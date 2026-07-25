import java.io.*;
import java.math.BigDecimal;
import java.nio.file.Files;
import java.nio.file.Path;
import java.text.DecimalFormat;
import java.util.zip.Deflater;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().RARShirt();
    }

    public void RARShirt(){
        Path fileToZip = Path.of("./src/Josegs95.java");
        String zipName = "Josegs95";

        zipFile(fileToZip, zipName);
    }

    private void zipFile(Path fileToZipPath, String zipFileName){
        File sourceFile = fileToZipPath.toFile();
        if (!Files.isRegularFile(sourceFile.toPath())){
            System.out.printf("Error, %s no es un archivo válido", fileToZipPath);
            return;
        }

        File zipFile = Path.of(sourceFile.getParent(), zipFileName + ".zip").toFile();
        try(ZipOutputStream zos = new ZipOutputStream(new FileOutputStream(zipFile))){
            zos.setLevel(Deflater.BEST_COMPRESSION);
            zos.putNextEntry(new ZipEntry(sourceFile.getName()));

            byte[] bytes = Files.readAllBytes(fileToZipPath);
            zos.write(bytes, 0, bytes.length);
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        Long sourceFileSize = sourceFile.length();
        Long zipFileSize = zipFile.length();
        Double ratio = ((double) zipFileSize) / sourceFileSize;

        System.out.println("Archivo comprimido con éxito");
        System.out.print(zipFile.getName() + ": " + zipFileSize + " bytes");
        System.out.println(" (ratio: " + ((int)(ratio * 100)) / 100.00 + ")");
    }
}

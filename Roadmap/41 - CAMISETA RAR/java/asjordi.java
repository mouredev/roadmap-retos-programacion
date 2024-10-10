import java.io.*;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

public class Main {

    public static void main(String[] args) throws IOException {
        var res = compressFile("persons.csv");
        System.out.println(res ? "File compressed successfully" : "Failed to compress file");
    }

    public static boolean compressFile(String sourceFile) {
        try (FileOutputStream fos = new FileOutputStream("compressed.zip");
             ZipOutputStream zipOut = new ZipOutputStream(fos) ) {

            File fileToZip = new File(sourceFile);

            try (FileInputStream fis = new FileInputStream(fileToZip)) {

                ZipEntry zipEntry = new ZipEntry(fileToZip.getName());
                zipOut.putNextEntry(zipEntry);
                byte[] bytes = new byte[2048];
                int length;

                while ((length = fis.read(bytes)) >= 0) {
                    zipOut.write(bytes, 0, length);
                }

            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
            return false;
        }

        return true;
    }

}

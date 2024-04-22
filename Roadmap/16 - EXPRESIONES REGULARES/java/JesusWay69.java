package ejercicio16;

/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */
public class JesusWay69 {

    public static void main(String[] args) {
        String text = "Un año tiene 365 días excepto si es bisiesto que tiene 366 divididos en 12 meses que pueden tener hasta 31 días cada uno.";
        char[] characters = text.toCharArray();
        String nums = "";
        for (int i = 0; i < characters.length; i++) {
            nums = Character.toString(characters[i]);
            if (nums.matches("\\d")) { //La er para cualquier número se puede declarar como "\\d" o "[0-9]"
                System.out.print(nums + "\s");
            }

        }
        System.out.println("\n" + emailValidation("jesus.way.69@hoTMail.com"));
        System.out.println(spainPhoneNumberValidation("+34716984941"));
        System.out.println(urlValidation("www.retosdeprogramacion.com"));
        System.out.println(spainDniValidation("48526522Y"));
        System.out.println(dateValidation("00-09-2050"));
    }

    private static boolean emailValidation(String email) {
        email = email.toLowerCase();
        return email.matches("[a-z0-9\\.]+(@)[a-z0-9]+\\.[a-z]{2,4}");
    }

    private static boolean spainPhoneNumberValidation(String phoneNumber) {
        return phoneNumber.matches("[9||7||6][0-9]{8}||(\\+34)[9||7||6][0-9]{8}");
    }

    private static boolean urlValidation(String url) {
        url = url.toLowerCase();
        return url.matches("[a-z0-9.]{1,63}\\.[a-z]+||(www)\\.[a-z0-9.]{1,63}\\.[a-z]+");
    }

    private static boolean spainDniValidation(String dniNum) {
        dniNum = dniNum.toUpperCase();
        return dniNum.matches("[0-9]{8}[^IOU]{1}");
    //Función que valida un dni español con 8 cifras y una letra al final que no puede ser i,o,u ni ñ 

    }
    private static boolean dateValidation(String date){
        return date.matches("^([0-2][0-9]||[3][0-1])(\\/|-)(0[1-9]||1[0-2])(\\/|-)((19)[5-9][0-9]||(20)[0-4][0-9]||(2050))$");
    //Función que valida una fecha en formato dd/mm/aaaa con límites de días a 31,meses a 12 y años entre 1950 y 2050
    }
}

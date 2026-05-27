public class AnaLauDB {

    // ==========================================================================
    // IMPLEMENTACIÓN QUE CUMPLE EL PRINCIPIO DE SEGREGACIÓN DE INTERFACES (ISP)
    // ==========================================================================

    // 1. INTERFACES ESPECÍFICAS (SEGREGADAS)
    // ==========================================================================

    // Interfaz para funcionalidad de impresión básica
    interface Imprimible {
        void imprimir(String documento);
    }

    // Interfaz para funcionalidad de impresión en color
    interface ImprimibleColor {
        void imprimirColor(String documento);
    }

    // Interfaz para funcionalidad de escaneado
    interface Escaneable {
        String escanear();
    }

    // Interfaz para funcionalidad de fax
    interface EnviadorFax {
        void enviarFax(String numero, String documento);
    }

    // ==========================================================================
    // 2. IMPLEMENTACIONES DE DIFERENTES TIPOS DE IMPRESORAS
    // ==========================================================================

    // Impresora que solo imprime en blanco y negro
    static class ImpresoraBlancoNegro implements Imprimible {
        private String modelo;

        public ImpresoraBlancoNegro(String modelo) {
            this.modelo = modelo;
        }

        @Override
        public void imprimir(String documento) {
            System.out.println("[" + modelo + "] Imprimiendo en blanco y negro: " + documento);
            // Simular tiempo de impresión
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            System.out.println("[" + modelo + "] Documento impreso en B&N.");
        }

        public String getModelo() {
            return modelo;
        }
    }

    // Impresora que solo imprime a color
    static class ImpresoraColor implements ImprimibleColor {
        private String modelo;

        public ImpresoraColor(String modelo) {
            this.modelo = modelo;
        }

        @Override
        public void imprimirColor(String documento) {
            System.out.println("[" + modelo + "] Imprimiendo a todo color: " + documento);
            // Simular tiempo de impresión (más lento por el color)
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            System.out.println("[" + modelo + "] Documento impreso a color.");
        }

        public String getModelo() {
            return modelo;
        }
    }

    // Impresora multifunción completa
    static class ImpresoraMultifuncion implements Imprimible, ImprimibleColor, Escaneable, EnviadorFax {
        private String modelo;

        public ImpresoraMultifuncion(String modelo) {
            this.modelo = modelo;
        }

        @Override
        public void imprimir(String documento) {
            System.out.println("[" + modelo + "] Imprimiendo en blanco y negro: " + documento);
            try {
                Thread.sleep(400);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            System.out.println("[" + modelo + "] Documento impreso en B&N.");
        }

        @Override
        public void imprimirColor(String documento) {
            System.out.println("[" + modelo + "] Imprimiendo a todo color: " + documento);
            try {
                Thread.sleep(800);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            System.out.println("[" + modelo + "] Documento impreso a color.");
        }

        @Override
        public String escanear() {
            System.out.println("[" + modelo + "] Escaneando documento...");
            try {
                Thread.sleep(600);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            String documentoEscaneado = "documento_escaneado_" + System.currentTimeMillis() + ".pdf";
            System.out.println("[" + modelo + "] Documento escaneado: " + documentoEscaneado);
            return documentoEscaneado;
        }

        @Override
        public void enviarFax(String numero, String documento) {
            System.out.println("[" + modelo + "] Enviando fax a " + numero + ": " + documento);
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            System.out.println("[" + modelo + "] Fax enviado exitosamente a " + numero);
        }

        public String getModelo() {
            return modelo;
        }
    }

    // Impresora básica con escáner (sin fax ni color)
    static class ImpresoraConEscaner implements Imprimible, Escaneable {
        private String modelo;

        public ImpresoraConEscaner(String modelo) {
            this.modelo = modelo;
        }

        @Override
        public void imprimir(String documento) {
            System.out.println("[" + modelo + "] Imprimiendo en blanco y negro: " + documento);
            try {
                Thread.sleep(450);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            System.out.println("[" + modelo + "] Documento impreso en B&N.");
        }

        @Override
        public String escanear() {
            System.out.println("[" + modelo + "] Escaneando documento...");
            try {
                Thread.sleep(550);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            String documentoEscaneado = "scan_" + System.currentTimeMillis() + ".pdf";
            System.out.println("[" + modelo + "] Documento escaneado: " + documentoEscaneado);
            return documentoEscaneado;
        }

        public String getModelo() {
            return modelo;
        }
    }

    // ==========================================================================
    // 3. GESTOR DE IMPRESORAS
    // ==========================================================================

    static class GestorImpresoras {

        // Método para manejar impresión básica
        public static void realizarImpresion(Imprimible impresora, String documento) {
            System.out.println("\nIniciando impresión básica...");
            impresora.imprimir(documento);
        }

        // Método para manejar impresión a color
        public static void realizarImpresionColor(ImprimibleColor impresora, String documento) {
            System.out.println("\nIniciando impresión a color...");
            impresora.imprimirColor(documento);
        }

        // Método para manejar escaneado
        public static String realizarEscaneo(Escaneable escaner) {
            System.out.println("\nIniciando escaneado...");
            return escaner.escanear();
        }

        // Método para enviar fax
        public static void enviarFax(EnviadorFax fax, String numero, String documento) {
            System.out.println("\nIniciando envío de fax...");
            fax.enviarFax(numero, documento);
        }

        // Método que demuestra el polimorfismo respetando ISP
        public static void procesamientoAvanzado(Object impresora, String documento) {
            System.out.println("\nProcesamiento automático según capacidades...");

            // Solo usar las interfaces que la impresora implementa
            if (impresora instanceof Imprimible) {
                ((Imprimible) impresora).imprimir(documento);
            }

            if (impresora instanceof ImprimibleColor) {
                ((ImprimibleColor) impresora).imprimirColor(documento + "_color");
            }

            if (impresora instanceof Escaneable) {
                String archivoEscaneado = ((Escaneable) impresora).escanear();
                System.out.println("Archivo generado: " + archivoEscaneado);
            }

            if (impresora instanceof EnviadorFax) {
                ((EnviadorFax) impresora).enviarFax("555-1234", documento);
            }
        }
    }

    // ==========================================================================
    // 4. CÓDIGO DE VERIFICACIÓN DEL ISP
    // ==========================================================================

    public static void main(String[] args) {
        System.out.println("=== DEMOSTRACIÓN DEL PRINCIPIO DE SEGREGACIÓN DE INTERFACES (ISP) ===");

        // Crear diferentes tipos de impresoras
        ImpresoraBlancoNegro impresoraBN = new ImpresoraBlancoNegro("HP LaserJet Pro");
        ImpresoraColor impresoraColor = new ImpresoraColor("Canon PIXMA");
        ImpresoraMultifuncion multifuncion = new ImpresoraMultifuncion("Epson WorkForce Pro");
        ImpresoraConEscaner impresoraEscaner = new ImpresoraConEscaner("Brother DCP-L2550");

        System.out.println("\n1. VERIFICANDO CUMPLIMIENTO DEL ISP:");
        System.out.println("ImpresoraBlancoNegro solo implementa Imprimible");
        System.out.println("ImpresoraColor solo implementa ImprimibleColor");
        System.out.println("ImpresoraMultifuncion implementa todas las interfaces necesarias");
        System.out.println("ImpresoraConEscaner implementa Imprimible y Escaneable");
        System.out.println("Ninguna clase implementa métodos que no necesita");

        // 2. Probar funcionalidades específicas
        System.out.println("\n2. PROBANDO FUNCIONALIDADES ESPECÍFICAS:");

        // Impresora B&N - solo puede imprimir
        GestorImpresoras.realizarImpresion(impresoraBN, "Informe_Anual.pdf");

        // Impresora Color - solo puede imprimir a color
        GestorImpresoras.realizarImpresionColor(impresoraColor, "Presentacion_Marketing.pdf");

        // Multifunción - puede hacer todo
        GestorImpresoras.realizarImpresion(multifuncion, "Documento_Oficial.pdf");
        GestorImpresoras.realizarImpresionColor(multifuncion, "Folleto_Promocional.pdf");
        String archivoEscaneado = GestorImpresoras.realizarEscaneo(multifuncion);
        GestorImpresoras.enviarFax(multifuncion, "555-9876", "Contrato.pdf");

        // Impresora con escáner - puede imprimir y escanear
        GestorImpresoras.realizarImpresion(impresoraEscaner, "Manual_Usuario.pdf");
        GestorImpresoras.realizarEscaneo(impresoraEscaner);

        // 3. Demostrar procesamiento polimórfico respetando ISP
        System.out.println("\n3. PROCESAMIENTO POLIMÓRFICO CON ISP:");

        Object[] impresoras = { impresoraBN, impresoraColor, multifuncion, impresoraEscaner };

        for (Object imp : impresoras) {
            System.out.println("\n--- Procesando: " + imp.getClass().getSimpleName() + " ---");
            GestorImpresoras.procesamientoAvanzado(imp, "TestDocument");
        }

        // 4. Verificar que ISP previene violaciones
        System.out.println("\n4. VERIFICACIÓN FINAL DEL ISP:");

        // Intentar usar solo las capacidades que cada impresora tiene
        System.out.println("\nVerificando que cada impresora solo expone métodos relevantes:");

        // Esta impresora NO puede hacer color, escanear o enviar fax
        if (!(impresoraBN instanceof ImprimibleColor)) {
            System.out.println("ImpresoraBN correctamente NO implementa ImprimibleColor");
        }

        if (!(impresoraBN instanceof Escaneable)) {
            System.out.println("ImpresoraBN correctamente NO implementa Escaneable");
        }

        if (!(impresoraBN instanceof EnviadorFax)) {
            System.out.println("ImpresoraBN correctamente NO implementa EnviadorFax");
        }

        // Esta impresora NO puede hacer B&N, escanear o enviar fax
        if (!(impresoraColor instanceof Imprimible)) {
            System.out.println("ImpresoraColor correctamente NO implementa Imprimible básico");
        }

        // Verificar que multifunción SÍ tiene todas las capacidades
        if (multifuncion instanceof Imprimible &&
                multifuncion instanceof ImprimibleColor &&
                multifuncion instanceof Escaneable &&
                multifuncion instanceof EnviadorFax) {
            System.out.println("Multifunción correctamente implementa todas las interfaces");
        }

        System.out.println("\nCONCLUSIÓN ISP:");
        System.out.println("- Cada interfaz es pequeña y específica");
        System.out.println("- Las clases solo implementan las interfaces que necesitan");
        System.out.println("- No hay métodos forzados o innecesarios");
        System.out.println("- El sistema es flexible y extensible");
        System.out.println("- Los clientes no dependen de funcionalidades que no usan");
    }
}

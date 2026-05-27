public class AnaLauDB {

    // ==========================================================================
    // IMPLEMENTACIÓN QUE CUMPLE EL PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS (DIP)
    // ==========================================================================

    // 1. ABSTRACCIÓN DE ALTO NIVEL (INTERFAZ)
    // ==========================================================================

    // Interfaz que define el contrato para cualquier servicio de notificación
    interface ServicioNotificacion {
        boolean enviarNotificacion(String destinatario, String mensaje);

        String getTipoNotificacion();

        boolean validarDestinatario(String destinatario);
    }

    // ==========================================================================
    // 2. IMPLEMENTACIONES ESPECÍFICAS (MÓDULOS DE BAJO NIVEL)
    // ==========================================================================

    // Implementación específica para Email
    static class ServicioEmail implements ServicioNotificacion {
        private String servidorSMTP;

        public ServicioEmail(String servidorSMTP) {
            this.servidorSMTP = servidorSMTP;
        }

        @Override
        public boolean enviarNotificacion(String destinatario, String mensaje) {
            if (!validarDestinatario(destinatario)) {
                System.out.println("Error: Email inválido - " + destinatario);
                return false;
            }

            System.out.println("ENVIANDO EMAIL...");
            System.out.println("Servidor SMTP: " + servidorSMTP);
            System.out.println("Para: " + destinatario);
            System.out.println("Mensaje: " + mensaje);

            // Simular envío
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }

            System.out.println("Email enviado exitosamente");
            return true;
        }

        @Override
        public String getTipoNotificacion() {
            return "EMAIL";
        }

        @Override
        public boolean validarDestinatario(String destinatario) {
            return destinatario != null && destinatario.contains("@") && destinatario.contains(".");
        }
    }

    // Implementación específica para notificaciones PUSH
    static class ServicioPush implements ServicioNotificacion {
        private String appId;

        public ServicioPush(String appId) {
            this.appId = appId;
        }

        @Override
        public boolean enviarNotificacion(String destinatario, String mensaje) {
            if (!validarDestinatario(destinatario)) {
                System.out.println("Error: Token de dispositivo inválido");
                return false;
            }

            System.out.println("ENVIANDO NOTIFICACIÓN PUSH...");
            System.out.println("App ID: " + appId);
            System.out.println("Token del dispositivo: " + destinatario);
            System.out.println("Mensaje: " + mensaje);

            // Simular envío
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }

            System.out.println("Notificación PUSH enviada exitosamente");
            return true;
        }

        @Override
        public String getTipoNotificacion() {
            return "PUSH";
        }

        @Override
        public boolean validarDestinatario(String destinatario) {
            return destinatario != null && destinatario.length() >= 10;
        }
    }

    // Implementación específica para SMS
    static class ServicioSMS implements ServicioNotificacion {
        private String proveedorSMS;
        private String apiKey;

        public ServicioSMS(String proveedorSMS, String apiKey) {
            this.proveedorSMS = proveedorSMS;
            this.apiKey = apiKey;
        }

        @Override
        public boolean enviarNotificacion(String destinatario, String mensaje) {
            if (!validarDestinatario(destinatario)) {
                System.out.println("Error: Número de teléfono inválido - " + destinatario);
                return false;
            }

            System.out.println("ENVIANDO SMS...");
            System.out.println("Proveedor: " + proveedorSMS);
            System.out.println("A: " + destinatario);
            System.out.println("Mensaje: " + mensaje);

            // Simular envío
            try {
                Thread.sleep(800);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }

            System.out.println("SMS enviado exitosamente");
            return true;
        }

        @Override
        public String getTipoNotificacion() {
            return "SMS";
        }

        @Override
        public boolean validarDestinatario(String destinatario) {
            return destinatario != null && destinatario.matches("\\+?[0-9]{10,15}");
        }
    }

    // ==========================================================================
    // 3. SISTEMA DE NOTIFICACIONES (MÓDULO DE ALTO NIVEL)
    // ==========================================================================

    // El sistema depende de la abstracción, NO de implementaciones concretas
    static class SistemaNotificaciones {
        private ServicioNotificacion servicioNotificacion;

        // Inyección de dependencia a través del constructor
        public SistemaNotificaciones(ServicioNotificacion servicioNotificacion) {
            this.servicioNotificacion = servicioNotificacion;
        }

        // Método para cambiar el servicio en tiempo de ejecución
        public void setServicioNotificacion(ServicioNotificacion servicioNotificacion) {
            this.servicioNotificacion = servicioNotificacion;
        }

        // Método principal para enviar notificaciones
        public boolean enviarNotificacion(String destinatario, String mensaje) {
            System.out.println("\n=== SISTEMA DE NOTIFICACIONES ===");
            System.out.println("Tipo de servicio: " + servicioNotificacion.getTipoNotificacion());

            return servicioNotificacion.enviarNotificacion(destinatario, mensaje);
        }

        // Método para enviar notificaciones múltiples
        public void enviarNotificacionMultiple(String[] destinatarios, String mensaje) {
            System.out.println("\n=== ENVÍO MÚLTIPLE ===");
            System.out.println("Servicio: " + servicioNotificacion.getTipoNotificacion());

            int exitosos = 0;
            for (String destinatario : destinatarios) {
                if (servicioNotificacion.enviarNotificacion(destinatario, mensaje)) {
                    exitosos++;
                }
            }

            System.out.println("Resumen: " + exitosos + "/" + destinatarios.length +
                    " notificaciones enviadas exitosamente");
        }

        // Método para obtener información del servicio actual
        public String getInformacionServicio() {
            return "Servicio actual: " + servicioNotificacion.getTipoNotificacion();
        }
    }

    // ==========================================================================
    // 4. FACTORY PARA CREAR SERVICIOS (OPCIONAL)
    // ==========================================================================

    static class FactoryNotificaciones {

        public static ServicioNotificacion crearServicioEmail(String servidor) {
            return new ServicioEmail(servidor);
        }

        public static ServicioNotificacion crearServicioPush(String appId) {
            return new ServicioPush(appId);
        }

        public static ServicioNotificacion crearServicioSMS(String proveedor, String apiKey) {
            return new ServicioSMS(proveedor, apiKey);
        }
    }

    // ==========================================================================
    // 5. CÓDIGO DE VERIFICACIÓN DEL DIP
    // ==========================================================================

    public static void main(String[] args) {
        System.out.println("=== DEMOSTRACIÓN DEL PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS (DIP) ===");

        // 1. Crear servicios específicos
        ServicioNotificacion servicioEmail = new ServicioEmail("smtp.gmail.com");
        ServicioNotificacion servicioPush = new ServicioPush("com.miapp.notificaciones");
        ServicioNotificacion servicioSMS = new ServicioSMS("Twilio", "sk_test_123456");

        // 2. Crear sistema de notificaciones con inyección de dependencia
        SistemaNotificaciones sistema = new SistemaNotificaciones(servicioEmail);

        System.out.println("\n1. VERIFICANDO CUMPLIMIENTO DEL DIP:");
        System.out.println("- El SistemaNotificaciones depende de la interfaz ServicioNotificacion");
        System.out.println("- NO depende de implementaciones concretas");
        System.out.println("- Las implementaciones dependen de la abstracción");
        System.out.println("- Se puede cambiar el comportamiento sin modificar el sistema");

        // 3. Probar con diferentes implementaciones
        System.out.println("\n2. PROBANDO CON SERVICIO EMAIL:");
        sistema.enviarNotificacion("usuario@ejemplo.com", "Bienvenido a nuestro sistema");

        System.out.println("\n3. CAMBIANDO A SERVICIO PUSH (sin modificar el sistema):");
        sistema.setServicioNotificacion(servicioPush);
        sistema.enviarNotificacion("token_dispositivo_123456789", "Nueva actualización disponible");

        System.out.println("\n4. CAMBIANDO A SERVICIO SMS:");
        sistema.setServicioNotificacion(servicioSMS);
        sistema.enviarNotificacion("+1234567890", "Código de verificación: 123456");

        // 4. Demonstrar envío múltiple con diferentes servicios
        String[] emailsDestino = { "ana@ejemplo.com", "carlos@ejemplo.com", "email_invalido" };
        String[] telefonos = { "+1234567890", "+0987654321", "telefono_invalido" };
        String[] tokens = { "token_123", "token_456", "tk_789" };

        System.out.println("\n5. ENVÍO MÚLTIPLE CON EMAIL:");
        sistema.setServicioNotificacion(servicioEmail);
        sistema.enviarNotificacionMultiple(emailsDestino, "Notificación masiva por email");

        System.out.println("\n6. ENVÍO MÚLTIPLE CON SMS:");
        sistema.setServicioNotificacion(servicioSMS);
        sistema.enviarNotificacionMultiple(telefonos, "Notificación masiva por SMS");

        System.out.println("\n7. ENVÍO MÚLTIPLE CON PUSH:");
        sistema.setServicioNotificacion(servicioPush);
        sistema.enviarNotificacionMultiple(tokens, "Notificación masiva PUSH");

        // 5. Demostrar uso del Factory
        System.out.println("\n8. USANDO FACTORY PARA CREAR SERVICIOS:");
        ServicioNotificacion emailFactory = FactoryNotificaciones.crearServicioEmail("smtp.outlook.com");
        sistema.setServicioNotificacion(emailFactory);
        sistema.enviarNotificacion("test@outlook.com", "Mensaje desde factory");

        // 6. Verificar manejo de errores
        System.out.println("\n9. PROBANDO MANEJO DE ERRORES:");
        sistema.setServicioNotificacion(servicioEmail);
        sistema.enviarNotificacion("email_sin_arroba", "Este email debería fallar");

        sistema.setServicioNotificacion(servicioSMS);
        sistema.enviarNotificacion("123", "Este SMS debería fallar");

        System.out.println("\n=== VERIFICACIÓN FINAL DEL DIP ===");
        System.out.println("CUMPLIMIENTO EXITOSO:");
        System.out.println("- Módulos de alto nivel no dependen de módulos de bajo nivel");
        System.out.println("- Ambos dependen de abstracciones");
        System.out.println("- Las abstracciones no dependen de detalles");
        System.out.println("- Los detalles dependen de abstracciones");
        System.out.println("- El sistema es extensible sin modificar código existente");
        System.out.println("- Se puede inyectar cualquier implementación de ServicioNotificacion");

        // Ejemplo de extensibilidad - agregar nuevo servicio sin modificar código
        // existente
        System.out.println("\n10. DEMOSTRANDO EXTENSIBILIDAD:");
        ServicioNotificacion nuevoServicio = new ServicioNotificacion() {
            @Override
            public boolean enviarNotificacion(String destinatario, String mensaje) {
                System.out.println("SLACK: Enviando a canal " + destinatario + ": " + mensaje);
                return true;
            }

            @Override
            public String getTipoNotificacion() {
                return "SLACK";
            }

            @Override
            public boolean validarDestinatario(String destinatario) {
                return destinatario != null && destinatario.startsWith("#");
            }
        };

        sistema.setServicioNotificacion(nuevoServicio);
        sistema.enviarNotificacion("#general", "Nuevo servicio agregado sin modificar código existente");

        System.out.println("\nSISTEMA COMPLETAMENTE COMPATIBLE CON DIP");
    }
}

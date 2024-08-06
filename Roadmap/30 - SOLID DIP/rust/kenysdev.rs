/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------------------
* SOLID: PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS (DIP)
-----------------------------------------------------
- Los módulos de alto nivel no deben depender de módulos de bajo nivel, sino de abstracciones. A su vez, las 
  abstracciones no deben depender de detalles concretos; los detalles deben depender de las abstracciones.

______________________________________
* EJERCICIO #1:
* Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
* Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
* de forma correcta e incorrecta.
*/

// ___________________________________
// De manera INCORRECTA:

// Estructura de 'bajo nivel'
struct FileStorage_;
impl FileStorage_ {
    fn save(&self, data: &str) {
        println!("Datos guardados en archivo: {}", data)
    }
}

// Estructura de 'bajo nivel'
struct DatabaseStorage_;
impl DatabaseStorage_ {
    fn save(&self, data: &str) {
        println!("Guardado en base de datos: {}", data)
    }
}

// Estructura de 'alto nivel'
struct DataManager_ {
    file_storage: FileStorage_,
    database_storage: DatabaseStorage_,
}

impl DataManager_ {

    //# Dependencia directa de Estructuras concretas('de bajo nivel')
    fn new() -> Self {
        DataManager_ {
            file_storage: FileStorage_,
            database_storage: DatabaseStorage_,
        }
    }

    fn file_storage(&self, data: &str) {
        self.file_storage.save(data);
    }

    fn database_storage(&self, data: &str) {
        self.database_storage.save(data);
    }
}

// ___________________________________
// De manera CORRECTA:

// 'Interfaz'
trait IStorage {
    fn save(&self, data: &str);
}

// Estructura concreta
struct FileStorage;
impl IStorage for FileStorage {
    fn save(&self, data: &str) {
        println!("Datos guardados en archivo: {}", data)
    }
}

// Estructura concreta
struct DatabaseStorage;
impl IStorage for DatabaseStorage {
    fn save(&self, data: &str) {
        println!("Guardado en base de datos: {}", data)
    }
}

// Estructura de 'alto nivel'
struct DataManager<T: IStorage> {
  storage: T,
}
impl <T: IStorage> DataManager<T> {

  //# Depende de las instancias que recibe, las cuales implementan la interfaz.
  fn new(storage: T) -> Self {
      DataManager { storage }
  }

  fn store_data(&self, data: &str) {
      self.storage.save(data);
  }
}

/*
//____________________________________
* EJERCICIO #2:
* Crea un sistema de notificaciones.
* Requisitos:
* 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
* 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
* Instrucciones:
* 1. Crea la interfaz o clase abstracta.
* 2. Desarrolla las implementaciones específicas.
* 3. Crea el sistema de notificaciones usando el DIP.
* 4. Desarrolla un código que compruebe que se cumple el principio.
*/

trait INotificationService {
  fn send(&self, to: &str, msg: &str);
}

// Implementación
struct EmailService;

impl INotificationService for EmailService {
  fn send(&self, to: &str, msg: &str) {
      println!("Correo enviado a: {}", to);
      println!("Mensaje: {}", msg);
  }
}

// Implementación
struct PushService;

impl INotificationService for PushService {
  fn send(&self, to: &str, msg: &str) {
      println!("Notificación PUSH enviada a: {}", to);
      println!("Mensaje: {}", msg);
  }
}

// Implementación
struct SmsService;

impl INotificationService for SmsService {
  fn send(&self, to: &str, msg: &str) {
      println!("Mensaje SMS enviado a: {}", to);
      println!("Mensaje: {}", msg);
  }
}

// Estructura 'de alto nivel'
struct NotificationSystem<T: INotificationService> {
  service: T,
}

impl<T: INotificationService> NotificationSystem<T> {
  fn new(service: T) -> Self {
      NotificationSystem { service }
  }

  fn notify(&self, to: &str, msg: &str) {
      self.service.send(to, msg);
  }
}

//____________________________________
fn main() {
    //________________________________
    // exs 1
    println!("Exs #1");

    // Usando ejemplo incorrecto:
    println!("Uso incorrecto:");

    let data_manager_ = DataManager_::new();
    data_manager_.file_storage("datos x");
    data_manager_.database_storage("datos x");

    // Usando ejemplo correcto:
    println!("Uso correcto:");

    // Instancias:
    let file_storage = FileStorage;
    let database_storage = DatabaseStorage;

    // Inyección
    let data_manager_file = DataManager::new(file_storage);
    let data_manager_database = DataManager::new(database_storage);
    
    // Uso del metodo implementado
    data_manager_file.store_data("datos x");
    data_manager_database.store_data("datos x");

    //________________________________
    // exs 2
    println!("\nExs #2");

    let email_service = EmailService;
    let push_service = PushService;
    let sms_service = SmsService;

    let email_system = NotificationSystem::new(email_service);
    email_system.notify("email@example.com", "Correo!");

    let push_system = NotificationSystem::new(push_service);
    push_system.notify("usuario123", "Notificación PUSH");

    let sms_system = NotificationSystem::new(sms_service);
    sms_system.notify("555-1234", "Mensaje SMS")
    
}

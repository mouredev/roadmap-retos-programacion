// Definición de la clase Telefono
class Telefono {
private:
  String nombre;
  String camara;
  String almacenamiento;
  String ram;

public:
  // Constructor para la clase Iphone
  Telefono(String nombre, String camara, String almacenamiento, String ram) {
    this->nombre = nombre;
    this->camara = camara;
    this->almacenamiento = almacenamiento;
    this->ram = ram;
  }

  // Método de presentación
  String presentacion() {
    return String("\nNombre: ") + nombre +
           String("\nCamara: ") + camara +
           String("\nAlmacenamiento: ") + almacenamiento +
           String("\nRam: ") + ram + "\n";
  }
};

// Instanciar un objeto de la clase Iphone
Telefono iphone15("iPhone15", "12MP", "256GB", "8GB");
Telefono sansungS23("Sansung S23", "200MP", "256GB", "8GB");
Telefono sansungS21("Sansung S21", "40MP", "256GB", "12GB");

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Presentar la información del iPhone15
  Serial.println(iphone15.presentacion());
  delay(2000);

  // Presentar la información del Sansung_S23
  Serial.println(sansungS21.presentacion());
  delay(2000);

  // Presentar la información del Sansung_S23
  Serial.println(sansungS23.presentacion());
  delay(2000);

  // Terminar el loop para evitar la repetición continua
  while (true) {}
}

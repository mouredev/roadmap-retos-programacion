import gleam/io

// Los comentario en Gleam son lineas simples precedidas por //
// Sitio oficial: https://gleam.run/
// Documentación: https://gleam.run/documentation/

const lenguaje = "Gleam"

pub fn main() {
  // Declaración de variables con let
  let saludo = "¡Hola, "
  // Si una variable es asignada pero nunca se usa Gleam emitira un warning
  let _seignora = ""
  // Con el prefijo _ se ignora el warning

  let _int = 1
  let _float = 1.0
  let _formato = 1_000_000
  let _binario = 0b1010
  let _octal = 0o10
  let _hexadecimal = 0x1a0
  let _string = "\"Hola Mundo\""
  let _unicode = "\u{1F600}"
  let _bool = True || False

  io.println(saludo <> lenguaje <> "!")
}

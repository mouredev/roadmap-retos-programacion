class Animal {
  constructor(color, nombre) {
    this.color = color;
    this.nombre = nombre;
  }
  get color() {
    return this._color;
  }
  set color(color) {
    return this._color = color;
  }
  get nombre() {
    return this.nombre;
  }
  set nombre(nombre) {
    return this.nombre = nombre;
  }
}
class Perro extends Animal {
  constructor() {
    super(color, nombre)
  }
}
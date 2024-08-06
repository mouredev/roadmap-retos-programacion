/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
 */

// Forma incorrecta de aplicar el principio ISP

class Vehicle {
    startEngine() {
        throw new Error("Method 'startEngine()' must be implemented.");
    }  
    stopEngine() {
        throw new Error("Method 'stopEngine()' must be implemented.");
    }  
    fly() {
        throw new Error("Method 'fly()' must be implemented.");
    }  
    drive() {
        throw new Error("Method 'drive()' must be implemented.");
    }  
    sail() {
        throw new Error("Method 'sail()' must be implemented.");
    }
}

class Car extends Vehicle{
    startEngine() {
        console.log('Car engine started');
    }
    
    stopEngine() {
        console.log('Car engine stopped');
    }
    
    fly() {
        throw new Error('Cars cannot fly');
    }
    
    drive() {
        console.log('Car is driving');
    }
    
    sail() {
        throw new Error('Cars cannot sail');
    }
}

const car1 = new Car();
car1.startEngine();
car1.fly();

// Forma correcta de aplicar el principio ISP

class EnginePowered{
    startEngine(){
        throw new Error("Method 'startEngine()' must be implemented.");
    }
    stopEngine(){
        throw new Error("Method 'stopEngine()' must be implemented.");
    }
}
class Drivable{
    drive(){
        throw new Error("Method 'drive()' must be implemented.");
    }
}
class Flyable{
    fly(){
        throw new Error("Method 'fly()' must be implemented.");
    }
}
class Sailable{
    sail(){
        throw new Error("Method 'sail()' must be implemented.");
    }
}


class CarEngine extends EnginePowered{
    startEngine() {
        console.log('Car engine started');
    }    
    stopEngine() {
        console.log('Car engine stopped');
    }
}

class CarDrive extends Drivable{
    drive(){
        console.log('Car is driving');
    }
}

class Car{
    constructor(){
        this.engine = new CarEngine();
        this.driving = new CarDrive();
    }
    startEngine(){
        this.engine.startEngine();
    }
    stopEngine(){
        this.engine.stopEngine();
    }
    drive(){
        this.driving.drive();
    }
}

class PlaneEngine extends EnginePowered{
    startEngine(){
        console.log('Plane engine started');
    }
    stopEngine(){
        console.log('Plane engine stopped');
    }
}

class PlaneFly extends Flyable{
    fly(){
        console.log("Plane is flying")
    }
}

class Plane{
    constructor(){
        this.engine = new PlaneEngine();
        this.flying = new PlaneFly();
    }
    startEngine(){
        this.engine.startEngine();
    }
    stopEngine(){
        this.engine.stopEngine();
    }
    fly(){
        this.flying.fly();
    }
}


const car = new Car();

car.startEngine();
car.drive();
car.stopEngine();

const plane = new Plane();

plane.startEngine();
plane.fly();
plane.stopEngine();


//////////////// --------------------------------------- EXTRA ------------------------------- //////////////////////


class BlackWhitePrint{
    printBlWh(){
        throw new Error("Method 'printBlWh()' must be implemented.");
    }
}
class ColorPrint{
    printColor(){
        throw new Error("Method 'printColor()' must be implemented.");
    }
}
class ScannerPrint{
    scan(){
        throw new Error("Method 'scan()' must be implemented.");
    }
}
class FaxPrint{
    sendFax(dest){
        throw new Error("Method 'sendFax()' must be implemented.");
    }
}

// Implementaciones para una impresoar Epson
class EpsonBlackWhite extends BlackWhitePrint{
    printBlWh(){
        console.log("Impresion en blanco y negro")
    }
}
class EpsonColor extends ColorPrint{
    printColor(){
        console.log("Impresion a colores")
    }
}
class EpsonScanner extends ScannerPrint{
    scan(){
        console.log("Escaneo disponible")
    }
}

class Epson{
    constructor(){
        this.blackWhite = new EpsonBlackWhite();
        this.colores = new EpsonColor();
        this.escaner = new EpsonScanner();
    }
    printBlWh(){
        this.blackWhite.printBlWh();
    }
    printColor(){
        this.colores.printColor();
    }
    scan(){
        this.escaner.scan();
    }
}

// Implementaciones para una impresora Cannon
class CannonBlackWhite extends BlackWhitePrint{
    printBlWh(){
        console.log("Impresion en blanco y negro")
    }
}
class CannonFax extends FaxPrint{
    sendFax(dest){
        console.log(`Enviando documento a ${dest}`)
    }
}

class Cannon{
    constructor(){
        this.blackWhite = new CannonBlackWhite();
        this.sendTo = new CannonFax();
    }
    printBlWh(){
        this.blackWhite.printBlWh();
    }
    sendFax(dest){
        this.sendTo.sendFax(dest);
    }
}

const epson = new Epson();
epson.printBlWh();
epson.printColor(),
epson.scan();

const cannon = new Cannon();
cannon.printBlWh();
cannon.sendFax("juan4512");

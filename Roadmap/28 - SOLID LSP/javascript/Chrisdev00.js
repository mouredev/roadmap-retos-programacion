/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
 */

// Forma incorrecta sin aplicar el principio LSP

class Content{
    render(){
        throw new Error("Method 'render' must be implemented.");
    }

    getSummary(){
        throw new Error("Method 'summary' must be implemented.");
    }
}

class Article extends Content{
    constructor(title, body){
        super();
        this.title = title;
        this.body = body
    }
    render(){
        return `${this.title}<p>${this.body}</p> `;
    }
    getSummary(){
        return this.body.substring(0, 100) + "...";
    }
}

class Video extends Content{
    constructor(title,videoUrl){
        super();
        this.title = title;
        this.videoUrl = videoUrl
    }
    render(){
        return `${this.title}<video src='${this.videoUrl}' controls></video>`;
    }
    getSummary(){
        return `${this.title} (Video)`;
    }
}

class ImageGallery extends Content{
    constructor(title, images){
        super();
        this.title = this.title;
        this.images = images;
    }
    render(){
        const imageTags = this.images.map(image => `<img src='${image}' />`).join('');
        return `${this.title}${imageTags}`;
    }
    getSummary(){
        return `${this.title} (${this.images.length} images)`;
    }
}

function displayContent(content){
    if(content instanceof Article){
        console.log("Rendering Article:");
        console.log(content.render());
        console.log("Summary:");
        console.log(content.getSummary());
    } else if(content instanceof Video){
        console.log("Rendering Video:");
        console.log(content.render());
        console.log("Summary:");
        console.log(content.getSummary());
    } else if(content instanceof ImageGallery){
        console.log("Rendering Image Gallery:");
        console.log(content.render());
        console.log("Summary:");
        console.log(content.getSummary());
    } else {
        console.log("Unknown content type");
    }
}

const article = new Article("My Article", "This is the body of my article.");
const video = new Video("My Video", "http://example.com/video.mp4");
const imageGallery = new ImageGallery("My Gallery", ["http://example.com/image1.jpg", "http://example.com/image2.jpg"]);

displayContent(article);
displayContent(video);
displayContent(imageGallery);


// Forma correcta de aplicar el principio LSP

class Content {
    render() {
        throw new Error("Method 'render()' must be implemented.");
    }
    getSummary() {
        throw new Error("Method 'getSummary()' must be implemented.");
    }
}

class Article extends Content {
    constructor(title, body) {
        super();
        this.title = title;
        this.body = body;
    }
    render() {
        return `${this.title}<p>${this.body}</p>`;
    }
    getSummary() {
        return this.body.substring(0, 100) + "...";
    }
}

class Video extends Content {
    constructor(title, videoUrl) {
        super();
        this.title = title;
        this.videoUrl = videoUrl;
    }
    render() {
        return `${this.title}<video src='${this.videoUrl}' controls></video>`;
    }
    getSummary() {
        return `${this.title} (Video)`;
    }
}

class ImageGallery extends Content {
    constructor(title, images) {
        super();
        this.title = title;
        this.images = images;
    }
    render() {
        const imageTags = this.images.map(image => `<img src='${image}' />`).join('');
        return `${this.title}${imageTags}`;
    }
    getSummary() {
        return `${this.title} (${this.images.length} images)`;
    }
}

class Audio extends Content {
    constructor(title, audioUrl) {
        super();
        this.title = title;
        this.audioUrl = audioUrl;
    }
    render() {
        return `${this.title}<audio src='${this.audioUrl}' controls></audio>`;
    }
    getSummary() {
        return `${this.title} (Audio)`;
    }
}

function displayContent(content) {
    console.log("Rendering content:");
    console.log(content.render());
    console.log("Summary:");
    console.log(content.getSummary());
}

const article1 = new Article("My Article", "This is the body of my article.");
const video1 = new Video("My Video", "http://example.com/video.mp4");
const imageGallery1 = new ImageGallery("My Gallery", ["http://example.com/image1.jpg", "http://example.com/image2.jpg"]);
const audio1 = new Audio("My Audio", "http://example.com/audio.mp3");

displayContent(article1);
displayContent(video1);
displayContent(imageGallery1);
displayContent(audio1);


////////// ---------------------------------------- EXTRA ---------------------------------------- ////////////////////

class Vehicle{
    constructor(maxSpeed){
        if(new.target === Vehicle){
            throw new TypeError("Cannot construct Vehicle instances directly");
        }
        this.currentSpeed = 0;
        this.maxSpeed = maxSpeed
    }
    accelerate(increment){
        throw new Error("Method 'accelerate()' must be implemented.");
    }
    brake(decrement){
        throw new Error("Method 'brake()' must be implemented.");
    }
    toString() {
        return "Vehicle"
    }    
}

class Car extends Vehicle{
    constructor(maxSpeed){
        super(maxSpeed);
    }
    accelerate(increment){
        const newSpeed = this.currentSpeed + increment;
        if(newSpeed <= this.maxSpeed){
            this.currentSpeed = newSpeed;
        }else{
            this.currentSpeed = this.maxSpeed;
        }
    }
    brake(decrement){
        const newSpeed = this.currentSpeed - decrement;
        if(newSpeed >=0){
            this.currentSpeed = newSpeed;
        }else{
            this.currentSpeed = 0;
        }
    }
    toString(){
        return "Auto"
    }
}

class Motorcycle extends Vehicle{
    constructor(maxSpeed){
        super(maxSpeed);
    }
    accelerate(increment){
        const newSpeed = this.currentSpeed + increment;
        if(newSpeed <= this.maxSpeed){
            this.currentSpeed = newSpeed;
        }else{
            this.currentSpeed = this.maxSpeed;
        } 
    }
    brake(decrement){
        const newSpeed = this.currentSpeed - decrement;
        if(newSpeed >=0){
            this.currentSpeed = newSpeed;
        }else{
            this.currentSpeed = 0;
        }
    }
    toString(){
        return "Motocicleta"
    }
}

class Boat extends Vehicle{
    constructor(maxSpeed){
        super(maxSpeed);
    }
    accelerate(increment){
        const newSpeed = this.currentSpeed + increment;
        if(newSpeed <= this.maxSpeed){
            this.currentSpeed = newSpeed;
        }else{
            this.currentSpeed = this.maxSpeed;
        }
    }
    brake(decrement){
        const newSpeed = this.currentSpeed - decrement;
        if(newSpeed >=0){
            this.currentSpeed = newSpeed;
        }else{
            this.currentSpeed = 0;
        }
    }
    toString(){
        return "Bote"
    }
}

function testVehicle(vehicle){
    console.log(`Datos: ${vehicle.toString()}:`);
    console.log(`Velocidad inicial: ${vehicle.currentSpeed} km/h`);
    vehicle.accelerate(50);
    console.log(`Velocidad despues de acelerar: ${vehicle.currentSpeed} km/h`);
    vehicle.brake(20);
    console.log(`Velocidad despues de frenar: ${vehicle.currentSpeed} km/h`);
}

const car = new Car(180);
const motorcycle = new Motorcycle(150);
const boat = new Boat(40);

testVehicle(car);
testVehicle(motorcycle);
testVehicle(boat);


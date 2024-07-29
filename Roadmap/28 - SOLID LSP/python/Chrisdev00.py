"""
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
"""

# Forma incorrecta sin aplicar el principio LSP

class Content:
    def render(self):
        pass
    def get_summary(self):
        pass

class Article(Content):
    def __init__(self, title, body):
        self.title = title
        self.body = body
    def render(self):
        return f"{self.title}<p>{self.body}</p>"    
    def get_summary(self):
        return self.body[:100] + "..."
    
class Video(Content):
    def __init__(self, title, video_url):
        self.title = title
        self.video_url = video_url
    def render(self):
        return f"{self.title}<video src='{self.video_url}' controls></video>"    
    def get_summary(self):
        return f"{self.title} (Video)"
    
class ImageGallery(Content):
    def __init__(self, title, images):
        self.title = title
        self.images = images
    def render(self):
        image_tags = "".join([f"imgagen '{image}' " for image in self.images])
        return f"{self.title}{image_tags}"    
    def get_summary(self):
        return f"{self.title} ({len(self.images)} images)"
    
class Audio(Content):
    def __init__(self, title, audio_url):
        self.title = title
        self.audio_url = audio_url
    def render(self):
        return f"{self.title}<audio src='{self.audio_url}' controls></audio>"    
    def get_summary(self):
        return f"{self.title} (Audio)"    

def display_content(content):
    if isinstance(content, Article):
        print("Rendering Article:")
        print(content.render())
        print("Summary:")
        print(content.get_summary())
    elif isinstance(content, Video):
        print("Rendering Video:")
        print(content.render())
        print("Summary:")
        print(content.get_summary())
    elif isinstance(content, ImageGallery):
        print("Rendering Image Gallery:")
        print(content.render())
        print("Summary:")
        print(content.get_summary())
    elif isinstance(content, Audio):
        print("Rendering Audio:")
        print(content.render())
        print("Summary:")
        print(content.get_summary())
    else:
        print("Unknown content type")

article = Article("My Article", "This is the body of my article.")
video = Video("My Video", "http://example.com/video.mp4")
image_gallery = ImageGallery("My Gallery", ["http://example.com/image1.jpg", "http://example.com/image2.jpg"])
audio = Audio("My Audio", "http://example.com/audio.mp3")

display_content(article)
display_content(video)
display_content(image_gallery)
display_content(audio)


# Forma correcta de aplicar el principio LSP

from abc import ABC, abstractmethod

class Content(ABC):
    @abstractmethod
    def render(self):
        pass
    @abstractmethod
    def get_summary(self):
        pass

class Article(Content):
    def __init__(self,title,body):
        self.title = title
        self.body = body
    def render(self):
        return f"Titulo: {self.title} // Parrafo: {self.body}"    
    def get_summary(self):
        return self.body[:100] + "..."
    
class Video(Content):
    def __init__(self, title, video_url):
        self.title = title
        self.video_url = video_url
    def render(self):
        return f"{self.title} - <url='{self.video_url}'>"    
    def get_summary(self):
        return f"{self.title} (Video)"
    
class ImageGallery(Content):
    def __init__(self, title, images):
        self.title = title
        self.images = images
    def render(self):
        image_tags = "".join([f"<img src='{image}' />" for image in self.images])
        return f"{self.title}:{image_tags}"    
    def get_summary(self):
        return f"{self.title} ({len(self.images)} images)"
    
class Audio(Content):
    def __init__(self, title, audio_url):
        self.title = title
        self.audio_url = audio_url
    def render(self):
        return f"{self.title} - <url='{self.audio_url}'>"    
    def get_summary(self):
        return f"{self.title} (Audio)"
    

def display_content(content: Content):
    print("Rendering content:")
    print(content.render())
    print("Summary:")
    print(content.get_summary())


article = Article("My Article", "This is the body of my article.")
video = Video("My Video", "http://example.com/video.mp4")
image_gallery  = ImageGallery("My Gallery", ["http://example.com/image1.jpg", "http://example.com/image2.jpg"])
audio = Audio("My Audio", "http://example.com/audio.mp3")

display_content(article)
display_content(video)
display_content(image_gallery)
display_content(audio)


################ ------------------------------ EXTRA ---------------------------------- ##############################

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, max_speed):
        self.current_speed = 0
        self.max_speed = max_speed

    @abstractmethod
    def accelerate(self, increment):
        pass

    @abstractmethod
    def brake(self, decrement):
        pass

    def __str__(self):
        return "Vehicle"

class Car(Vehicle):
    def __init__(self, max_speed):
        super().__init__(max_speed)

    def accelerate(self, increment):
        new_speed = self.current_speed + increment
        if new_speed <= self.max_speed:
            self.current_speed = new_speed
        else:
            self.current_speed = self.max_speed

    def brake(self, decrement):
        new_speed = self.current_speed - decrement
        if new_speed >= 0:
            self.current_speed = new_speed
        else:
            self.current_speed = 0

    def __str__(self):
        return "Auto"

class Motorcycle(Vehicle):
    def __init__(self, max_speed):
        super().__init__(max_speed)

    def accelerate(self, increment):
        new_speed = self.current_speed + increment
        if new_speed <= self.max_speed:
            self.current_speed = new_speed
        else:
            self.current_speed = self.max_speed

    def brake(self, decrement):
        new_speed = self.current_speed - decrement
        if new_speed >= 0:
            self.current_speed = new_speed
        else:
            self.current_speed = 0

    def __str__(self):
        return "Motocicleta"

class Bicycle(Vehicle):
    def __init__(self, max_speed):
        super().__init__(max_speed)

    def accelerate(self, increment):
        new_speed = self.current_speed + increment
        if new_speed <= self.max_speed:
            self.current_speed = new_speed
        else:
            self.current_speed = self.max_speed

    def brake(self, decrement):
        new_speed = self.current_speed - decrement
        if new_speed >= 0:
            self.current_speed = new_speed
        else:
            self.current_speed = 0

    def __str__(self):
        return "Bicicleta"

def test_vehicle(vehicle: Vehicle):
    print(f"Datos {vehicle}:")
    print(f"Velocidad inicial: {vehicle.current_speed} km/h")
    vehicle.accelerate(50)
    print(f"Velocidad despues de acelerar: {vehicle.current_speed} km/h")
    vehicle.brake(20)
    print(f"Velocidad despues de frenar: {vehicle.current_speed} km/h")
    print()

car = Car(180)
motorcycle = Motorcycle(150)
bicycle = Bicycle(40)

test_vehicle(car)
test_vehicle(motorcycle)
test_vehicle(bicycle)
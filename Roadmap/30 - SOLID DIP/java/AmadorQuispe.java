package com.amsoft.roadmap.example30;


import java.util.ArrayList;
import java.util.Arrays;
//El principio de inversión de dependencias indica que las clases de un sistema deben depender
//de las abstracciones/interfaces y no de las implementaciones concretas
public class Example30 {
    public static void main(String[] args) {
        /*Viola DIP*/
        UserRepository repository = new UserRepository();
        UserService service = new UserService(repository);
        System.out.println(service.getUsers());
        System.out.println(service.getUser("Amador"));
        /*Cumple DIP*/
        UserRepositoryInterface userRepository = new UserRepositoryImpl();
        UserServiceDIP userService = new UserServiceDIP(userRepository);
        System.out.println(userService.getUsers());
        System.out.println(userService.getUser("Alex"));
        /*EXTRA*/
        NotificationService notificationEmailService = new NotificationService(message -> {
            System.out.println("Enviando mensaje por email: " + message);
        });
        notificationEmailService.sendNotification("Hola como estas");

        NotificationService notificationSMSService = new NotificationService(message -> {
            System.out.println("Enviando mensaje por SMS: " + message);
        });
        notificationSMSService.sendNotification("Hola como estas SMS");

        NotificationService notificationPUSHService = new NotificationService(message -> {
            System.out.println("Enviando mensaje por PUSH: " + message);
        });
        notificationPUSHService.sendNotification("Hola como estas PUSH");
    }
}
/*Viola DIP*/
/*
* En el caso se viola el DIP porque la clase UserService tiene dependencia directa con UserRepository
*
* */
class UserRepository {
    private final ArrayList<String> users = new ArrayList<>(Arrays.asList("Amador","Alex"));
    public ArrayList<String> findAll() {
        return users;
    }

    public String findByName(String name){
        var user = users.stream().filter(u->u.equals(name)).findFirst();
        return user.orElse(null);
    }

}
class UserService {
    UserRepository userRepository;
    UserService(UserRepository userRepository){
        this.userRepository = userRepository;
    }

    public ArrayList<String> getUsers() {
        return userRepository.findAll();
    }

    public String getUser(String name){
        return userRepository.findByName(name);
    }
}

/*Con DIP*/
/*
* Ahora UserService depende de una abstracción, por lo tanto, facilmente podemos cambiar la implementación
* del repositorio implementando la interfaz
* */
interface UserRepositoryInterface {
    ArrayList<String> findAll();
    String findByName(String name);
}
class UserRepositoryImpl implements UserRepositoryInterface {
    private final ArrayList<String> users = new ArrayList<>(Arrays.asList("Amador","Alex"));
    @Override
    public ArrayList<String> findAll() {
        return users;
    }

    @Override
    public String findByName(String name) {
        var user = users.stream().filter(u->u.equals(name)).findFirst();
        return user.orElse(null);
    }
}
class UserServiceDIP {
    UserRepositoryInterface userRepository;
    UserServiceDIP(UserRepositoryInterface userRepository){
        this.userRepository = userRepository;
    }

    public ArrayList<String> getUsers() {
        return userRepository.findAll();
    }

    public String getUser(String name){
        return userRepository.findByName(name);
    }
}

/*  EXTRA  */
interface Notifiable {
    void sendNotification(String message);
}

class NotificationService {
    private final Notifiable notifiable;

    public NotificationService(Notifiable notifiable) {
        this.notifiable = notifiable;
    }
    public void sendNotification(String message){
        this.notifiable.sendNotification(message);
    }
}
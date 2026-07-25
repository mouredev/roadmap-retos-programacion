import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.Scanner;
import java.util.Set;
import java.util.UUID;
import java.util.stream.Collectors;

public class MohamedElderkaoui {
    private static final Map<String, User> users = new HashMap<>();
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("¡Bienvenido a la red social descentralizada!");
        int option;

        do {
            System.out.println("\nMenú:");
            System.out.println("1. Registrar usuario");
            System.out.println("2. Seguir a un usuario");
            System.out.println("3. Dejar de seguir a un usuario");
            System.out.println("4. Crear un post");
            System.out.println("5. Eliminar un post");
            System.out.println("6. Dar like a un post");
            System.out.println("7. Eliminar like de un post");
            System.out.println("8. Ver mi feed");
            System.out.println("9. Ver feed de usuarios seguidos");
            System.out.println("10. Listar usuarios registrados"); // New Option
            System.out.println("11. Salir");
            System.out.print("Seleccione una opción: ");
            try {
                option = scanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Entrada inválida. Por favor ingrese un número.");
                scanner.nextLine(); // limpiar el buffer del scanner
                option = -1; // opción inválida para continuar el bucle
            }
            scanner.nextLine(); // Consumir la línea

            switch (option) {
                case 1 -> registerUser();
                case 2 -> followUser();
                case 3 -> unfollowUser();
                case 4 -> createPost();
                case 5 -> deletePost();
                case 6 -> likePost();
                case 7 -> unlikePost();
                case 8 -> viewMyFeed();
                case 9 -> viewFollowingFeed();
                case 10 -> listUsers(); // Call the new method
                case 11 -> System.out.println("Saliendo de la red social...");
                default -> System.out.println("Opción inválida. Intente nuevamente.");
            }
        } while (option != 11);
    }

    private static void registerUser() {
        System.out.print("Ingrese el nombre de usuario: ");
        String name = scanner.nextLine();
        if (users.containsKey(name)) {
            System.out.println("Error: El usuario ya existe.");
        } else {
            User newUser = new User(name);
            users.put(name, newUser);
            System.out.println("Usuario registrado exitosamente: " + name);
        }
    }

    private static void followUser() {
        User user = findUser("Tu nombre de usuario: ");
        User toFollow = findUser("Nombre del usuario a seguir: ");
        if (user != null && toFollow != null) {
            user.follow(toFollow);
            System.out.println("Ahora sigues a " + toFollow.getName());
        }
    }

    private static void unfollowUser() {
        User user = findUser("Tu nombre de usuario: ");
        User toUnfollow = findUser("Nombre del usuario a dejar de seguir: ");
        if (user != null && toUnfollow != null) {
            user.unfollow(toUnfollow);
            System.out.println("Has dejado de seguir a " + toUnfollow.getName());
        }
    }

    private static void createPost() {
        User user = findUser("Tu nombre de usuario: ");
        if (user != null) {
            System.out.print("Ingrese el texto del post (máximo 200 caracteres): ");
            String text = scanner.nextLine();
            if (text.length() > 200) {
                System.out.println("Error: El texto excede los 200 caracteres.");
            } else {
                Post post = new Post(user, text);
                user.addPost(post);
                System.out.println("Post creado exitosamente: " + post);
            }
        }
    }

    private static void deletePost() {
        User user = findUser("Tu nombre de usuario: ");
        if (user != null) {
            System.out.print("Ingrese el ID del post a eliminar: ");
            String postId = scanner.nextLine();
            boolean success = user.deletePost(postId);
            if (success) {
                System.out.println("Post eliminado exitosamente.");
            } else {
                System.out.println("Error: No se encontró el post con ese ID.");
            }
        }
    }

    private static void likePost() {
        User user = findUser("Tu nombre de usuario: ");
        if (user != null) {
            // Pedir el nombre del autor del post
            System.out.print("Ingrese el nombre del usuario que publicó el post: ");
            String authorName = scanner.nextLine();
            User author = users.get(authorName);

            if (author != null) {
                // Pedir el número del post en el feed del autor
                System.out.print("Ingrese el número del post que desea dar like (1 para el primero, 2 para el segundo, etc.): ");
                int postNumber;
                try {
                    postNumber = scanner.nextInt();
                    scanner.nextLine(); // Limpiar el buffer
                    List<Post> posts = author.getPosts();
                    
                    // Validar el número de post
                    if (postNumber > 0 && postNumber <= posts.size()) {
                        Post post = posts.get(postNumber - 1); // Ajustar el índice (es 0-based)
                        post.addLike(user);
                        System.out.println("Diste like al post de " + author.getName());
                    } else {
                        System.out.println("Error: Número de post inválido.");
                    }
                } catch (InputMismatchException e) {
                    System.out.println("Entrada inválida. Por favor ingrese un número.");
                    scanner.nextLine(); // Limpiar el buffer
                }
            } else {
                System.out.println("Error: Usuario no encontrado.");
            }
        }
    }

    private static void unlikePost() {
        User user = findUser("Tu nombre de usuario: ");
        if (user != null) {
            System.out.print("Ingrese el ID del post a eliminar like: ");
            String postId = scanner.nextLine();
            Post post = findPost(postId);
            if (post != null) {
                post.removeLike(user);
                System.out.println("Eliminaste tu like del post.");
            } else {
                System.out.println("Error: No se encontró el post con ese ID.");
            }
        }
    }

    private static void viewMyFeed() {
        User user = findUser("Tu nombre de usuario: ");
        if (user != null) {
            System.out.println("Tu feed:");
            user.getMyFeed().forEach(System.out::println);
        }
    }

    private static void viewFollowingFeed() {
        User user = findUser("Tu nombre de usuario: ");
        if (user != null) {
            System.out.println("Feed de usuarios que sigues:");
            user.getFollowingFeed().forEach(System.out::println);
        }
    }

    private static void listUsers() {
        if (users.isEmpty()) {
            System.out.println("No hay usuarios registrados actualmente.");
        } else {
            System.out.println("Usuarios registrados:");
            users.values().forEach(user -> System.out.println("- " + user.getName() + " (ID: " + user.getId() + ")"));
        }
    }

    private static User findUser(String prompt) {
        System.out.print(prompt);
        String name = scanner.nextLine();
        User user = users.get(name);
        if (user == null) {
            System.out.println("Error: Usuario no encontrado.");
        }
        return user;
    }

    private static Post findPost(String postId) {
        for (User user : users.values()) {
            Optional<Post> post = user.getPosts().stream()
                                      .filter(p -> p.getId().equals(postId))
                                      .findFirst();
            if (post.isPresent()) {
                return post.get();
            }
        }
        return null;
    }
}

class User {
    private final String id;
    private final String name;
    private final List<User> following = new ArrayList<>();
    private final List<Post> posts = new ArrayList<>();

    public User(String name) {
        this.id = UUID.randomUUID().toString();
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public String getId() {
        return id;
    }

    public List<Post> getPosts() {
        return posts;
    }

    public void follow(User user) {
        if (!following.contains(user)) {
            following.add(user);
        }
    }

    public void unfollow(User user) {
        following.remove(user);
    }

    public void addPost(Post post) {
        posts.add(post);
    }

    public boolean deletePost(String postId) {
        return posts.removeIf(post -> post.getId().equals(postId));
    }

    public List<Post> getMyFeed() {
        return posts.stream()
                    .sorted(Comparator.comparing(Post::getCreationDate).reversed())
                    .limit(10)
                    .collect(Collectors.toList());
    }

    public List<Post> getFollowingFeed() {
        return following.stream()
                        .flatMap(user -> user.getPosts().stream())
                        .sorted(Comparator.comparing(Post::getCreationDate).reversed())
                        .limit(10)
                        .collect(Collectors.toList());
    }
}

class Post {
    private final String id;
    private final User user;
    private final String content;
    private final LocalDateTime creationDate;
    private final Set<User> likes = new HashSet<>();

    public Post(User user, String content) {
        this.id = UUID.randomUUID().toString();
        this.user = user;
        this.content = content;
        this.creationDate = LocalDateTime.now();
    }

    public String getId() {
        return id;
    }

    public LocalDateTime getCreationDate() {
        return creationDate;
    }

    public void addLike(User user) {
        likes.add(user);
    }

    public void removeLike(User user) {
        likes.remove(user);
    }

    @Override
    public String toString() {
        return "Post de " + user.getName() + ": " + content + " | Likes: " + likes.size();
    }
}

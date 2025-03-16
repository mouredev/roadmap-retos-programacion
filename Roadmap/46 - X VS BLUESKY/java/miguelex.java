import java.util.*;

class SocialNetwork {
    private Map<Integer, String> users = new HashMap<>();
    private Map<Integer, Post> posts = new HashMap<>();
    private Map<Integer, Set<Integer>> follows = new HashMap<>();
    private Map<Integer, Set<Integer>> likes = new HashMap<>();

    public void registerUser(int userId, String username) {
        if (users.containsKey(userId)) {
            System.out.println("El usuario con ID " + userId + " ya existe.");
        } else {
            users.put(userId, username);
            System.out.println("Usuario " + username + " registrado con éxito.");
        }
    }

    public void followUser(int followerId, int followeeId) {
        if (!users.containsKey(followerId) || !users.containsKey(followeeId)) {
            System.out.println("Uno de los usuarios no existe.");
            return;
        }
        follows.putIfAbsent(followerId, new HashSet<>());
        follows.get(followerId).add(followeeId);
        System.out.println("Usuario " + followerId + " ahora sigue a " + followeeId + ".");
    }

    public void unfollowUser(int followerId, int followeeId) {
        if (follows.containsKey(followerId) && follows.get(followerId).contains(followeeId)) {
            follows.get(followerId).remove(followeeId);
            System.out.println("Usuario " + followerId + " ha dejado de seguir a " + followeeId + ".");
        } else {
            System.out.println("El usuario " + followerId + " no sigue a " + followeeId + ".");
        }
    }

    public void createPost(int userId, int postId, String text) {
        if (!users.containsKey(userId)) {
            System.out.println("El usuario no existe.");
            return;
        }
        if (text.length() > 200) {
            System.out.println("El texto del post excede los 200 caracteres.");
            return;
        }
        String username = users.get(userId);
        posts.put(postId, new Post(userId, username, postId, text));
        System.out.println("Post creado con éxito.");
    }

    public void deletePost(int postId) {
        if (posts.containsKey(postId)) {
            posts.remove(postId);
            System.out.println("Post eliminado con éxito.");
        } else {
            System.out.println("El post no existe.");
        }
    }

    public void likePost(int userId, int postId) {
        if (!users.containsKey(userId)) {
            System.out.println("El usuario no existe.");
            return;
        }
        if (!posts.containsKey(postId)) {
            System.out.println("El post no existe.");
            return;
        }
        likes.putIfAbsent(userId, new HashSet<>());
        if (likes.get(userId).add(postId)) {
            posts.get(postId).incrementLikes();
            System.out.println("Like añadido al post " + postId + ".");
        } else {
            System.out.println("Ya has hecho like en este post.");
        }
    }

    public void unlikePost(int userId, int postId) {
        if (likes.containsKey(userId) && likes.get(userId).remove(postId)) {
            posts.get(postId).decrementLikes();
            System.out.println("Like eliminado del post " + postId + ".");
        } else {
            System.out.println("El usuario no ha hecho like en el post " + postId + ".");
        }
    }

    public void viewUserFeed(int userId) {
        if (!users.containsKey(userId)) {
            System.out.println("El usuario no existe.");
            return;
        }
        List<Post> userPosts = new ArrayList<>();
        for (Post post : posts.values()) {
            if (post.getUserId() == userId) {
                userPosts.add(post);
            }
        }
        userPosts.sort(Comparator.comparing(Post::getCreatedAt).reversed());
        userPosts.stream().limit(10).forEach(post -> {
            System.out.println(post);
        });
    }

    public void viewFollowedFeed(int userId) {
        if (!users.containsKey(userId)) {
            System.out.println("El usuario no existe.");
            return;
        }
        List<Post> followedPosts = new ArrayList<>();
        if (follows.containsKey(userId)) {
            for (Integer followeeId : follows.get(userId)) {
                for (Post post : posts.values()) {
                    if (post.getUserId() == followeeId) {
                        followedPosts.add(post);
                    }
                }
            }
        }
        followedPosts.sort(Comparator.comparing(Post::getCreatedAt).reversed());
        followedPosts.stream().limit(10).forEach(post -> {
            System.out.println(post);
        });
    }

    public String getUsername(int userId) {
        return users.get(userId);
    }
}

class Post {
    private int userId;
    private String username;
    private int postId;
    private String text;
    private String createdAt;
    private int likes;

    public Post(int userId, String username, int postId, String text) {
        this.userId = userId;
        this.username = username;
        this.postId = postId;
        this.text = text;
        this.createdAt = new Date().toString();
        this.likes = 0;
    }

    public int getUserId() {
        return userId;
    }

    public String getCreatedAt() {
        return createdAt;
    }

    public void incrementLikes() {
        likes++;
    }

    public void decrementLikes() {
        likes--;
    }

    @Override
    public String toString() {
        return "ID: " + userId + ", Usuario: " + username + ", Texto: " + text + ", Fecha: " + createdAt + ", Likes: " + likes;
    }
}

public class miguelex {
    public static void main(String[] args) {
        SocialNetwork network = new SocialNetwork();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Seleccione una opción:");
            System.out.println("1. Registrar usuario");
            System.out.println("2. Seguir a un usuario");
            System.out.println("3. Dejar de seguir a un usuario");
            System.out.println("4. Crear post");
            System.out.println("5. Eliminar post");
            System.out.println("6. Hacer like en un post");
            System.out.println("7. Eliminar like de un post");
            System.out.println("8. Ver feed del usuario");
            System.out.println("9. Ver feed de usuarios seguidos");
            System.out.println("0. Salir");
            System.out.print("Opción: ");

            int option = scanner.nextInt();
            scanner.nextLine();  // Consumir la nueva línea

            switch (option) {
                case 1:
                    System.out.print("ID de usuario: ");
                    int userId = scanner.nextInt();
                    scanner.nextLine();
                    System.out.print("Nombre de usuario: ");
                    String username = scanner.nextLine();
                    network.registerUser(userId, username);
                    break;
                case 2:
                    System.out.print("ID del seguidor: ");
                    int followerId = scanner.nextInt();
                    System.out.print("ID del seguido: ");
                    int followeeId = scanner.nextInt();
                    network.followUser(followerId, followeeId);
                    break;
                case 3:
                    System.out.print("ID del seguidor: ");
                    followerId = scanner.nextInt();
                    System.out.print("ID del seguido: ");
                    followeeId = scanner.nextInt();
                    network.unfollowUser(followerId, followeeId);
                    break;
                case 4:
                    System.out.print("ID de usuario: ");
                    userId = scanner.nextInt();
                    System.out.print("ID del post: ");
                    int postId = scanner.nextInt();
                    scanner.nextLine();
                    System.out.print("Texto del post: ");
                    String text = scanner.nextLine();
                    network.createPost(userId, postId, text);
                    break;
                case 5:
                    System.out.print("ID del post: ");
                    postId = scanner.nextInt();
                    network.deletePost(postId);
                    break;
                case 6:
                    System.out.print("ID de usuario: ");
                    userId = scanner.nextInt();
                    System.out.print("ID del post: ");
                    postId = scanner.nextInt();
                    network.likePost(userId, postId);
                    break;
                case 7:
                    System.out.print("ID de usuario: ");
                    userId = scanner.nextInt();
                    System.out.print("ID del post: ");
                    postId = scanner.nextInt();
                    network.unlikePost(userId, postId);
                    break;
                case 8:
                    System.out.print("ID de usuario: ");
                    userId = scanner.nextInt();
                    network.viewUserFeed(userId);
                    break;
                case 9:
                    System.out.print("ID de usuario: ");
                    userId = scanner.nextInt();
                    network.viewFollowedFeed(userId);
                    break;
                case 0:
                    System.out.println("¡Hasta luego!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Opción no válida. Intente de nuevo.");
                    break;
            }
        }
    }
}

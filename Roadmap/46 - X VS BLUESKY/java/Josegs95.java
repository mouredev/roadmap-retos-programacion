import java.time.LocalDateTime;
import java.time.ZoneOffset;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().socialNetwork();
    }

    private Integer userIDCount = 1;
    private Integer postIDCount = 1;
    private List<User> userList;

    public void socialNetwork(){
        User user1 = createUser("Jose");
        User user2 = createUser("María");
        User user3 = createUser("Ramón");
        User user4 = createUser("Daniel");
        User user5 = createUser("Yolanda");
        userList = Arrays.asList(user1, user2, user3, user4, user5);

        followUser(user1, user2);
        followUser(user1, user5);
        followUser(user2, user1);
        followUser(user2, user3);
        followUser(user2, user4);
        followUser(user2, user5);
        followUser(user3, user5);
        followUser(user4, user5);
        followUser(user5, user2);
        followUser(user5, user3);

        unfollowUser(user4, user5);

        generatePosts();

        for (Post post : user2.getPostList()){
            likePost(user1, post);
            likePost(user2, post);
        }
        for (User user : userList)
            likePost(user, user1.getPostList().get(2));
        likePost(user5, user2.getPostList().get(1));

        unlikePost(user4, user2.getPostList().get(1));
        likePost(user4, user2.getPostList().get(1));
        unlikePost(user4, user2.getPostList().get(1));

        for(User user : userList){
            printOwnFeed(user);
            printUserFeed(user);
        }
    }
    private User createUser(String name){
        return new User(userIDCount++, name);
    }

    private boolean followUser(User user, User following){
        if (user == null || following == null)
            return false;

        return user.follow(following);
    }

    private boolean unfollowUser(User user, User unfollowing){
        if (user == null || unfollowing == null)
            return false;

        return user.unfollow(unfollowing);
    }

    private void createPost(User owner, String text, Integer postId){
        if (text.length() > 200){
            System.out.println("El texto es demasiado largo (max 200).");
            return;
        }
        owner.createPost(text, postId);
    }

    private void deletePost(User owner, Post post){
        if (!post.getOwner().equals(owner)){
            System.out.println("El usuario " + owner + " no es el creador del post");
            return;
        }
        owner.deletePost(post);
    }

    private boolean likePost(User user, Post post){
        if (user == null || post == null)
            return false;

        return user.like(post);
    }

    private boolean unlikePost(User user, Post post){
        if (user == null || post == null)
            return false;

        return user.unlike(post);
    }

    private void printOwnFeed(User user){
        List<Post> posts = getLatestPosts(Arrays.asList(user), 10);
        System.out.println("Imprimiendo la feed de: " + user);

        if (posts.size() == 0){
            System.out.println("No hay nada :( ¡Escribe tu primer post!\n");
            return;
        }
        printPosts(posts);
    }

    private void printUserFeed(User user){
        List<Post> posts = getLatestPosts(user.getFollowingUsers(), 10);
        System.out.println("Imprimiendo la feed de los usuarios que sigue: " + user);

        if (posts.size() == 0){
            System.out.println("No hay nada :( Sigue a usuarios para ver sus posts\n");
            return;
        }
        printPosts(posts);
    }

    private void printPosts(List<Post> posts){
        for (Post post : posts){
            System.out.println("==============================");
            System.out.println("Usuario: " + post.getOwner());
            System.out.println("'" + post.getText() + "' Likes: " + post.getLikesCount()
                    + " Fecha de creación: " + post.getCreationDateFormatted());
            System.out.println("==============================");
        }
        System.out.println("\n");
    }

    private List<Post> getLatestPosts(List<User> users, int limit){
        List<Post> posts = new ArrayList<>();
        for (User user : users){
            posts.addAll(user.getPostList());
        }

        posts.sort(Comparator.comparing(Post::getCreationDate).reversed());
        if (posts.size() > limit)
            posts = posts.subList(0, limit);

        return posts;
    }

    //Lo hago de esta manera tan complicada para poder automatizar los post y así dormir el
    //hilo principal para que se creen los post a diferentes fechas
    private void generatePosts(){
        List<Object[]> postToCreate = new ArrayList<>();
        postToCreate.add(new Object[]{userList.get(0), "Mi primer post"});
        postToCreate.add(new Object[]{userList.get(0), "Mi segundo post"});
        postToCreate.add(new Object[]{userList.get(1), "Hola a todos"});
        postToCreate.add(new Object[]{userList.get(3), "Hola, soy nuevo"});
        for (int i = 1; i < 21; i++)
            postToCreate.add(new Object[]{userList.get(4), "Buenos días, hoy es " + i + " de Diciembre"});
        postToCreate.add(new Object[]{userList.get(1), "Hoy empiezo el gym"});
        postToCreate.add(new Object[]{userList.get(0), "Ya llega la Navidad"});

        try{
            for (Object[] post : postToCreate) {
                createPost((User) post[0], (String) post[1], postIDCount++);
                Thread.sleep(100);
            }
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

        deletePost(userList.get(1), userList.get(1).getPostList().get(1));
        createPost(userList.get(1), "Al final se cancela lo del gym, !A comer polvorones¡", postIDCount++);
    }

    public class User{
        final private Integer ID;
        private String name;
        private List<User> followingUsers;
        private List<Post> postList;
        private List<Post> likedPosts;

        public User(Integer id, String name) {
            this.ID = id;
            this.name = name;
            followingUsers = new ArrayList<>();
            postList = new ArrayList<>();
            likedPosts = new ArrayList<>();
        }

        public boolean follow(User user){
            if (!this.equals(user) && !followingUsers.contains(user))
                return followingUsers.add(user);
            return false;
        }

        public boolean unfollow(User user){
            return followingUsers.remove(user);
        }

        public boolean createPost(String text, Integer idPost){
            return postList.add(new Post(idPost, text,
                    LocalDateTime.now(ZoneOffset.UTC), this));
        }

        public boolean deletePost(Post post){
            return postList.remove(post);
        }

        public boolean like(Post post){
            if (!likedPosts.contains(post)){
                post.like();
                return likedPosts.add(post);
            }
            return false;
        }

        public boolean unlike(Post post){
            if (likedPosts.contains(post))
                post.deleteLike();
            return likedPosts.remove(post);
        }

        public Integer getID() {
            return ID;
        }

        public String getName() {
            return name;
        }

        public List<Post> getPostList() {
            return postList;
        }

        public List<User> getFollowingUsers() {
            return followingUsers;
        }

        @Override
        public String toString(){
            return name + " (ID:" + ID + ")";
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof User user)) return false;
            return Objects.equals(ID, user.ID);
        }

        @Override
        public int hashCode() {
            return Objects.hash(ID, name, followingUsers, postList, likedPosts);
        }
    }

    public class Post{
        final private Integer ID;
        private String text;
        private LocalDateTime creationDate;
        private Integer likesCount;
        private User owner;

        public Post(Integer id, String text, LocalDateTime creationDate, User owner) {
            this.ID = id;
            this.text = text;
            this.creationDate = creationDate;
            this.owner = owner;
            likesCount = 0;
        }

        public void like(){
            likesCount++;
        }

        public void deleteLike(){
            likesCount--;
        }

        public Integer getID() {
            return ID;
        }

        public String getText() {
            return text;
        }

        public LocalDateTime getCreationDate() {
            return creationDate;
        }

        public String getCreationDateFormatted(){
            return creationDate.format(DateTimeFormatter.ofPattern("dd-MM-yyyy kk:mm:ss 'UTC'"));
        }

        public User getOwner() {
            return owner;
        }

        public Integer getLikesCount() {
            return likesCount;
        }
    }
}

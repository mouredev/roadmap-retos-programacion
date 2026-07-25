import lombok.*;
import java.time.LocalDate;
import java.util.*;
import java.util.UUID;

public class Main {

    public static void main(String[] args) {
        // Register users
        User pedro = new User("Pedro");
        User juan = new User("Juan");
        User maria = new User("Maria");
        User ana = new User("Ana");

        // Follow users
        pedro.follow(juan);
        pedro.follow(maria);
        pedro.follow(ana);

        // Create post
        Post postJava = new Post("Java ...", LocalDate.of(2024, 1, 1));
        Post postJs = new Post("JavaScript ...", LocalDate.of(2024, 2, 1));
        Post postPython = new Post("Python ...", LocalDate.of(2024, 3, 1));
        Post postSql = new Post("SQL ...", LocalDate.of(2024, 4, 1));
        Post postNginx = new Post("Nginx ...", LocalDate.of(2024, 5, 1));
        Post postDocker = new Post("Docker ...", LocalDate.of(2024, 6, 1));
        Post postKubernetes = new Post("Kubernetes ...", LocalDate.of(2024, 7, 1));
        Post postUbuntu = new Post("Ubuntu ...", LocalDate.of(2024, 8, 1));
        Post postCertbot = new Post("Certbot ...", LocalDate.of(2024, 9, 1));
        Post postCloudflare = new Post("Cloudflare ...", LocalDate.of(2024, 10, 1));
        Post postGithub = new Post("Github ...", LocalDate.of(2024, 11, 1));
        Post postGitlab = new Post("Gitlab ...", LocalDate.of(2024, 12, 1));

        pedro.createPost(postJava);
        pedro.createPost(postJs);
        pedro.createPost(postPython);
        juan.createPost(postSql);
        juan.createPost(postNginx);
        juan.createPost(postDocker);
        maria.createPost(postKubernetes);
        maria.createPost(postUbuntu);
        maria.createPost(postCertbot);
        ana.createPost(postCloudflare);
        ana.createPost(postGithub);
        ana.createPost(postGitlab);

        // Delete post
        pedro.deletePost(postPython.getId());

        // Like / Dislike
        pedro.getPosts().get(0).like(juan);
        pedro.getPosts().get(0).like(maria);
        pedro.getPosts().get(0).like(ana);
        pedro.getPosts().get(1).like(juan);
        pedro.getPosts().get(1).like(maria);
        pedro.getPosts().get(1).like(ana);
        pedro.getPosts().get(1).dislike(ana);

        // Show user posts
        pedro.showPosts();

        // Show feed
        pedro.showFeed();

    }

    @Getter
    @ToString
    @EqualsAndHashCode
    static class Post {
        private final UUID id = UUID.randomUUID();
        private String content;
        private LocalDate pubDate;
        @Setter
        private User user;
        private final List<User> likes = new ArrayList<>();

        public Post(String content, LocalDate pubDate) {
            if (content.length() > 200) throw new IllegalArgumentException("Post content must be less than 200 characters");
            this.content = content;
            this.pubDate = pubDate;
        }

        public boolean like(User user) {
            if (this.likes.contains(user)) return false;
            this.likes.add(user);
            return true;
        }

        public boolean dislike(User user) {
            return this.likes.remove(user);
        }

        public int getLikes() {
            return this.likes.size();
        }
    }

    @Data
    @AllArgsConstructor
    @NoArgsConstructor
    static class User {
        private final UUID id = UUID.randomUUID();
        private String username;
        private final List<User> following = new ArrayList<>();
        private final List<Post> posts = new ArrayList<>();

        public boolean follow(User user) {
            return this.following.add(user);
        }

        public boolean unfollow(User user) {
            return this.following.remove(user);
        }

        public boolean createPost(Post post) {
            post.setUser(this);
            return this.posts.add(post);
        }

        public boolean deletePost(UUID id) {
            return this.posts.removeIf(p -> p.getId().equals(id));
        }

        public void showPosts() {
            this.posts.sort(Comparator.comparing(Post::getPubDate).reversed());
            System.out.println(this.username + " posts:");
            printPosts(this.posts);
        }

        public void showFeed() {
            List<Post> post = new ArrayList<>();
            this.following.stream()
                    .map(User::getPosts)
                    .forEach(post::addAll);

            post.sort(Comparator.comparing(Post::getPubDate).reversed());
            System.out.println(this.username + " feed:");
            printPosts(post);
        }

        private void printPosts(List<Post> list) {
            list.stream()
                    .limit(10)
                    .forEach(p -> System.out.println(
                            "{" +
                                    "userId=" + this.id +
                                    ", username=" + this.username +
                                    ", content=" + p.getContent() +
                                    ", pubDate=" + p.getPubDate() +
                                    ", likes=" + p.getLikes() +
                                    "}"
                    ));
        }

        public void printFollowing() {
            System.out.println(this.username + " is following:");
            this.following.forEach(user -> System.out.println(user.getUsername()));
        }

    }

}

// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <string>
#include <algorithm>
#include <ctime>

/*
 * EJERCICIO:
 * La alternativa descentralizada a X, Bluesky, comienza a atraer
 * a nuevos usuarios. ¿Cómo funciona una red de este estilo?
 * 
 * Implementa un sistema que simule el comportamiento de estas
 * redes sociales.
 * 
 * Debes crear las siguientes operaciones:
 * - Registrar un usuario por nombre e identificador único.
 * - Un usuario puede seguir/dejar de seguir a otro.
 * - Creación de post asociado a un usuario. Debe poseer
 *   texto (200 caracteres máximo), fecha de creación 
 *   e identificador único.   
 * - Eliminación de un post.
 * - Posibilidad de hacer like (y eliminarlo) en un post.
 * - Visualización del feed de un usuario con sus 10 publicaciones
 *   más actuales ordenadas desde la más reciente.
 * - Visualización del feed de un usuario con las 10 publicaciones
 *   más actuales de los usuarios que sigue ordenadas 
 *   desde la más reciente.
 *   
 * Cuando se visualiza un post, debe mostrarse:
 * ID de usuario, nombre de usuario, texto del post, 
 * fecha de creación y número total de likes.
 * 
 * Controla errores en duplicados o acciones no permitidas.
*/

// Helper struct for representing a post
struct Post {
    std::string postId;
    std::string userId;
    std::string text;
    std::time_t createdAt;
    int likes = 0;

    void displayPost(const std::string &userName) const {
        std::cout << "User ID: " << userId << ", Name: " << userName
                  << ", Post ID: " << postId << ", Text: " << text
                  << ", Created At: " << std::ctime(&createdAt)
                  << ", Likes: " << likes << '\n';
    }
};

class SocialNetwork {
private:
    struct User {
        std::string userId;
        std::string name;
        std::unordered_set<std::string> following;
        std::vector<Post> posts;
    };

    std::unordered_map<std::string, User> users;
    std::unordered_map<std::string, Post*> postMap;

public:
    void registerUser(const std::string &userId, const std::string &name) {
        if (users.count(userId)) {
            throw std::runtime_error("User ID already exists.");
        }
        users[userId] = {userId, name, {}, {}};
    }

    void toggleFollow(const std::string &followerId, const std::string &followedId) {
        if (!users.count(followerId) || !users.count(followedId)) {
            throw std::runtime_error("User ID not found.");
        }
        auto &following = users[followerId].following;
        if (!following.insert(followedId).second) {
            following.erase(followedId);
        }
    }

    void createPost(const std::string &userId, const std::string &postId, const std::string &text) {
        if (!users.count(userId)) {
            throw std::runtime_error("User ID not found.");
        }
        if (postMap.count(postId)) {
            throw std::runtime_error("Post ID already exists.");
        }
        if (text.length() > 200) {
            throw std::runtime_error("Text exceeds maximum length of 200 characters.");
        }
        Post post = {postId, userId, text, std::time(nullptr)};
        users[userId].posts.push_back(post);
        postMap[postId] = &users[userId].posts.back();
    }

    void deletePost(const std::string &postId) {
        if (!postMap.count(postId)) {
            throw std::runtime_error("Post ID not found.");
        }
        auto &post = *postMap[postId];
        auto &userPosts = users[post.userId].posts;
        userPosts.erase(std::remove_if(userPosts.begin(), userPosts.end(),
                                       [&](const Post &p) { return p.postId == postId; }),
                        userPosts.end());
        postMap.erase(postId);
    }

    void toggleLike(const std::string &postId) {
        if (!postMap.count(postId)) {
            throw std::runtime_error("Post ID not found.");
        }
        auto &post = *postMap[postId];
        post.likes = post.likes == 0 ? 1 : 0;
    }

    void getUserFeed(const std::string &userId) const {
        if (!users.count(userId)) {
            throw std::runtime_error("User ID not found.");
        }
        const auto &posts = users.at(userId).posts;
        displayFeed(posts);
    }

    void getFollowingFeed(const std::string &userId) const {
        if (!users.count(userId)) {
            throw std::runtime_error("User ID not found.");
        }
        std::vector<Post> feed;
        for (const auto &followedId : users.at(userId).following) {
            const auto &posts = users.at(followedId).posts;
            feed.insert(feed.end(), posts.begin(), posts.end());
        }
        std::sort(feed.begin(), feed.end(), [](const Post &a, const Post &b) {
            return a.createdAt > b.createdAt;
        });
        displayFeed(feed);
    }

private:
    void displayFeed(const std::vector<Post> &posts) const {
        int count = 0;
        for (const auto &post : posts) {
            if (++count > 10) break;
            const auto &user = users.at(post.userId);
            post.displayPost(user.name);
        }
    }
};

int main() {
    SocialNetwork sn;
    try {
        sn.registerUser("u1", "Alice");
        sn.registerUser("u2", "Bob");

        sn.toggleFollow("u1", "u2");

        sn.createPost("u1", "p1", "Hello, this is Alice!");
        sn.createPost("u2", "p2", "Hi, this is Bob's post.");
        sn.toggleLike("p2");

        std::cout << "\n[+] - User Feed for Alice:\n";
        sn.getUserFeed("u1");

        std::cout << "\n[+] - Following Feed for Alice:\n";
        sn.getFollowingFeed("u1");

        sn.deletePost("p1");
        std::cout << "\n[+] - After Deleting Alice's Post:\n";
        sn.getUserFeed("u1");
    } catch (const std::exception &ex) {
        std::cerr << "Error: " << ex.what() << '\n';
    }
    return 0;
}

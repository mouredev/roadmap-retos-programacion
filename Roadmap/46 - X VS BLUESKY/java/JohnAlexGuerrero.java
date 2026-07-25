package org.example;

import java.util.HashSet;
import java.util.Objects;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        SocialNetwork socialnetwork = new SocialNetwork();

        //- Registrar un usuario por defecto con nombre e identificador único.
        socialnetwork.registerUser("u123", "alexander guerrero");
        socialnetwork.registerUser("u456", "sandra estacio");
        socialnetwork.registerUser("u467", "carolina maigual");
        socialnetwork.registerUser("u897", "mileidy cruz");
        socialnetwork.registerUser("u230", "daniel botina");
        socialnetwork.registerUser("u239", "diego botina");
        socialnetwork.registerUser("u348", "gloria maigual");
        socialnetwork.registerUser("u438", "teresa maigual");
        socialnetwork.registerUser("u489", "alejandra rojas");

        //- Seleccionar un usuario
        User u1 = socialnetwork.getUser("u489");
        //- Un usuario puede seguir/dejar de seguir a otro.
        u1.followUser("u348");
        u1.followUser("u467");
        u1.followUser("u897");

        //- Mostrar usuarios
        for (User user : socialnetwork.getUsers()) {
            System.out.println(user.toString());
        }
    }
}

class SocialNetwork{
    private static HashSet<User> users;
    public SocialNetwork() {
        users = new HashSet<>();
    }
    public void registerUser(String id, String name){
        users.add(new User(id, name));
    }
    public User getUser(String id){
        for(User user: users){
            if(user.getId().equals(id)){
                return user;
            }
        }
        return null;
    }
    public void unfollowUser(){}
    public HashSet<User> getUsers() {
        return users;
    }
}

class User{
    private String id;
    private String name;
    private HashSet<String> followers;
    private HashSet<String> following;
    public void followUser(String followIdUser){
        followers.add(followIdUser);
    }

    public User(String id, String name) {
        this.id = id;
        this.name = name;
        this.followers = new HashSet<String>();
        this.following = new HashSet<String>();
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public HashSet<String> getFollowers() {
        return followers;
    }

    public HashSet<String> getFollowing() {
        return following;
    }

    @Override
    public String toString() {
        return "User{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", followers=" + followers +
                ", following=" + following +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        User user = (User) o;
        return Objects.equals(id, user.id) && Objects.equals(name, user.name) && Objects.equals(followers, user.followers) && Objects.equals(following, user.following);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, name, followers, following);
    }
}

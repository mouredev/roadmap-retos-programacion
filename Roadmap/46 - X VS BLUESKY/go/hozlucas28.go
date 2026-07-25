package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"slices"
	"strings"
	"sync"
	"time"
)

/* -------------------------------------------------------------------------- */
/*                                 STRUCTURES                                 */
/* -------------------------------------------------------------------------- */

/* ---------------------------------- Post ---------------------------------- */

type Post interface {
	GetAuthor() string
	GetContent() string
	GetDate() *time.Time
	GetID() string
	GetLikes() []string

	AddLike(uName string) error
	RemoveLike(uName string) error
}

type post struct {
	author  string
	content string
	date    *time.Time
	id      string
	likes   []string
	_       struct{}
}

func NewPost(author string, content string) (Post, error) {
	var database Database = DatabaseInstance()

	var id string
	var currentDate time.Time = time.Now()

	if len(content) > 200 {
		return nil, errors.New("Content of the post exceed the maximum length (200 chars)")
	}

	id = fmt.Sprintf("%s %d", author, len(database.GetPosts()))

	var post post = post{
		author:  author,
		content: content,
		date:    &currentDate,
		id:      id,
		likes:   []string{},
	}

	return &post, nil
}

func (post *post) GetAuthor() string {
	return post.author
}

func (post *post) GetContent() string {
	return post.content
}

func (post *post) GetDate() *time.Time {
	return post.date
}

func (post *post) GetID() string {
	return post.id
}

func (post *post) GetLikes() []string {
	return post.likes
}

func (post *post) AddLike(uName string) error {
	var errMsg string

	if slices.Contains(post.likes, uName) {
		errMsg = fmt.Sprintf("\"%s\" like already exists", uName)
		return errors.New(errMsg)
	}

	post.likes = append(post.likes, uName)
	return nil
}

func (post *post) RemoveLike(uName string) error {
	var errMsg string

	likeI := slices.Index(post.likes, uName)
	if likeI == -1 {
		errMsg = fmt.Sprintf("\"%s\" like doesn't  exist", uName)
		return errors.New(errMsg)
	}

	post.likes = slices.Concat(post.likes[0:likeI], post.likes[likeI+1:])
	return nil
}

/* ---------------------------------- User ---------------------------------- */

type User interface {
	GetUName() string
	GetFollowers() []string
	GetFollowings() []string
	GetPosts() []string

	CreatePost(content string) error
	DeletePost(id string) error
	Follow(uName string) error
	LikePost(id string) error
	Unfollow(uName string) error
	UnlikePost(id string) error

	addFollower(uName string)
	removeFollower(uName string) error
}

type user struct {
	followers  []string
	followings []string
	posts      []string
	uName      string
	_          struct{}
}

func NewUser(uName string) User {
	var user user = user{
		followers:  []string{},
		followings: []string{},
		posts:      []string{},
		uName:      uName,
	}

	return &user
}

func (user *user) GetUName() string {
	return user.uName
}

func (user *user) GetFollowers() []string {
	return user.followers
}

func (user *user) GetFollowings() []string {
	return user.followings
}

func (user *user) GetPosts() []string {
	return user.posts
}

func (user *user) CreatePost(content string) error {
	var database Database = DatabaseInstance()

	post, err := NewPost((*user).GetUName(), content)
	if err != nil {
		return err
	}

	database.addNewPost(&post)
	user.posts = append(user.posts, post.GetID())
	return nil
}

func (user *user) DeletePost(id string) error {
	var errMsg string
	var database Database = DatabaseInstance()

	var postI int = slices.Index(user.posts, id)
	if postI == -1 {
		errMsg = fmt.Sprintf("\"%s\" doesn't posted the post with \"%s\" id", user.uName, id)
		return errors.New(errMsg)
	}

	database.deletePost(id)
	user.posts = slices.Concat(user.posts[0:postI], user.posts[postI+1:])
	return nil
}

func (user *user) Follow(uName string) error {
	var errMsg string
	var database Database = DatabaseInstance()

	var followingI int = slices.Index(user.followings, uName)
	if followingI != -1 {
		errMsg = fmt.Sprintf("\"%s\" already follows \"%s\"", user.uName, uName)
		return errors.New(errMsg)
	}

	userFollowed, err := database.GetUser(uName)
	if err != nil {
		return err
	}

	(*userFollowed).addFollower(user.uName)
	user.followings = append(user.followings, uName)
	return nil
}

func (user *user) LikePost(id string) error {
	var database Database = DatabaseInstance()

	post, err := database.GetPost(id)
	if err != nil {
		return err
	}

	(*post).AddLike(user.uName)
	return nil
}

func (user *user) Unfollow(uName string) error {
	var errMsg string
	var database Database = DatabaseInstance()

	var followingI int = slices.Index(user.followings, uName)
	if followingI == -1 {
		errMsg = fmt.Sprintf("\"%s\" doesn't follow \"%s\"", user.uName, uName)
		return errors.New(errMsg)
	}

	userUnfollowed, err := database.GetUser(uName)
	if err != nil {
		return err
	}

	(*userUnfollowed).removeFollower(user.uName)
	user.followings = slices.Concat(user.followings[0:followingI], user.followings[followingI+1:])
	return nil
}

func (user *user) UnlikePost(id string) error {
	var database Database = DatabaseInstance()

	post, err := database.GetPost(id)
	if err != nil {
		return err
	}

	(*post).RemoveLike(user.uName)
	return nil
}

func (user *user) addFollower(uName string) {
	user.followers = append(user.followers, uName)
}

func (user *user) removeFollower(uName string) error {
	var errMsg string

	var followerI int = slices.Index(user.followers, uName)
	if followerI == -1 {
		errMsg = fmt.Sprintf("\"%s\" isn't follow by \"%s\"", user.uName, uName)
		return errors.New(errMsg)
	}

	user.followers = slices.Concat(user.followers[0:followerI], user.followers[followerI+1:])
	return nil
}

/* -------------------------------- Database -------------------------------- */

type Database interface {
	GetPosts() []*Post
	GetUsers() []*User

	GetUser(uName string) (*User, error)
	GetPost(id string) (*Post, error)
	GetUserFollowingsPosts(uName string) ([]*Post, error)
	GetUserPosts(uName string) ([]*Post, error)
	DeleteUser(uName string) error
	PostUser(newUser *User) error

	addNewPost(newPost *Post)
	deletePost(postID string) error
}

type database struct {
	posts []*Post
	users []*User
	_     struct{}
}

var databaseInstance *database
var databaseMutex *sync.Mutex = &sync.Mutex{}

func DatabaseInstance() Database {
	if databaseInstance == nil {
		databaseMutex.Lock()
		defer databaseMutex.Unlock()

		if databaseInstance == nil {
			databaseInstance = &database{}
		}
	}

	return databaseInstance
}

func (database *database) GetPosts() []*Post {
	return database.posts
}

func (database *database) GetUsers() []*User {
	return database.users
}

func (database *database) GetUser(uName string) (*User, error) {
	var errMsg string

	for _, user := range database.users {
		if (*user).GetUName() == uName {
			return user, nil
		}
	}

	errMsg = fmt.Sprintf("\"%s\" username not found", uName)
	return nil, errors.New(errMsg)
}

func (database *database) GetPost(id string) (*Post, error) {
	var errMsg string

	for _, post := range database.posts {
		if (*post).GetID() == id {
			return post, nil
		}
	}

	errMsg = fmt.Sprintf("\"%s\" id post not found", id)
	return nil, errors.New(errMsg)
}

func (database *database) GetUserFollowingsPosts(uName string) ([]*Post, error) {
	var followingPosts []*Post
	var followingsPosts []*Post = []*Post{}

	user, err := database.GetUser(uName)
	if err != nil {
		return nil, err
	}

	for _, following := range (*user).GetFollowings() {
		followingPosts, err = database.GetUserPosts(following)
		if err == nil {
			followingsPosts = append(followingsPosts, followingPosts...)
		}
	}

	return followingsPosts, nil
}

func (database *database) GetUserPosts(uName string) ([]*Post, error) {
	var post *Post
	var userPosts []*Post = []*Post{}

	user, err := database.GetUser(uName)
	if err != nil {
		return nil, err
	}

	for _, postID := range (*user).GetPosts() {
		post, err = database.GetPost(postID)
		if err == nil {
			userPosts = append(userPosts, post)
		}
	}

	return userPosts, nil
}

func (database *database) DeleteUser(uName string) error {
	var errMsg string

	var userI int = slices.IndexFunc(database.users, func(user *User) bool {
		return (*user).GetUName() == uName
	})

	if userI == -1 {
		errMsg = fmt.Sprintf("\"%s\" doesn't exist", uName)
		return errors.New(errMsg)
	}

	database.users = slices.Concat(database.users[0:userI], database.users[userI+1:])
	return nil
}

func (database *database) PostUser(newUser *User) error {
	var errMsg string

	var userI int = slices.IndexFunc(database.users, func(user *User) bool {
		return (*user).GetUName() == (*newUser).GetUName()
	})

	if userI != -1 {
		errMsg = fmt.Sprintf("\"%s\" already exists", (*newUser).GetUName())
		return errors.New(errMsg)
	}

	database.users = append(database.users, newUser)
	return nil
}

func (database *database) addNewPost(newPost *Post) {
	database.posts = append(database.posts, newPost)
}

func (database *database) deletePost(postID string) error {
	var errMsg string

	var postI int = slices.IndexFunc(database.posts, func(post *Post) bool {
		return (*post).GetID() == postID
	})

	if postI == -1 {
		errMsg = fmt.Sprintf("\"%s\" id post doesn't exist", postID)
		return errors.New(errMsg)
	}

	database.posts = slices.Concat(database.posts[0:postI], database.posts[postI+1:])
	return nil
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	var err error
	var database Database = DatabaseInstance()

	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var input01 int
	var input02 int

	var uName string
	var postID string
	var postContent string

	var user *User
	var posts []*Post

	fmt.Println(
		"> Available operations...\n\n",
		"  1 - Sign up a new user.\n",
		"  2 - Sign in as user.\n",
		"  0 - Exit.",
	)

	fmt.Printf("\n> Enter an operation: ")
	fmt.Scanf("%d\n", &input01)

	for input01 != 0 {
	input01SW:
		switch input01 {
		case 1:
			fmt.Printf("\n> Username: ")
			uName, _ = reader.ReadString('\n')
			uName = strings.TrimSpace(uName)

			_user := NewUser(uName)
			database.PostUser(&_user)
			break input01SW

		case 2:
			fmt.Printf("\n> Username: ")
			uName, _ = reader.ReadString('\n')
			uName = strings.TrimSpace(uName)

			user, err = database.GetUser(uName)
			if err != nil {
				fmt.Println("\n> Username not found.")
				break input01SW
			}

			fmt.Println(
				"\n> Available operations...\n\n",
				"  1 - Create a new post.\n",
				"  2 - Show personal feed.\n",
				"  3 - Show following feed.\n",
				"  4 - Delete post.\n",
				"  5 - Follow user.\n",
				"  6 - Unfollow user.\n",
				"  7 - Like post.\n",
				"  8 - Unlike post.\n",
				"  0 - Exit.",
			)

			fmt.Printf("\n> Enter an operation: ")
			fmt.Scanf("%d\n", &input02)

			for input02 != 0 {
			input02SW:
				switch input02 {
				case 1:
					fmt.Printf("\n> Post content (maximum 200 characters): ")
					postContent, _ = reader.ReadString('\n')
					postContent = strings.TrimSpace(postContent)

					(*user).CreatePost(postContent)
					break input02SW

				case 2:
					posts, err = database.GetUserPosts((*user).GetUName())
					if err != nil {
						fmt.Println("\n> Error! An error occurred on get user posts.")
						break input02SW
					}

					slices.SortFunc(posts,
						func(a *Post, b *Post) int {
							var _a Post = *a
							var _b Post = *b
							return _b.GetDate().Compare(*_a.GetDate())
						})

					for _, _post := range posts {
						fmt.Printf("\n> ID: \"%s\".\n", (*_post).GetID())
						fmt.Printf("> Author: \"%s\".\n", (*_post).GetAuthor())
						fmt.Printf("> Content: \"%s\".\n", (*_post).GetContent())
						fmt.Printf("> Creation date: \"%s\".\n", (*_post).GetDate())
						fmt.Printf("> Likes: %d.\n", len((*_post).GetLikes()))
					}
					break input02SW

				case 3:
					posts, err = database.GetUserFollowingsPosts((*user).GetUName())
					if err != nil {
						fmt.Println("\n> Error! An error occurred on get user posts.")
						break input02SW
					}

					slices.SortFunc(posts,
						func(a *Post, b *Post) int {
							var _a Post = *a
							var _b Post = *b
							return _b.GetDate().Compare(*_a.GetDate())
						})

					for _, _post := range posts {
						fmt.Printf("\n> ID: \"%s\".\n", (*_post).GetID())
						fmt.Printf("> Author: \"%s\".\n", (*_post).GetAuthor())
						fmt.Printf("> Content: \"%s\".\n", (*_post).GetContent())
						fmt.Printf("> Creation date: \"%s\".\n", (*_post).GetDate())
						fmt.Printf("> Likes: %d.\n", len((*_post).GetLikes()))
					}
					break input02SW

				case 4:
					fmt.Printf("\n> Post ID: ")
					postID, _ = reader.ReadString('\n')
					postID = strings.TrimSpace(postID)

					(*user).DeletePost(postID)
					break input02SW

				case 5:
					fmt.Printf("\n> Username: ")
					uName, _ = reader.ReadString('\n')
					uName = strings.TrimSpace(uName)

					(*user).Follow(uName)
					break input02SW

				case 6:
					fmt.Printf("\n> Username: ")
					uName, _ = reader.ReadString('\n')
					uName = strings.TrimSpace(uName)

					(*user).Unfollow(uName)
					break input02SW

				case 7:
					fmt.Printf("\n> Post ID: ")
					postID, _ = reader.ReadString('\n')
					postID = strings.TrimSpace(postID)

					(*user).LikePost(postID)
					break input02SW

				case 8:
					fmt.Printf("\n> Post ID: ")
					postID, _ = reader.ReadString('\n')
					postID = strings.TrimSpace(postID)

					(*user).UnlikePost(postID)
					break input02SW

				default:
					fmt.Println("\n> Invalid operation! Try again...")
				}

				fmt.Println(
					"\n> Available operations...\n\n",
					"  1 - Create a new post.\n",
					"  2 - Show personal feed.\n",
					"  3 - Show following feed.\n",
					"  4 - Delete post.\n",
					"  5 - Follow user.\n",
					"  6 - Unfollow user.\n",
					"  7 - Like post.\n",
					"  8 - Unlike post.\n",
					"  0 - Exit.",
				)

				fmt.Printf("\n> Enter an operation: ")
				fmt.Scanf("%d\n", &input02)
			}
			break input01SW

		default:
			fmt.Println("\n> Invalid operation! Try again...")
		}

		fmt.Println(
			"\n> Available operations...\n\n",
			"  1 - Sign up a new user.\n",
			"  2 - Sign in as user.\n",
			"  0 - Exit.",
		)

		fmt.Printf("\n> Enter an operation: ")
		fmt.Scanf("%d\n", &input01)
	}
}

# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,broad-exception-raised,raise-missing-from

from abc import ABCMeta, abstractmethod
from datetime import datetime
from typing import Any
from uuid import UUID, uuid4

# ---------------------------------------------------------------------------- #
#                                    CLASSES                                   #
# ---------------------------------------------------------------------------- #

# ----------------------------------- Post ----------------------------------- #


class AbcPost(metaclass=ABCMeta):
    @property
    @abstractmethod
    def uid(self) -> UUID:
        pass

    @property
    @abstractmethod
    def content(self) -> str:
        pass

    @property
    @abstractmethod
    def date(self) -> datetime:
        pass

    @property
    @abstractmethod
    def author(self) -> str:
        pass

    @property
    @abstractmethod
    def likes(self) -> list[str]:
        pass

    @abstractmethod
    def add_like(self, *, _u_name: str) -> None:
        pass

    @abstractmethod
    def remove_like(self, *, _u_name: str) -> None:
        pass


class Post(AbcPost):
    __uid: UUID
    __content: str
    __date: datetime
    __author: str
    __likes: list[str]

    def __init__(self, *, author: str, content: str) -> None:
        if len(content) > 200:
            raise Exception("Content of the post exceed the maximum length (200 chars)")

        self.__uid = uuid4()
        self.__content = content
        self.__date = datetime.now()
        self.__author = author
        self.__likes = []

    @property
    def uid(self) -> UUID:
        return self.__uid

    @property
    def content(self) -> str:
        return self.__content

    @property
    def date(self) -> datetime:
        return self.__date

    @property
    def author(self) -> str:
        return self.__author

    @property
    def likes(self) -> list[str]:
        return self.__likes

    def add_like(self, *, _u_name: str) -> None:
        try:
            self.__likes.index(_u_name)
            raise Exception(f"'{_u_name}' like already exists")
        except ValueError:
            self.__likes.append(_u_name)

    def remove_like(self, *, _u_name: str) -> None:
        try:
            like_index: int = self.__likes.index(_u_name)
            self.__likes.pop(like_index)
        except ValueError:
            raise Exception(f"'{_u_name}' like doesn't  exist")


# ----------------------------------- User ----------------------------------- #


class AbcUser(metaclass=ABCMeta):
    @property
    @abstractmethod
    def u_name(self) -> str:
        pass

    @property
    @abstractmethod
    def followers(self) -> list[str]:
        pass

    @property
    @abstractmethod
    def followings(self) -> list[str]:
        pass

    @property
    @abstractmethod
    def posts(self) -> list[UUID]:
        pass

    @abstractmethod
    def add_follower(self, *, _u_name: str) -> None:
        pass

    @abstractmethod
    def remove_follower(self, *, _u_name: str) -> None:
        pass

    @abstractmethod
    def create_post(self, *, content: str) -> None:
        pass

    @abstractmethod
    def delete_post(self, *, uid: UUID) -> None:
        pass

    @abstractmethod
    def follow(self, *, _u_name: str) -> None:
        pass

    @abstractmethod
    def like_post(self, *, uid: UUID) -> None:
        pass

    @abstractmethod
    def unfollow(self, *, _u_name: str) -> None:
        pass

    @abstractmethod
    def unlike_post(self, *, uid: UUID) -> None:
        pass


class User(AbcUser):
    __followers: list[str]
    __followings: list[str]
    __posts: list[UUID]
    __u_name: str

    def __init__(self, *, _u_name: str) -> None:
        self.__followers = []
        self.__followings = []
        self.__posts = []
        self.__u_name = _u_name

    @property
    def u_name(self) -> str:
        return self.__u_name

    @property
    def followers(self) -> list[str]:
        return self.__followers

    @property
    def followings(self) -> list[str]:
        return self.__followings

    @property
    def posts(self) -> list[UUID]:
        return self.__posts

    def add_follower(self, *, _u_name: str) -> None:
        self.__followers.append(_u_name)

    def remove_follower(self, *, _u_name: str) -> None:
        try:
            follower_index: int = self.__followers.index(_u_name)
            self.__followers.pop(follower_index)
        except ValueError:
            raise Exception(f"'{self.__u_name}' isn't follow by '{_u_name}'")

    def create_post(self, *, content: str) -> None:
        _post: AbcPost = Post(author=self.u_name, content=content)
        _database: Database = Database()

        _database.add_new_post(new_post=_post)
        self.__posts.append(_post.uid)

    def delete_post(self, *, uid: UUID) -> None:
        _database: Database = Database()

        try:
            post_index: int = self.__posts.index(uid)
            _database.delete_post(uid=uid)
            self.__posts.pop(post_index)
        except ValueError:
            raise Exception(f"'{self.u_name}' doesn't posted the post with '{uid}' id")

    def follow(self, *, _u_name: str) -> None:
        _database: Database = Database()

        try:
            self.__followings.index(_u_name)
            raise Exception(f"'{self.u_name}' already follows '{_u_name}'")
        except ValueError:
            user_followed: AbcUser | None = _database.get_user(_u_name=_u_name)
            if user_followed is None:
                raise Exception(f"'{self.u_name}' doesn't exist")

            user_followed.add_follower(_u_name=self.u_name)
            self.__followings.append(_u_name)

    def like_post(self, *, uid: UUID) -> None:
        _database: Database = Database()

        _post: AbcPost | None = _database.get_post(uid=uid)
        if _post is None:
            raise Exception(f"'{uid}' post doesn't exist")

        _post.add_like(_u_name=self.u_name)

    def unfollow(self, *, _u_name: str) -> None:
        _database: Database = Database()

        try:
            _following_index: int = self.__followings.index(_u_name)

            user_unfollowed: AbcUser | None = _database.get_user(_u_name=_u_name)
            if user_unfollowed is None:
                raise Exception(f"'{self.u_name}' doesn't exist")

            user_unfollowed.remove_follower(_u_name=self.u_name)
            self.__followings.pop(_following_index)
        except ValueError:
            raise Exception(f"'{self.u_name}' doesn't follow '{_u_name}'")

    def unlike_post(self, *, uid: UUID) -> None:
        _database: Database = Database()

        _post: AbcPost | None = _database.get_post(uid=uid)
        if _post is None:
            raise Exception(f"'{uid}' post doesn't exist")

        _post.remove_like(_u_name=self.u_name)


# --------------------------------- Database --------------------------------- #


class Singleton(type):
    __instances: dict[Any, Any] = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls.__instances:
            instance: Any = super().__call__(*args, **kwds)
            cls.__instances[cls] = instance

        return cls.__instances[cls]


# class AbcDatabase(metaclass=ABCMeta):
#     @property
#     @abstractmethod
#     def posts(self) -> list[AbcPost]:
#         pass

#     @property
#     @abstractmethod
#     def users(self) -> list[AbcUser]:
#         pass

#     @abstractmethod
#     def get_user(self, *, u_name: str) -> AbcUser | None:
#         pass

#     @abstractmethod
#     def get_post(self, *, uid: UUID) -> AbcPost | None:
#         pass

#     @abstractmethod
#     def get_user_followings_posts(self, *, u_name: str) -> list[AbcPost]:
#         pass

#     @abstractmethod
#     def get_user_posts(self, *, u_name: str) -> list[AbcPost]:
#         pass

#     @abstractmethod
#     def delete_user(self, *, u_name: str) -> None:
#         pass

#     @abstractmethod
#     def post_user(self, *, new_user: AbcUser) -> None:
#         pass

#     @abstractmethod
#     def add_new_post(self, *, new_post: AbcPost) -> None:
#         pass

#     @abstractmethod
#     def delete_post(self, *, uid: UUID) -> None:
#         pass


class Database(metaclass=Singleton):
    __posts: list[AbcPost]
    __users: list[AbcUser]

    def __init__(self) -> None:
        self.__posts = []
        self.__users = []

    @property
    def posts(self) -> list[AbcPost]:
        return self.__posts

    @property
    def users(self) -> list[AbcUser]:
        return self.__users

    def get_user(self, *, _u_name: str) -> AbcUser | None:
        for _user in self.__users:
            if _user.u_name == _u_name:
                return _user

        return None

    def get_post(self, *, uid: UUID) -> AbcPost | None:
        for _post in self.__posts:
            if str(_post.uid) == str(object=uid):
                return _post

        return None

    def get_user_followings_posts(self, *, _u_name: str) -> list[AbcPost]:
        followings_posts: list[AbcPost] = []

        _user: AbcUser | None = self.get_user(_u_name=_u_name)
        if _user is None:
            raise Exception(f"'{_u_name}' doesn't exist")

        for following in _user.followings:
            following_posts: list[AbcPost] = self.get_user_posts(_u_name=following)
            followings_posts.append(*following_posts)

        return followings_posts

    def get_user_posts(self, *, _u_name: str) -> list[AbcPost]:
        user_posts: list[AbcPost] = []

        _user: AbcUser | None = self.get_user(_u_name=_u_name)
        if _user is None:
            raise Exception(f"'{_u_name}' doesn't exist")

        for uid in _user.posts:
            _post: AbcPost | None = self.get_post(uid=uid)
            if _post is not None:
                user_posts.append(_post)

        return user_posts

    def delete_user(self, *, _u_name: str) -> None:
        user_index: int = -1

        for _i, _user in enumerate(iterable=self.__users):
            if _user.u_name == _u_name:
                user_index = _i
                break

        if user_index < 0:
            raise Exception(f"'{_u_name}' doesn't exist")

        self.__users.pop(user_index)

    def post_user(self, *, new_user: AbcUser) -> None:
        user_index: int = -1

        for _i, _user in enumerate(iterable=self.__users):
            if _user.u_name == new_user.u_name:
                user_index = _i
                break

        if user_index >= 0:
            raise Exception(f"'{new_user.u_name}' already exists")

        self.__users.append(new_user)

    def add_new_post(self, *, new_post: AbcPost) -> None:
        self.__posts.append(new_post)

    def delete_post(self, *, uid: UUID) -> None:
        post_index: int = -1

        for _i, _post in enumerate(iterable=self.__posts):
            if str(_post.uid) == str(uid):
                post_index = _i
                break

        if post_index < 0:
            raise Exception(f"'{uid}' doesn't exist")

        self.__posts.pop(post_index)


# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #

database: Database = Database()

print(str(uuid4()))

print(
    "> Available operations...\n\n"
    "  1 - Sign up a new user.\n"
    "  2 - Sign in as user.\n"
    "  0 - Exit."
)

input_01: str = input("\n> Enter an operation: ").strip()

while input_01 != "0":
    match input_01:
        case "0":
            pass

        case "1":
            u_name: str = input("\n> Username: ").strip()
            user = User(_u_name=u_name)
            database.post_user(new_user=user)

        case "2":
            u_name = input("\n> Username: ").strip()
            user: AbcUser | None = database.get_user(_u_name=u_name)
            if user is not None:
                print(
                    "\n> Available operations...\n\n"
                    "  1 - Create a new post.\n"
                    "  2 - Show personal feed.\n"
                    "  3 - Show following feed.\n"
                    "  4 - Delete post.\n"
                    "  5 - Follow user.\n"
                    "  6 - Unfollow user.\n"
                    "  7 - Like post.\n"
                    "  8 - Unlike post.\n"
                    "  0 - Exit."
                )

                input_02: str = input("\n> Enter an operation: ").strip()

                while input_02 != "0":
                    match input_02:
                        case "0":
                            pass

                        case "1":
                            post_content: str = input(
                                "\n> Post content (maximum 200 characters): "
                            ).strip()
                            user.create_post(content=post_content)

                        case "2":
                            posts: list[AbcPost] = database.get_user_posts(
                                _u_name=user.u_name
                            )

                            posts.sort(key=lambda post: post.date, reverse=True)

                            for i, post in enumerate(iterable=posts):
                                if i > 10:
                                    break

                                print(f"\n> ID: '{post.uid}'.")
                                print(f"> Author: '{post.author}'.")
                                print(f"> Content: '{post.content}'.")
                                print(f"> Creation date: '{post.date}'.")
                                print(f"> Likes: {len(post.likes)}.")

                        case "3":
                            posts = database.get_user_followings_posts(
                                _u_name=user.u_name
                            )

                            posts.sort(key=lambda post: post.date, reverse=True)

                            for i, post in enumerate(iterable=posts):
                                if i > 10:
                                    break

                                print(f"\n> ID: '{post.uid}'.")
                                print(f"> Author: '{post.author}'.")
                                print(f"> Content: '{post.content}'.")
                                print(f"> Creation date: '{post.date}'.")
                                print(f"> Likes: {len(post.likes)}.")

                        case "4":
                            post_uid: UUID = input("\n> Post ID: ").strip()  # type: ignore
                            user.delete_post(uid=post_uid)

                        case "5":
                            u_name = input("\n> Username: ").strip()
                            user.follow(_u_name=u_name)

                        case "6":
                            u_name = input("\n> Username: ").strip()
                            user.unfollow(_u_name=u_name)

                        case "7":
                            post_uid = input("\n> Post ID: ").strip()  # type: ignore
                            user.like_post(uid=post_uid)

                        case "8":
                            post_uid = input("\n> Post ID: ").strip()  # type: ignore
                            user.unlike_post(uid=post_uid)

                        case _:
                            print("\n> Invalid operation! Try again...")

                    print(
                        "\n> Available operations...\n\n"
                        "  1 - Create a new post.\n"
                        "  2 - Show personal feed.\n"
                        "  3 - Show following feed.\n"
                        "  4 - Delete post.\n"
                        "  5 - Follow user.\n"
                        "  6 - Unfollow user.\n"
                        "  7 - Like post.\n"
                        "  8 - Unlike post.\n"
                        "  0 - Exit."
                    )

                    input_02: str = input("\n> Enter an operation: ").strip()
            else:
                print("> Username not found.")

        case _:
            print("\n> Invalid operation! Try again...")

    print(
        "\n> Available operations...\n\n"
        "  1 - Sign up a new user.\n"
        "  2 - Sign in as user.\n"
        "  0 - Exit."
    )

    input_01: str = input("\n> Enter an operation: ").strip()

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton()
s2 = Singleton()

print(s1 is s2) 


# -- extra challenge
class UserSession:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.user_data = None
        return cls._instance

    def set_user(self, user_id, username, name, email):
        self.user_data = {
            "user_id": user_id,
            "username": username,
            "name": name,
            "email": email,
        }

    def get_user_data(self):
        return self.user_data

    def clear_session(self):
        self.user_data = None


session1 = UserSession()
session2 = UserSession()

session1.set_user(1, "qwik", "Qwik Zgheib", "qwikzgheib@gmail.com")

print(session1.get_user_data())
print(session2.get_user_data())

session2.clear_session()

def singleton(cls):
    instances = dict()

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrap


@singleton
class UserSession:
    def __init__(self):
        self.user_data = {}

    def set_user(self, user_id, username, name, email):
        self.user_data[user_id] = {
            'username': username,
            'name': name,
            'email': email
        }

    def get_user(self, user_id):
        if user_id in self.user_data:
            return self.user_data.get(user_id, None)
        return f'ID {user_id} not found'

    def clear_user(self, user_id):
        if user_id in self.user_data:
            del self.user_data[user_id]
            return f'ID {user_id} deleted'
        return f'ID {user_id} not found'


if __name__ == '__main__':
    sessions = UserSession()
    sessions.set_user(
        1,
        'Juan',
        'Juan Perez',
        'juan@juan.com'
    )
    print(sessions.get_user(1))

    sessions.set_user(
        2,
        'Maria',
        'Maria Perez',
        'maria@maria.com'
    )
    print(sessions.get_user(2))

    print(sessions.get_user(3))

    print(sessions.clear_user(1))

    print(sessions.get_user(1))

    sessions2 = UserSession()

    print(sessions is sessions2)

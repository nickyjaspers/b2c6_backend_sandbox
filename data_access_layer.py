import mariadb

from user import User


class DataAccessLayer(object):
    def __init__(self):
        self.connection = mariadb.connect(
            host="localhost",
            port=3306,
            user="root",
            password="password",
            database="mydatabase"
        )

    def get_users(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, username FROM user")
        results = cursor.fetchall()

        users = []
        for user in results:
            users.append(User(user_id=user[0], user_name=user[1]))

        return users

    def get_user(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, username FROM user where id = ?", (user_id,))
        results = cursor.fetchone()
        return User(user_id=results[0], user_name=results[1])

    def create_user(self, user):
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO user (username) VALUES (?)", (user.user_name,))
        except mariadb.Error as e:
            print(f"Error: {e}")

        self.connection.commit()
        print(f"Last Inserted ID: {cursor.lastrowid}")


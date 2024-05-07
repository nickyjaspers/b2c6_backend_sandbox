from data_access_layer import DataAccessLayer
from user import User
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"hello": "world again"}


@app.get("/users")
def get_users():
    data_access_layer = DataAccessLayer()
    return data_access_layer.get_users()


@app.post("/users")
def create_user(user_name: str):
    data_access_layer = DataAccessLayer()
    data_access_layer.create_user(User(user_id=0, user_name=user_name))
    return data_access_layer.get_users()


@app.get("/users/{user_id}")
def get_user(user_id: int):
    data_access_layer = DataAccessLayer()
    return data_access_layer.get_user(user_id)


if __name__ == '__main__':
    print('Hello World!')

    data_access_layer = DataAccessLayer()
    print(data_access_layer.get_users())

from data_access_layer import DataAccessLayer


if __name__ == '__main__':
    print('Hello World!')
    data_access_layer = DataAccessLayer()
    print(data_access_layer.get_users())



    # Example for insert a new user

    # from user import User
    # data_access_layer.create_user(User(user_id=0, user_name='Third User'))
    # print(data_access_layer.get_users())


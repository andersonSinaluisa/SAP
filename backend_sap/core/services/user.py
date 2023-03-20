from django.contrib.auth.models import User


def create_user(user):
    """
        Creates a user with the given username, email and password.

        :param user: The dict with data for the user
        :type user: dict

        :return: The created user
        :rtype: User
    """
    user = User.objects.create_user(**user)
    user.save()
    return user

def update_user(id_user, dict):
    """
        Updates a user with the given id.

        :param id_user: The user's id
        :type id_user: int
        :param dict: The dict with the data to update
        :type dict: dict

        :return: The updated user
        :rtype: User
    """
    user = User.objects.get(id=id_user)
    user.username = dict['username']
    user.email = dict['email']
    user.set_password(dict['password'])
    user.save()
    return user

def list_users():
    """
        Lists all users.

        :return: A list of users
        :rtype: list
    """
    return User.objects.all()

def get_user(username):
    """
        Gets a user with the given username.

        :param username: The user's username
        :type username: str

        :return: The user
        :rtype: User
    """
    return User.objects.get(username=username)

def delete_user(id):
    """
        Deletes a user with the given id.

        :param id: The user's id
        :type id: int
    """
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
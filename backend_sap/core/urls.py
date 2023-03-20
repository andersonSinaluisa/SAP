
from django.conf.urls import url
from core.views.auth import CustomAuthToken, getAllUser, createUser, updateUser, deleteUser, logOut
from django.urls import path



urlpatterns = [
    path('login', CustomAuthToken.as_view(), name="auth_login"),
    path('users/list', getAllUser.as_view(), name="getAllUser"),
    path('users/create', createUser.as_view(), name="createUser"),
    path('users/update/<user_id>', updateUser.as_view(), name="updateUser"),
    path('users/delete/<user_id>', deleteUser.as_view(), name="deleteUser"),
    path('logout', logOut.as_view(), name="logOut"),
]
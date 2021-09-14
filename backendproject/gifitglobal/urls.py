from django.shortcuts import render
from django.conf.urls import url
from . views import UserAPI,getUpdateDeleteUser,SignupAPI,UserSigin

urlpatterns = [
    url(r'^api/users', UserAPI.as_view()),
    url(r'^api/updateuser/(?P<id>[0-9]+)$',getUpdateDeleteUser.as_view()),
    url(r'^api/signup', SignupAPI.as_view()),
    url(r'^api/signin',UserSigin.as_view()),


]

from .base import *
import os

DEBUG = True

DATABASES = {
     'default': {
        'ENGINE': 'djongo',
        'NAME':'giftiglobal',
        'HOST' :  "mongodb://bhanu:bhanu@123@localhost:27017/giftiglobal",
        'USER': "bhanu",
        "PASSWORD": "bhanu@123"
    }
}

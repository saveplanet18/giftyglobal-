from django.shortcuts import render
from .models import Users
from .serializers import UserSerializer
from rest_framework.decorators import api_view,APIView
from django.http import Http404
from rest_framework import status
from django.core import serializers
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
import bcrypt
import datetime
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import IsAuthenticated



class UserAPI(APIView):
    def get(self,request,*args,**kwargs):
        try:
            obj=Users.objects.all()
            serializer=UserSerializer(obj,many=True)
            return Response(serializer.data)
        except Users.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        try:
            obj = request.data
            password = obj["password"]
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password, salt)
            request.data["password"]= hashed
            serializer=UserSerializer(data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"success":True,"data":serializer.data})
            return Response({"message":serializer.errors})


        except Http404:
            return Response({"message":"data not added"})




class getUpdateDeleteUser(APIView):
	def get_object(self,id):
		try:
			return Users.objects.get(id=id)
		except:
			raise Http404
	def get(self, request, id, format=None):
		try:
			get=self.get_object(id)
			serializer=UserSerializer(get)
			return Response(serializer.data)
		except Http404:
			return JsonResponse({"message:":" no records found on this id"})

	def put(self,request,id,format=None):
		try:
			obj=self.get_object(id)
			request.data["updated_at"]=datetime.date.today()
			serializer=UserSerializer(obj,data=request.data,partial=True)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse({"success":True,"data":serializer.data})
			return JsonResponse({"message":serializer.errors})
		except Http404:
			return JsonResponse({"message":"data not updated"})

	def delete(self,request,id,format=None):
		try:
			obj=self.get_object(id)
			obj.delete()
			return Response({"message":"data  deleted"})
		except Http404:
			return JsonResponse({"message":"data not deleted"})




class SignupAPI(APIView):

	def post(self,request,format=None):
			obj = request.data
			email = request.data["email"]
			password = obj["password"]
			salt = bcrypt.gensalt()
			hashed = bcrypt.hashpw(password, salt)

			request.data["password"]= hashed
			serializer=UserSerializer(data=request.data,partial=True)
			if serializer.is_valid():
				serializer.save()
				subject = 'welcome to GFG world'
				message = f'Hi {email}, thank you for registering in geeksforgeeks.'
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [email, ]
				send_mail( subject, message, email_from, recipient_list )
				return Response({"success":True,"data":serializer.data})
			return Response({"message":serializer.errors})


class UserSigin(APIView):
	def post(self,request,format=None):
            obj = request.data
            email = obj["email"]
            password = obj["password"]
            email_check = Users.objects.filter(email=request.data["email"]).first()
            if email_check is not None:
                hashed_password = email_check.password
                print(hashed_password)
                if bcrypt.checkpw(password,hashed_password):
                    return Response ({"success":True,
                        'message': 'logined successfully'
                        })
                else:
                    return Response({"success":False,"message": "Invalid password"})
            else:
                return Response({"success":False,"message": "Invalid UserName"})

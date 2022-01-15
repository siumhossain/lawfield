

from django.db import models
from django.db.models import fields
from django.db.models.base import ModelBase
from rest_framework import serializers
from .models import About, Appointment, Category, File, Law, LawDescription, LawyerCategory, Position, Quiz,User,AppointmentDetails

class RegisterSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ['username','email','password']
       
        def save(self):
            user = User(
                username = self.validate_data['username'],
                email=self.validated_data['email'],
                password = self.validated_data['password']
            )
            user.save()
            return user
# class TreeNodeSerializer(serializers.ModelSerializer):
#     sections = serializers.SerializerMethodField()

#     class Meta:
#         depth = 1
#         model = Law
#         fields = ('act','title','description','omited','sections')

#     def get_sections(self, obj):
#         return TreeNodeSerializer(obj.get_children(), many=True).data

class LawyerSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()

    class Meta:
        model = LawyerCategory
        fields = ('id','name','category','position','area')
    
    def get_id(self,obj):
        return obj.user.id

    def get_name(self,obj):
        return obj.user.username
    def get_category(self,obj):
        return obj.category.name
    def get_position(self,obj):
        return obj.position.name

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id','description']
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id','name']





class FileS(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class SendAppointment(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class LawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = '__all__'

class LawDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawDescription
        fields = ['title','description']


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id','question','option_A','option_B','option_C','option_D']

class QuizAnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id','right_ans']

class AppointmentDetailsSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField("%d-%m-%Y %I:%M %p")
    
    class Meta:
        model = AppointmentDetails
        fields = ['id','lawyer','client','message','file','created']

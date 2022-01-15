import re
from django.shortcuts import render
from .models import About, AppointmentDetails, File, Law, LawDescription, LawyerCategory, Position, Quiz, User,Appointment
from mptt.utils import tree_item_iterator
# Create your views here.
from django.http import JsonResponse, response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AboutSerializer, AppointmentDetailsSerializer, FileS, LawDescriptionSerializer, LawSerializer, PositionSerializer, QuizAnsSerializer, QuizSerializer, SendAppointment, LawyerSerializer,RegisterSerializer
from django.db.models import Q
from rest_framework.authtoken.models import Token
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from django.template.loader import render_to_string 

from core import serializers

@api_view(['GET'])
def law(request):
    if request.method == 'GET':
        obj = Law.objects.all()
        serializers = LawSerializer(obj,many=True)
        if serializers:

            return Response(serializers.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def lawSearch(request):
    if request.method == 'POST':
        value = request.data['value']
        obj = Law.objects.filter(
            Q(act_no__icontains = value) | Q(title__icontains = value) | Q(description__icontains = value)
        ).distinct()
        serializers = LawSerializer(obj,many=True)
        if serializers:

            return Response(serializers.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def lawDescription(request,id):
    if request.method == 'GET':
        obj = LawDescription.objects.filter(act_no__id = id)
        serializers = LawDescriptionSerializer(obj,many=True)
        if serializers:
            return Response(serializers.data,status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors,status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def quiz(request,q):
    if request.method == 'GET':
        if q == '5':
            obj = Quiz.objects.order_by('?')[:5]
            serializers = QuizSerializer(obj,many=True)
            if serializers:
                return Response(serializers.data,status=status.HTTP_200_OK)
            else:
                return Response(serializers.errors,status=status.HTTP_404_NOT_FOUND)
        if q == '10':
            obj = Quiz.objects.order_by('?')[:10]
            serializers = QuizSerializer(obj,many=True)
            if serializers:
                return Response(serializers.data,status=status.HTTP_200_OK)
            else:
                return Response(serializers.errors,status=status.HTTP_404_NOT_FOUND)
        if q == '15':
            obj = Quiz.objects.order_by('?')[:10]
            serializers = QuizSerializer(obj,many=True)
            if serializers:
                return Response(serializers.data,status=status.HTTP_200_OK)
            else:
                return Response(serializers.errors,status=status.HTTP_404_NOT_FOUND)

            
        
@api_view(['GET'])
def quiz_ans_check(request,id):
    obj = Quiz.objects.get(id=id)
    if obj:
        serializers = QuizAnsSerializer(obj)
        return Response(serializers.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# def law_search(request):
#     if request.method == 'POST':
#         act_no = request.data['act']
#         details = request.data['details']
#         if act_no:
#             result = Law.objects.filter(
#                 Q(act__icontains = act_no) | Q(section_number__icontains = act_no)
#             )
#             serializer = TreeNodeSerializer(result,many=True)
#             return Response(serializer.data,status=status.HTTP_200_OK)
        
#         elif details:
#             result = Law.objects.filter(
#                 Q(title__icontains = details) | Q(description__icontains = details)
#             )
#             serializer = TreeNodeSerializer(result,many=True)
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         elif act_no and details:
#             result = Law.objects.filter(
#                 Q(act__icontains = act_no) | Q(section_number__icontains = act_no) | Q(title__icontains = details) | Q(description__icontains = details)
#             ).distinct()
#             serializer = TreeNodeSerializer(result, many=True)
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def lawyer_search_name(request,name):
    if request.method == 'GET':
       
        
        if name:
            result = LawyerCategory.objects.filter(
                user__username__icontains = name
                
                    
                
            ).distinct()
        
        if result:
            serializer = LawyerSerializer(result,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    'message':'Not found'
                }
            )
@api_view(['GET'])
def lawyer_search_category(request,category):
    if request.method == 'GET':
        

        if category:
            result = LawyerCategory.objects.filter(
                category__name__icontains = category
                    
                
            ).distinct()
        
        if result:
            serializer = LawyerSerializer(result,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    'message':'Not found'
                }
            )
@api_view(['GET'])
def lawyer_search_position(request,position):
    if request.method == 'GET':
       
        

        if position:
            result = LawyerCategory.objects.filter(
                position__name__icontains = position
                    
                
            ).distinct()
        
        if result:
            serializer = LawyerSerializer(result,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    'message':'Not found'
                }
            )
@api_view(['GET'])
def lawyer_search_area(request,area):
    if request.method == 'GET':
        
        

        if position:
            result = LawyerCategory.objects.filter(
                area__icontains = area
                    
                
            ).distinct()
        
        if result:
            serializer = LawyerSerializer(result,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    'message':'Not found'
                }
            )


@api_view(['POST'])
def register(request):
   if request.method == 'POST':
      serializer = RegisterSerializer(data=request.data)
      data = {}
      if serializer.is_valid():
         user = serializer.save()
         data['response'] = "success"
         data['email'] = user.email
         token = Token.objects.get(user=user).key
         
         data['token'] = token
      else:
         data = serializer.errors
      return Response(data)
        

@api_view(['GET'])
def about(request):
    if request.method == 'GET':
        obj = About.objects.all()
        serializer = AboutSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def position(request):
    if request.method == 'GET':
        obj = Position.objects.all()
        serializer = PositionSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def all_lawyer(request):
    if request.method == 'GET':
        obj = LawyerCategory.objects.all()
        serializer = LawyerSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



# multiple_file_upload_test
def handle_uploaded_file(f):
        with open(f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
@api_view(['POST'])
def fileup(request):
    if request.method == 'POST':
        
        files = request.FILES.getlist('files')

        for file in files:
            obj = File.objects.create(
                file = file
            )

        return Response('ok',status=status.HTTP_200_OK)

@api_view(['POST'])
def sendAppointment(request):
    if request.method == 'POST':

        serializers = SendAppointment(data=request.data)
        if serializers.is_valid():
            

            serializers.save()
            fromUser = serializers.validated_data['fromUser']
            toUser = serializers.validated_data['toUser']
            message = serializers.validated_data['message']
            file = serializers.validated_data['file']

            
            
            user = User.objects.get(id=fromUser)
            lawyer = User.objects.get(id=toUser)

            AppointmentDetails.objects.create(
                lawyer = lawyer,
                client = toUser,
                message = message,
                file = file
            )
            
            subject, from_email, to = 'Appointment information', settings.EMAIL_HOST_USER, lawyer.email
            html = './appointment.html'
            html_msg = render_to_string(html,{
                'fromUser':user.username,
                'userEmail':user.email,
                
                'message':message
            })
            msg = EmailMultiAlternatives(subject,html_msg,from_email, [to])
            msg.content_subtype = 'html'
            
            msg.attach_file(f'./media/{file}')
            msg.send()
            return Response(serializers.data,status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def lawyer_check(request):
    group_check = request.user.groups.filter(name='Lawyer').exists()
    if not request.user.is_staff or not group_check:
      
      return JsonResponse({
            'msg':'false'
        })
    else:
        return JsonResponse({
            'msg':'true'
        })

@api_view(['GET'])
def appointmentDetails(request,id):
    obj = AppointmentDetails.objects.filter(lawyer__id = id)
    if obj:
        serializers = AppointmentDetailsSerializer(obj,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
        
@api_view(['GET'])
def appointmentInDetails(request,id):
    obj = AppointmentDetails.objects.get(id=id)   
    if obj:
        serializers = AppointmentDetailsSerializer(obj)
        return Response(serializers.data,status=status.HTTP_200_OK)

            
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# @receiver(post_save, sender=Appointment)
# def post_user_created_signal(sender,instance,created,**kwargs):
#     if created:
#         print('hello user created')


  
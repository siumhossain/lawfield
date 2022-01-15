from django.urls import path
from .import views
urlpatterns = [
    path('law/', views.law),
    path('lawSearch/', views.lawSearch),
    path('lawDescription/<str:id>/', views.lawDescription),
    
    # path('lawSearch/', views.law_search),
    
    path('about/',views.about),
    path('position/',views.position),
    path('all-lawyer/',views.all_lawyer),
    path('lawyer_name/<str:name>/',views.lawyer_search_name),
    path('lawyer_category/<str:category>/',views.lawyer_search_category),
    path('lawyer_position/<str:position>/',views.lawyer_search_position),
    path('lawyer_area/<str:area>/',views.lawyer_search_area),
    path('file/',views.fileup),
    path('sendAppointment/',views.sendAppointment),
    path('appointmentDetails/<str:id>/',views.appointmentDetails),
    path('appointmentInDetails/<str:id>/',views.appointmentInDetails),



    path('quiz/<str:q>/',views.quiz),
    path('quiz/ans/<str:id>/',views.quiz_ans_check),

    path('lawyer_check/',views.lawyer_check)

]
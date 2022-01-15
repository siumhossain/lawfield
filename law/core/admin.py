from django.contrib import admin
from .models import About, Appointment, AppointmentDetails, Category, File, Law, LawDescription, LawyerCategory, Position, Quiz, User
from mptt.admin import MPTTModelAdmin

# Register your models here.

# admin.site.register(Law,MPTTModelAdmin)
admin.site.register(Category)
admin.site.register(LawyerCategory)
admin.site.register(User)
admin.site.register(About)
admin.site.register(Position)
admin.site.register(File)
admin.site.register(Appointment)
admin.site.register(Law)
admin.site.register(LawDescription)
admin.site.register(Quiz)
admin.site.register(AppointmentDetails)











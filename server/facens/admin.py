from django.contrib import admin
from facens.models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
	list_display = ("created_at", "user", "ra")
	#list_filter  = (,)

class TeacherAdmin(admin.ModelAdmin):
	list_display = ("created_at", "user", "cpf")
	#list_filter  = (,)

class CourseAdmin(admin.ModelAdmin):
	list_display = ("created_at", "name")
	#list_filter  = (,)

class RegionAdmin(admin.ModelAdmin):
	list_display = ("created_at", "name")
	#list_filter  = (,)

class ClassLocationAdmin(admin.ModelAdmin):
	list_display = ("created_at", "region", "name")
	list_filter  = ("region",)

class ClassAdmin(admin.ModelAdmin):
	list_display = ("created_at", "name", "teacher", "course", "location", "weekday", "time", "duration",)
	list_filter  = ("teacher", "course", "location", "weekday",)
	readonly_fields = ("duration",)

class NotificationAdmin(admin.ModelAdmin):
	list_display = ("created_at", "title", "teacher", "course", "date")
	list_filter  = ("teacher", "course")

class StudentInscritionAdmin(admin.ModelAdmin):
	list_display = ("created_at", "student", "course")
	list_filter  = ("course",)

admin.site.register(Student           , StudentAdmin)
admin.site.register(Teacher           , TeacherAdmin)
admin.site.register(Course            , CourseAdmin)
admin.site.register(Region            , RegionAdmin)
admin.site.register(ClassLocation     , ClassLocationAdmin)
admin.site.register(Class             , ClassAdmin)
admin.site.register(Notification      , NotificationAdmin)
admin.site.register(StudentInscrition , StudentInscritionAdmin)
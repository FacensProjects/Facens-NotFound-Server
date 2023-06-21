from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
from facens.models import *

from datetime import datetime
import json

# Create your views here.

def search_ra(ra):
	try:
		student = Student.objects.get(ra=ra)
		course = StudentInscrition.objects.filter(student=student).last().course

		current_time = datetime.now().time()
		weekday = datetime.now().isoweekday()
		result = Class.objects.filter(course=course,weekday=str(weekday))
		
		current_class = None

		for class_instance in result:
			class_start_time = class_instance.get_start()
			class_end_time = class_instance.get_end()

			if current_time >= class_start_time and current_time <= class_end_time:
				current_class = class_instance
				break
			elif current_time < class_start_time:
				current_class = class_instance
				break

		context = {
				"status": True,
				"student": {
					"name" : student.user.first_name,
					"ra"   : student.ra,
				}
			}

		if (current_class):
			context['class'] = {
						"status"   : True,
						"location" : current_class.location.region.name,
						"class"    : current_class.location.name,
						"name"     : current_class.name,
						"course"   : course.name,
						"course"   : current_class.name,
						"teacher"  : current_class.teacher.user.first_name,
						"start"    : current_class.get_start(),
						"end"      : current_class.get_end(),
					}
		else:
			context['class'] = {"status": False}

		notification = []
		current_datetime = timezone.now()
		query1 = Notification.objects.filter(course__isnull=True,date=current_datetime.date())
		query2 = Notification.objects.filter(course=course,date=current_datetime.date())
		result = query1.union(query2)
		for notf in result:
			notification.append({
					"teacher"     : notf.teacher.user.first_name,
					"title"       : notf.title,
					"description" : notf.description,
					})

		context['notification'] = notification

	except:
		context = {
				"status": False,
				"description": "Ocorreu algum erro"
		}
	return context

@csrf_exempt
def api_search(request):
    if request.method == "POST":
        data = json.loads(request.body)
        ra = data.get("ra")
        context = search_ra(ra)

        return JsonResponse(context)
    else:
        context = {
            "status": False,
            "description": "Acesso restrito."
        }
        return JsonResponse(context)


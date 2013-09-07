from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render

from scores import Database
from courseAdvisor.models import Course

@csrf_exempt
def course_search(request):
	if not request.is_ajax():
		print 'not ajax'
		return
	coursecode = request.POST['coursecode']
	db = Database()
	courses = db.determine_searched_course(coursecode)
	for course in courses:
		print course
        return HttpResponse('success')

def index(request):
	return render(request, 'courseAdvisor/index.html')

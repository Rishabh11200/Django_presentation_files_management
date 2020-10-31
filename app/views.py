from django.shortcuts import render,redirect
from app.models import *
from .forms import *

def home(request):
	return render(request,"home.html")

def Index(request):
	return render(request,"index.html")

def register(request):
	form  = formuser()
	if request.method == 'POST':
		form = formuser(request.POST)
		form.save()
		return redirect('/login/')
	else:
		form = formuser()
	return render(request,"register.html",{"form":form})

def login(request):
	enroll = request.POST.get('enroll')
	passw = request.POST.get('password1')
	if enroll:
		var = usermodel.objects.filter(enrollment__icontains = enroll)
		for data in var:
			if data.password == passw:
				subject = subjectmodel.objects.filter(semester = data.semester).filter(coursename  = data.course)
				sem_variable  = str(data.semester)
				course_variable = str(data.course)
				enrollment = str(data.enrollment)
				request.session['sem'] = sem_variable
				request.session['co'] = course_variable
				request.session['enrollment'] = enrollment
				#return redirect('/main/')
				return render(request,'index.html')
	return render(request,"login.html")

def profile(request): 	 	
	if request.session.has_key('enrollment'):
		var = request.session.get('enrollment')
		student = usermodel.objects.filter(enrollment = var)
		return render(request,"profile.html",{"var":student})
		
	else:
		return redirect('/login/')

def cecform(request):
	if 'enrollment' in request.session: 
		form=formcec(request)
		if request.method == 'POST':
			form=formcec(request,request.POST)
			if form.is_valid():
				form.save()
				return redirect('/displayteam/')
			else:
				form = formcec(request)	
		return render(request,'cec.html',{'form1':form})
	else:
		return redirect('/login/')
def upload(request):
	teamno = request.GET.get('id')
	x = teammodel.objects.get(team_no=teamno)
	form1 = formaddfile(instance=x)
	if request.method == 'POST':
		form1 = formaddfile(request.POST,request.FILES,instance = x)
		if form1.is_valid():
			form1.save()
			return redirect('/displayteam/')
		else:
			form1 = formaddfile()
	return render(request,"upload.html",{'form':form1})

def displayteam(request):
	sessionvar = request.session.get('enrollment')
	var = teammodel.objects.filter(student__enrollment = sessionvar)
	return render(request,"displayteam.html",{'var':var})



def main(request):
	return render(request,"main.html")

def logout(request):
	del request.session['sem']
	del request.session['co']
	del request.session['enrollment']
	return redirect('/login/')

def contact(request):
	return render(request,'contact.html')
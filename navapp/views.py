from django.shortcuts import render,redirect
from django.http import HttpResponse
from navapp.models import Usrg
from navapp.forms import Usrf

# Create your views here.
def nav(req):
	return HttpResponse("<style>h1{text-align:center;background-color:aqua;}</style><h1>Welcome to home page</h1><h2 style='color:black;background-color:Gold;'>Naveen</h2>")
def ch(req):
	return HttpResponse("<script>alert('click ok to display MSG')</script><h2>welcome</h2>")
def home(req):
	return render(req,'navtemp/home.html')

def lg(req):
	return render(req,'navtemp/login.html')
def reg(req):
	""" if req.method=="POST":
		emailaddress=req.POST['a'];
		pas=req.POST['b'];
		age=req.POST['ag'];
		return render(req,'navtemp/home.html',{'info':emailaddress,'info1':pas,'info2':age})"""
	return render(req,'navtemp/register.html')
def bthm(req):
	return render(req,'navtemp/bthm.html')
def about(req):
	return render(req,'navtemp/about.html')
def contact(req):
	return render(req,'navtemp/contact.html')
def rf(req):
	return render(req,'navtemp/reg.html')
def rega(req):
	if req.method=="POST":
		fn=req.POST['fname'];
		ln=req.POST['lname'];
		age=req.POST['age'];
		mail=req.POST['email'];
		pas=req.POST['pwd'];
		pas1=req.POST['pwd1'];
		d={'info':fn,'info1':ln,'info2':age,'info3':mail}
		return render(req,'navtemp/regadetails.html',{'d':d})
	    
		
	return render(req,'navtemp/rega.html')
def action(rq):
	if rq.method == "POST":
		un=rq.POST['usrnam']
		p=rq.POST['pswd']
		e=rq.POST['email']
		ph=rq.POST['phon']
		data2=Usrg.objects.all()
		if len(un)!=0:
			data=Usrg.objects.create(username=un,password=p,email=e,ag=ph)
		return render(rq,'navtemp/action.html',{'info':data2})
    
	data2=Usrg.objects.all()
	return render(rq,'navtemp/action.html',{'info':data2})

def dlt(rq,id):
	data=Usrg.objects.get(id=id)
	data.delete()
	return redirect('/at')

def dform(rq):
	if rq.method=="POST":
		e=Usrf(rq.POST)
		if e.is_valid():
			e.save()
			data2=Usrg.objects.all()
			return render(rq,'navtemp/dyform1.html',{'info':data2})
	

 
			#return HttpResponse("User created Successfully")
		 	
	e=Usrf()
	return render(rq,'navtemp/dyform.html',{'tu':e})
	
    

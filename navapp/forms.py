from navapp.models import Usrg
from django import forms
class Usrf(forms.ModelForm):
	class Meta:
		model=Usrg;
		fields=['username','email','password']

		widgets={
		"username":forms.TextInput(attrs={"class":"form-control ","placeholder":"Enter username", "required":True}),
		"email":forms.EmailInput(attrs={"class":"form-control ","placeholder":"Enter email", "required":True}),
		"password":forms.PasswordInput(attrs={"class":"form-control ","placeholder":"Enter Password", "required":True})
		}
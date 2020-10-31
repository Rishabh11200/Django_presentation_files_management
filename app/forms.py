from .models import *
from django import forms


class formuser(forms.ModelForm):
	class Meta:
		model = usermodel
		fields = "__all__"


class formcec(forms.ModelForm):

	class Meta:
		model=teammodel
		fields=['team_no','student','subject','team_name']

	def __init__(self, request, *args, **kwargs):
		var = request.session.get('sem')
		var1 = request.session.get('co')
		super(formcec, self).__init__(*args, **kwargs)
		if self.instance:
			self.fields['subject'].queryset = subjectmodel.objects.filter(semester__sem = var).filter(coursename__coursename=var1)
			self.fields['student'].queryset = usermodel.objects.filter(semester__sem = var).filter(course__coursename = var1)

class formaddfile(forms.ModelForm):
	 file = forms.FileField(label='Select a file',widget=forms.FileInput(attrs={'accept':'application/pdf','class':'form-control-file','aria-describedby':'inputGroupFileAddon01'}))
	 class Meta:
	 	model=teammodel
	 	fields= ['topic_name','file']
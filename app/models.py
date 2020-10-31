from django.db import models


class coursemodel(models.Model):
	coursename=models.CharField(max_length=50)
	def __str__(self):
		return self.coursename


class semestermodel(models.Model):
	sem = models.CharField(max_length = 20)
	def __str__(self):
		return self.sem

class subjectmodel(models.Model):
	semester = models.ForeignKey(semestermodel,on_delete=models.CASCADE)
	subjectname= models.CharField(max_length=50)
	coursename= models.ForeignKey(coursemodel,on_delete=models.CASCADE)
	def __str__(self):
		return self.subjectname
			
class usermodel(models.Model):
	name = models.CharField(max_length = 50)
	enrollment  = models.IntegerField()
	semester = models.ForeignKey(semestermodel,on_delete=models.CASCADE)
	email  = models.EmailField(max_length = 200)
	password = models.CharField(max_length = 50)
	mobile = models.CharField(max_length=12)
	batch = models.CharField(max_length = 10)
	course  =   models.ForeignKey(coursemodel,on_delete=models.CASCADE)
	class Meta:
		ordering = ['enrollment']
	def __str__(self):
		return str(self.name)

class teammodel(models.Model):
	team_no = models.AutoField(primary_key=True)
	student = models.ManyToManyField(usermodel)
	subject = models.ForeignKey(subjectmodel,on_delete=models.CASCADE)
	team_name  = models.CharField(max_length = 100)
	topic_name  = models.CharField(max_length = 100,blank=True,null=True)
	file = models.FileField(upload_to='',blank=True,null=True)

	def __str__(self):
		return str(self.team_no)

	def delete(self, *args, **kwargs):
		self.file.delete()
		super().delete(*args, **kwargs)


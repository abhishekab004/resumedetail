from django.contrib import admin
from myapp.models import Resume

# Register your models here.
class ResumeAdmin(admin.ModelAdmin):
    list_display=['id','name','dob','gender','locality','city','pin','state','mobile','job_city','profile_image','my_file']

admin.site.register(Resume,ResumeAdmin)

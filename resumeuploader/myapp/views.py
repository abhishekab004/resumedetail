from django.shortcuts import render,redirect
from myapp.forms import ResumeForm
from myapp.models import Resume
from django.views import View

# Create your views here.
class Home_view(View):
    def get(self,request):
        form=ResumeForm()
        candidates=Resume.objects.all()
        return render(request,'myapp/home.html',{'form':form,'candidates':candidates})
    
    def post(self,request):
        form=ResumeForm()
        if request.method=="POST":
            form=ResumeForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
            return redirect("/")
        form=ResumeForm()
        return render(request,'myapp/home.html',{'form':form})    

class Candidate_view(View):
    def get(self,request,id):
        candidate=Resume.objects.get(id=id)
        return render(request,'myapp/candidate.html',{'candidate':candidate})
from django.shortcuts import render

# Create your views here.
from .models import Project, Qualification,Testimonial,ContactMessage
from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):   
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form is valid and data saved!")
          
            return redirect('index')  # Redirect to the same page after successful submission
        else:
            print("Form is not valid:", form.errors)
    else:
        form = ContactForm()
        
    projects = Project.objects.all()
    qualifications = Qualification.objects.all()
    testimonials= Testimonial.objects.all()
   
    context = {
        'projects': projects,
        'qualifications': qualifications,
        'testimonials': testimonials,
        'form': form,
    }

    return render(request, 'index.html', context)

def project(request):   
    #     for item in items:
                
    # projects = Project.objects.all()
    # qualifications= Qualification.objects.all()
    


    # context = {
    #     'project' : project,
    #     'qualifications' : qualifications,
        
    # }

    # return render(request, 'index.html', context)
    return render(request, 'index.html')


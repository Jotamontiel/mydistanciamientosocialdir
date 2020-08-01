from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
from courses.models import Course, Category
import random

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    courses = Course.objects.all()
    categories = Category.objects.all()

    # Others Courses [Begin]
    if len(courses) < 3:
        saved_courses = []
        saved_courses = courses
    else:
        # Random Courses [Begin]
        saved_numbers = []
        saved_numbers = random.sample(range(0,len(courses)), 3)
        saved_courses = []
        for number in saved_numbers:
            saved_courses.append(courses[number])
        # Random Courses [Finish]
    # Others Courses [Finish]

    if request.method == "POST":
        contact_form  = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "SOCIAL DISTANCE: Nuevo mensaje de contacto",
                "De {} <{}>\n\nTeléfono: {}\n\nEscribió: {}".format(name, email, phone, content),
                "distanciamientosocial@gmail.com",
                ["jorgemontielmontiel@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha salido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form':contact_form, 'course_list':courses, 'category_list':categories, 'saved_courses':saved_courses})
    



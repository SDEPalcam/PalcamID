from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Student
from django.core.mail import send_mail
from .models import StudentCard

def create_digital_card(request):
    if request.method == 'POST':
        student = request.user
        StudentCard.objects.create(student=student)
        return HttpResponseRedirect('/dashboard')

def request_physical_card(request):
    if request.method == 'POST':
        student = request.user
        card = StudentCard.objects.get(student=student)
        card.is_physical_card_requested = True
        card.save()
        send_mail(
            'Solicitud de Tarjeta Física',
            f'El estudiante {student.name} ha solicitado una tarjeta física.',
            'noreply@example.com',
            ['admin@example.com'],
            fail_silently=False,
        )
        return HttpResponseRedirect('/dashboard')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        student_number = request.POST['student_number']
        student = Student.objects.create(name=name, email=email, student_number=student_number)
        student.set_password(password)
        student.save()
        return HttpResponseRedirect('/login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        student = authenticate(request, email=email, password=password)
        if student is not None:
            login(request, student)
            return HttpResponseRedirect('/dashboard')
        else:
            return HttpResponseRedirect('/login')
    return render(request, 'login.html')

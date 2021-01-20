from django.shortcuts import render
from .models import Register, Contact, Tap_model


def index(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        pass_out = request.POST['pass_out']
        stream = request.POST['stream']

        register = Register(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            pass_out=pass_out,
            stream=stream, )
        register.save()
    return render(request, 'main/index.html', )


# def who(request):
#     return render(request, 'main/who.html', )


def Digital_Marketing(request):
    return render(request, 'main/Digital-Marketing.html', )
def Courses(request):
    return render(request, 'main/Courses.html', )

def Digital_Market(request):
    return render(request, 'main/Digital_Market.html', )
def CV_Building(request):
    return render(request, 'main/CV-Building.html', )
def Mock_Interviews(request):
    return render(request, 'main/Mock-Interviews.html', )
def Profile_Preparation(request):
    return render(request, 'main/Profile-Preparation.html', )

def Crash_Course(request):
    return render(request, 'main/Crash-Course.html', )
def Data_science(request):
    return render(request, 'main/Data-science.html', )
def Aptitude_Reasoning(request):
    return render(request, 'main/Aptitude-Reasoning.html', )

def full_stack(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        pass_out = request.POST['pass_out']
        stream = request.POST['stream']
        City = request.POST['City']
        Comment = request.POST['Comment']
        register = Register(
            first_name=first_name, last_name=last_name, email=email, phone=phone,
            pass_out=pass_out, stream=stream, City=City, Comment=Comment, )
        register.save()
    return render(request, 'main/full-stack.html', )


def about(request):
    return render(request, 'main/about.html', )
def Training(request):
    return render(request, 'main/Training.html', )

def full_stack_developers(request):
    return render(request, 'main/full-stack-Developers.html', )


def clients(request):
    return render(request, 'main/clients.html', )


# def services(request):
#     return render(request, 'main/services.html', )


def ongoing(request):
    Tap_models = Tap_model.objects.all()
    data = {'Tap_models': Tap_models, }
    return render(request, 'main/ongoing.html', data)


def clients(request):
    return render(request, 'main/clients.html', )


def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']

        message = request.POST['message']

        contact = Contact(
            full_name=full_name,
            email=email,
            phone=phone,

            message=message,
        )
        contact.save()
    return render(request, 'main/contact.html', )


# def more(request):
#     return render(request, 'main/more.html', )


def Recruitments(request):
    return render(request, 'main/Recruitments.html', )


def software_deve(request):
    return render(request, 'main/software-deve.html', )


def tap(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        pass_out = request.POST['pass_out']
        stream = request.POST['stream']
        City = request.POST['City']
        Comment = request.POST['Comment']
        register = Register(
            first_name=first_name, last_name=last_name, email=email, phone=phone,
            pass_out=pass_out, stream=stream, City=City, Comment=Comment, )
        register.save()

    return render(request, 'main/TAP.html', )


def training(request):
    return render(request, 'main/Training.html', )

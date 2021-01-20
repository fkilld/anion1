from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('who', views.who, name='who'),
    # path('services', views.services, name='services'),
    path('ongoing', views.ongoing, name='ongoing'),
    path('Training', views.Training, name='Training'),
    path('full_stack_developers', views.full_stack_developers, name='full_stack_developers'),
    path('clients', views.clients, name='clients'),
    path('contact', views.contact, name='contact'),
    path('Crash_Course', views.Crash_Course, name='Crash_Course'),
    path('Data_science', views.Data_science, name='Data_science'),
    path('Aptitude_Reasoning', views.Aptitude_Reasoning, name='Aptitude_Reasoning'),
    path('Courses', views.Courses, name='Courses'),
    path('Profile_Preparation', views.Profile_Preparation, name='Profile_Preparation'),
    path('CV_Building', views.CV_Building, name='CV_Building'),
    path('Mock_Interviews', views.Mock_Interviews, name='Mock_Interviews'),
    path('Digital_Market', views.Digital_Market, name='Digital_Market'),
    # path('more', views.more, name='more'),
    path('about', views.about, name='about'),

    path('Digital_Marketing', views.Digital_Marketing, name='Digital_Marketing'),
    path('full_stack', views.full_stack, name='full_stack'),
    path('Recruitments', views.Recruitments, name='Recruitments'),
    path('software_deve', views.software_deve, name='software_deve'),
    path('tap', views.tap, name='tap'),
    path('training', views.training, name='training'),
]

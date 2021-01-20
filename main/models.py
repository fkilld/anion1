from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Register(models.Model):
    EDUCATIONS = (
        ('BSc', 'BSc'),
        ('MBA', 'MBA'),
        ('BE / Btech IT', 'BE / Btech IT'),
        ('BE / Btech Computer', 'BE / Btech Computer'),
        ('BE / Btech Mechanical', 'BE / Btech Mechanical'),
        ('BE / Btech Civil', 'BE / Btech Civil'),
        ('MSC', 'MSC'),
        ('BE / Btech Electrical', 'BE / Btech Electrical'),
        ('BCom', 'BCom'),
        ('BE / Btech Electronics', 'BE / Btech Electronics'),
        ('MCA', 'MCA'),
        ('BCA', 'BCA'),
        ('Others', 'Others'),
        ('Career Counselling', 'Career Counselling'),
    )

    first_name = models.CharField(max_length=200, blank=False, default=None)
    last_name = models.CharField(max_length=200, blank=False, default=None)
    email = models.EmailField(max_length=200, blank=False, default=None)
    phone = models.CharField(max_length=200, blank=False, default=None)
    pass_out = models.CharField(max_length=200, blank=False, default=None)
    stream = models.CharField(max_length=100, choices=EDUCATIONS, default=None)
    City = models.CharField(max_length=200, blank=False, default=None)
    Comment = models.CharField(max_length=200, blank=False, default=None)
    date_joined = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    full_name = models.CharField(max_length=200, blank=False, default=None)
    email = models.EmailField(max_length=200, blank=False, default=None)
    phone = models.CharField(max_length=50, blank=False, default=None)
    # subject = models.CharField(max_length=500, blank=False, default=None)
    message = models.CharField(max_length=1000, blank=False, default=None)
    date_of_contact = models.DateTimeField(auto_now_add=True)


class Tap_model(models.Model):
    # Fresh_or_Experience = (
    #     ('fresh', 'fresh'),
    #     ('experience', 'experience'),
    #
    # )
    # EDUCATIONS = (
    #     ('BSc', 'BSc'),
    #     ('MBA', 'MBA'),
    #     ('BE / Btech IT', 'BE / Btech IT'),
    #     ('BE / Btech Computer', 'BE / Btech Computer'),
    #     ('BE / Btech Mechanical', 'BE / Btech Mechanical'),
    #     ('BE / Btech Civil', 'BE / Btech Civil'),
    #     ('MSC', 'MSC'),
    #     ('BE / Btech Electrical', 'BE / Btech Electrical'),
    #     ('BCom', 'BCom'),
    #     ('BE / Btech Electronics', 'BE / Btech Electronics'),
    #     ('MCA', 'MCA'),
    #     ('BCA', 'BCA'),
    #     ('Others', 'Others'),
    #     ('Career Counselling', 'Career Counselling'),
    #
    # )
    job_title = models.CharField(max_length=500, blank=False, default=None)
    job_description = RichTextField(blank=False, default=None)

    # department = models.CharField(max_length=2000, blank=False, default=None)
    # salary = models.CharField(max_length=500, blank=True, )
    # location = models.CharField(max_length=500, blank=True, )
    # requirement = models.CharField(max_length=500, blank=True, )
    # fresh_or_experience = models.CharField(max_length=50, choices=Fresh_or_Experience)
    # educations = models.CharField(max_length=50, choices=EDUCATIONS)

    class Meta:
        ordering = ('-id',)

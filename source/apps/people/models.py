from django.db import models
FEMALE = 0
MALE = 1
OTHERS = 2

GENDERS = (
    ('Female', FEMALE),
    ('Male', MALE),
    ('Others', OTHERS),
)

class Student(models.Model):  
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    gender = models.CharField(choices=GENDERS, max_length=6)
    biography = models.CharField(max_length=500)
    # photo = models.ImageField(upload_to='profile_photo', blank=True, null=True)
    languages = models.CharField(max_length=200, blank=True, null=True,)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    is_unit_student = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    created_at = models.DateField('Create At', auto_now_add=True)
    updated_at = models.DateTimeField('Update At', auto_now=True)

    def __str__(self):
        return self.name
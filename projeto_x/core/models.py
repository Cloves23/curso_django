from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Person(BaseModel):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30)
    document = models.CharField(max_length=16)
    phone = models.CharField(max_length=16)
    email = models.EmailField()


class LegalPerson(Person):
    person = models.OneToOneField('core.Person', on_delete=models.CASCADE, parent_link=True)
    state_registration = models.CharField(max_length=18)
    municipal_registration = models.CharField(max_length=18)

    def __str__(self):
        return f'{self.document} - {self.name}'


class NaturalPerson(Person):
    GENDER = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

    person = models.OneToOneField('core.Person', on_delete=models.CASCADE, parent_link=True)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER)
    nationality = models.CharField(max_length=40)
    naturalness = models.CharField(max_length=30)

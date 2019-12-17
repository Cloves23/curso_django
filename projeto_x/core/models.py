from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        abstract = True


class Person(BaseModel):
    name = models.CharField(_('name'), max_length=50)
    nickname = models.CharField(_('nickname'), max_length=30)
    document = models.CharField(_('document'), max_length=16)
    phone = models.CharField(_('phone'), max_length=16)
    email = models.EmailField(_('email'))

    @property  # "Converte" um método em um atributo
    def is_legalperson(self):
        return hasattr(self, 'legalperson')

    @property
    def is_naturalperson(self):
        return hasattr(self, 'naturalperson')


class LegalPerson(Person):
    person = models.OneToOneField('core.Person',
                                  on_delete=models.CASCADE,
                                  parent_link=True,
                                  verbose_name=_('person'))
    state_registration = models.CharField(_('state registration'), max_length=18)
    municipal_registration = models.CharField(_('municipal registration'), max_length=18)

    def __str__(self):
        return f'{self.document} - {self.name}'


class NaturalPerson(Person):
    GENDER = [('M', _('Male')), ('F', _('Female')), ('O', _('Other'))]

    person = models.OneToOneField(Person,
                                  on_delete=models.CASCADE,
                                  parent_link=True,
                                  verbose_name=_('person'))
    birthday = models.DateField(_('birthday'))
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER)
    nationality = models.CharField(_('nationality'), max_length=40)
    naturalness = models.CharField(_('naturalness'), max_length=30)


class Address(BaseModel):
    person = models.ForeignKey(Person,
                               on_delete=models.CASCADE,
                               related_name='addresses',
                               related_query_name='address',
                               verbose_name=_('person'))
    street = models.CharField(_('street'), max_length=30)
    neighbourhood = models.CharField(_('neighbourhood'), max_length=30)
    city = models.CharField(_('city'), max_length=30)
    number = models.CharField(_('number'), max_length=5)
    complement = models.CharField(_('complement'), max_length=30)
    tags = models.ManyToManyField('Tag',
                                  related_name='addresses',
                                  related_query_name='address',
                                  blank=True,
                                  verbose_name=_('tags'))


class Tag(BaseModel):
    name = models.CharField(_('name'), max_length=30, unique=True)

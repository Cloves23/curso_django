from django import forms

from projeto_x.core.models import NaturalPerson


class UserFormMixin(forms.ModelForm):
    FIELDS = ['created_by', 'created_at', 'updated_at']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._user = user

    def save(self, commit=True):
        if not self.instance.pk:
            self.instance.created_by = self._user
        return super().save(commit)


class NaturalPersonForm(UserFormMixin):
    class Meta:
        model = NaturalPerson
        exclude = UserFormMixin.FIELDS
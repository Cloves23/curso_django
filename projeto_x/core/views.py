from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin

from projeto_x.core.models import NaturalPerson
from projeto_x.core.forms import NaturalPersonForm


class IndexView(TemplateView):
    template_name = 'index.html'


class UserViewMixin(FormMixin):
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs



class NaturalPersonCreateView(UserViewMixin, LoginRequiredMixin, CreateView):
    model = NaturalPerson
    template_name = 'core/naturalperson_create.html'
    form_class = NaturalPersonForm

    def get_success_url(self):
        return reverse('core:np', kwargs={'pk': self.object.pk})


class NaturalPersonDetailView(DetailView):
    model = NaturalPerson
    template_name = 'core/naturalperson.html'
    context_object_name = 'person'

    def get_context_data(self, **kwargs):
        kwargs['algo'] = 'Algum valor'
        return super().get_context_data(**kwargs)


class NaturalPersonListView(LoginRequiredMixin, ListView):
    model = NaturalPerson
    # queryset = NaturalPerson.objects.exclude(gender='M')  # Nega o filtro
    # queryset = NaturalPerson.objects.none()  # Sempre retorna uma queryset vazia
    template_name = 'core/naturalperson_list.html'
    context_object_name = 'people'

    def get_queryset(self):
        return super().get_queryset().exclude(gender='M')

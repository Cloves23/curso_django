from django.views.generic import TemplateView, CreateView, DetailView
from django.urls import reverse_lazy

from projeto_x.core.models import NaturalPerson


class IndexView(TemplateView):
    template_name = 'index.html'


class NaturalPersonDetailView(DetailView):
    model = NaturalPerson
    template_name = 'core/naturalperson.html'

    def get_context_data(self, **kwargs):
        kwargs['algo'] = 'teste'
        return super().get_context_data(**kwargs)


class NaturalPersonCreateView(CreateView):
    model = NaturalPerson
    template_name = 'core/naturalperson_create.html'
    fields = '__all__'
    success_url = reverse_lazy('core:np')

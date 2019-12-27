from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView

from projeto_x.core.models import NaturalPerson


class IndexView(TemplateView):
    template_name = 'index.html'


class NaturalPersonDetailView(DetailView):
    model = NaturalPerson
    template_name = 'core/naturalperson.html'

    def get_context_data(self, **kwargs):
        kwargs['algo'] = 'Algum valor'
        return super().get_context_data(**kwargs)


class NaturalPersonCreateView(CreateView):
    model = NaturalPerson
    template_name = 'core/naturalperson_create.html'
    fields = '__all__'
    # success_url = reverse_lazy('core:np')
    # slug_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse('core:np', kwargs={'pk': self.object.pk})

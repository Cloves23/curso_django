from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from projeto_x.core import views

app_name = 'core'
urlpatterns = [
    path('accounts/login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    path('person/natural/', views.NaturalPersonListView.as_view(), name='np_list'),
    path('person/natural/create/', views.NaturalPersonCreateView.as_view(), name='np_create'),
    path('person/natural/<int:pk>/', views.NaturalPersonDetailView.as_view(), name='np'),
]

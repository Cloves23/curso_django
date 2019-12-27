from django.urls import path

from projeto_x.core import views

app_name='core'
urlpatterns = [
    path('person/natural/<int:id>/', views.NaturalPersonDetailView.as_view(), name='np'),
    path('person/natural/create/', views.NaturalPersonCreateView.as_view(), name='np_create')
]

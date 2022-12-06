from django.urls import path
from . import views

app_name = 'parser'

urlpatterns = [
    path('parser_film/', views.ParserFormView.as_view(), name='parser_func'),
    path('parser_film_info/', views.ParserView.as_view(), name='parser_view'),
]
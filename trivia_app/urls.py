# trivia_app/urls.py
from django.urls import path
from . import views

app_name = 'trivia_app'

urlpatterns = [
    path('trivia/', views.home, name='home'),
    path('trivia/categories/', views.categories, name='categories'),
    path('trivia/category/<int:category_id>/<int:question_index>/', views.question_page, name='question_page'),
    path('trivia/category/<int:category_id>/results/', views.results, name='results'),
    path('trivia/category/<int:category_id>/<int:question_index>/save/', views.save_answer, name='save_answer'),
    path('metrics/', views.metrics_view, name='metrics'),
]
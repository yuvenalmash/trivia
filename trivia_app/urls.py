# trivia_app/urls.py
from django.urls import path
from . import views

app_name = 'trivia_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('category/<int:category_id>/<int:question_index>/', views.question_page, name='question_page'),
    path('category/<int:category_id>/results/', views.results, name='results'),
    path('category/<int:category_id>/<int:question_index>/save/', views.save_answer, name='save_answer'),
]
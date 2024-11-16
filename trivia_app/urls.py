from django.urls import path
from .views import home, category_list, question_list, question_detail, submit_answer

urlpatterns = [
    path('', home, name='home'),
    path('categories/', category_list, name='category_list'),
    path('category/<int:category_id>/', question_list, name='question_list'),
    path('question/<int:question_id>/', question_detail, name='question_detail'),
    path('question/<int:question_id>/submit/', submit_answer, name='submit_answer'),
]
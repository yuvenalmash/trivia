# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Question, Answer
import random

def home(request):
    return render(request, 'trivia_app/home.html')

def categories(request):
    categories = Category.objects.all()
    return render(request, 'trivia_app/categories.html', {'categories': categories})

def question_page(request, category_id, question_index=0):
    category = get_object_or_404(Category, pk=category_id)
    questions = category.questions.all()
    
    if question_index >= len(questions):
        return redirect('trivia_app:results', category_id=category_id)

    question = questions[question_index]
    answers = list(question.answers.all())
    random.shuffle(answers)
    return render(request, 'trivia_app/question.html', {
        'question': question,
        'answers': answers,
        'question_index': question_index,
        'total_questions': len(questions),
    })

def results(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    user_answers = request.session.get('user_answers', {})
    correct_answers = []
    score = 0

    for question in category.questions.all():
        correct = [a.text for a in question.answers.filter(is_correct=True)]
        user_answer = user_answers.get(str(question.id), None)
        correct_answers.append({
            'question': question.text,
            'correct': correct,
            'user_answer': user_answer,
            'is_correct': user_answer in correct,
        })
        if user_answer in correct:
            score += 1

    return render(request, 'trivia_app/results.html', {
        'category': category,
        'score': score,
        'total': len(correct_answers),
        'correct_answers': correct_answers,
    })

def save_answer(request, category_id, question_index):
    if request.method == 'POST':
        answer = request.POST.get('answer')
        question_id = request.POST.get('question_id')
        user_answers = request.session.get('user_answers', {})
        user_answers[question_id] = answer
        request.session['user_answers'] = user_answers
        return redirect('trivia_app:question_page', category_id=category_id, question_index=question_index + 1)
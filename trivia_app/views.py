from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Question, AnswerChoice

# View for listing all categories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'trivia_app/category_list.html', {'categories': categories})

# View for displaying questions for a specific category
def question_list(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    questions = category.questions.all()  # Get all questions related to this category
    return render(request, 'trivia_app/question_list.html', {'category': category, 'questions': questions})

# View for answering a specific question
def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.answer_choices.all()  # Get all answer choices related to this question
    return render(request, 'trivia_app/question_detail.html', {'question': question, 'choices': choices})

# View for submitting the answer
def submit_answer(request, question_id):
    if request.method == "POST":
        question = get_object_or_404(Question, pk=question_id)
        selected_choice = request.POST.get('choice')  # Get selected choice from the form
        
        # Check if the answer is correct
        is_correct = question.answer_choices.get(pk=selected_choice).is_correct
        
        # Return a result page with correct/incorrect message
        return render(request, 'trivia_app/answer_result.html', {'is_correct': is_correct, 'question': question})

    return redirect('question_detail', question_id=question_id)

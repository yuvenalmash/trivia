# trvia_app models
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Question(models.Model):
    category = models.ForeignKey(Category, related_name='questions', on_delete=models.CASCADE)
    text= models.TextField()
    difficulty = models.CharField(max_length=50, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='medium')

    def __str__(self):
        return self.text
    
class AnswerChoice(models.Model):
    question = models.ForeignKey(Question, related_name='answer_choices', on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

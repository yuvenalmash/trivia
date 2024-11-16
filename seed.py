import random
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trivia_project.settings')
django.setup()

from trivia_app.models import Category, Question, AnswerChoice

def seed_data():
    print("Seeding the database...")

    # Clear existing data
    AnswerChoice.objects.all().delete()
    Question.objects.all().delete()
    Category.objects.all().delete()

    # Categories
    categories = [
        "Science",
        "History",
        "Sports",
        "Movies",
        "Geography"
    ]
    category_objects = [Category.objects.create(name=cat) for cat in categories]

    # Questions and Answers
    for category in category_objects:
        for i in range(5):  # Add 5 questions per category
            question = Question.objects.create(
                category=category,
                text=f"Sample question {i+1} in {category.name}?",
                difficulty=random.choice(["easy", "medium", "hard"])
            )
            # Add answer choices
            for j in range(4):  # 4 choices per question
                is_correct = (j == 0)  # Make the first one correct
                AnswerChoice.objects.create(
                    question=question,
                    text=f"Choice {j+1} for {question.text}",
                    is_correct=is_correct
                )

    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()

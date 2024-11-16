import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trivia_project.settings")
django.setup()

from trivia_app.models import Category, Question, Answer

def run():
    # Clear existing data
    Answer.objects.all().delete()
    Question.objects.all().delete()
    Category.objects.all().delete()

    # Categories
    categories_data = [
        "Technology",
        "Science",
        "History",
        "Geography",
        "Entertainment",
    ]

    categories = {name: Category.objects.create(name=name) for name in categories_data}

    # Questions and Answers
    questions_data = {
        "Technology": [
            {
                "text": "Who is known as the father of the computer?",
                "answers": [
                    {"text": "Charles Babbage", "is_correct": True},
                    {"text": "Alan Turing", "is_correct": False},
                    {"text": "Bill Gates", "is_correct": False},
                    {"text": "Steve Jobs", "is_correct": False},
                ],
            },
            {
                "text": "What is the smallest unit of data in a computer?",
                "answers": [
                    {"text": "Bit", "is_correct": True},
                    {"text": "Byte", "is_correct": False},
                    {"text": "Megabyte", "is_correct": False},
                    {"text": "Gigabyte", "is_correct": False},
                ],
            },
            {
                "text": "What does CPU stand for?",
                "answers": [
                    {"text": "Central Processing Unit", "is_correct": True},
                    {"text": "Computer Personal Unit", "is_correct": False},
                    {"text": "Central Process Unit", "is_correct": False},
                    {"text": "Computer Processing Unit", "is_correct": False},
                ],
            },
        ],
        "Science": [
            {
                "text": "What planet is known as the Red Planet?",
                "answers": [
                    {"text": "Mars", "is_correct": True},
                    {"text": "Venus", "is_correct": False},
                    {"text": "Jupiter", "is_correct": False},
                    {"text": "Saturn", "is_correct": False},
                ],
            },
            {
                "text": "What is the powerhouse of the cell?",
                "answers": [
                    {"text": "Mitochondria", "is_correct": True},
                    {"text": "Nucleus", "is_correct": False},
                    {"text": "Ribosome", "is_correct": False},
                    {"text": "Endoplasmic Reticulum", "is_correct": False},
                ],
            },
            {
                "text": "What is the chemical symbol for water?",
                "answers": [
                    {"text": "H2O", "is_correct": True},
                    {"text": "CO2", "is_correct": False},
                    {"text": "O2", "is_correct": False},
                    {"text": "H2O2", "is_correct": False},
                ],
            },
        ],
        "History": [
            {
                "text": "Who was the first President of the Kenya?",
                "answers": [
                    {"text": "Jomo Kenyatta", "is_correct": True},
                    {"text": "Uhuru Kenyatta", "is_correct": False},
                    {"text": "Mwai Kibaki", "is_correct": False},
                    {"text": "Daniel Moi", "is_correct": False},
                ],
            },
            {
                "text": "Who was the first European to reach India by sea?",
                "answers": [
                    {"text": "Vasco da Gama", "is_correct": True},
                    {"text": "Christopher Columbus", "is_correct": False},
                    {"text": "Ferdinand Magellan", "is_correct": False},
                    {"text": "Amerigo Vespucci", "is_correct": False},
                ],
            },
            {
                "text": "Who was a Kenyan freedom fighter from the Giriama people?",
                "answers": [
                    {"text": "Mekatilili wa Menza", "is_correct": True},
                    {"text": "Wangari Maathai", "is_correct": False},
                    {"text": "Dedan Kimathi", "is_correct": False},
                    {"text": "Koitalel Arap Samoei", "is_correct": False},
                ],
            },
        ],
        "Geography": [
            {
                "text": "Which is the largest ocean on Earth?",
                "answers": [
                    {"text": "Pacific Ocean", "is_correct": True},
                    {"text": "Atlantic Ocean", "is_correct": False},
                    {"text": "Indian Ocean", "is_correct": False},
                    {"text": "Arctic Ocean", "is_correct": False},
                ],
            },
            {
                "text": "What is the capital of Australia?",
                "answers": [
                    {"text": "Canberra", "is_correct": True},
                    {"text": "Sydney", "is_correct": False},
                    {"text": "Melbourne", "is_correct": False},
                    {"text": "Perth", "is_correct": False},
                ],
            },
            {
                "text": "What is the largest country in the world?",
                "answers": [
                    {"text": "Russia", "is_correct": True},
                    {"text": "Canada", "is_correct": False},
                    {"text": "China", "is_correct": False},
                    {"text": "United States", "is_correct": False},
                ],
            },
        ],
        "Entertainment": [
            {
                "text": "Who directed the movie 'Inception'?",
                "answers": [
                    {"text": "Christopher Nolan", "is_correct": True},
                    {"text": "Steven Spielberg", "is_correct": False},
                    {"text": "James Cameron", "is_correct": False},
                    {"text": "Quentin Tarantino", "is_correct": False},
                ],
            },
            {
                "text": "Which actor plays the character Tony Stark in the Marvel Cinematic Universe?",
                "answers": [
                    {"text": "Robert Downey Jr.", "is_correct": True},
                    {"text": "Chris Evans", "is_correct": False},
                    {"text": "Chris Hemsworth", "is_correct": False},
                    {"text": "Mark Ruffalo", "is_correct": False},
                ],
            },
            {
                "text": "What is the highest-grossing movie of all time?",
                "answers": [
                    {"text": "Avengers: Endgame", "is_correct": True},
                    {"text": "Avatar", "is_correct": False},
                    {"text": "Titanic", "is_correct": False},
                    {"text": "Star Wars: The Force Awakens", "is_correct": False},
                ],
            },
        ],
    }

    for category_name, questions in questions_data.items():
        category = categories[category_name]
        for question_data in questions:
            question = Question.objects.create(
                category=category, text=question_data["text"]
            )
            for answer_data in question_data["answers"]:
                Answer.objects.create(
                    question=question,
                    text=answer_data["text"],
                    is_correct=answer_data["is_correct"],
                )

    print("Seeding complete!")

if __name__ == "__main__":
    run()

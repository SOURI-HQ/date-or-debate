from app.domain.question import Question
from app.extensions import db


class QuestionService:
    @staticmethod
    def create_question(content):
        new_question = Question(content=content)

        db.session.add(new_question)
        db.session.commit()

        return new_question

    @staticmethod
    def get_all_questions():
        return Question.query.all()

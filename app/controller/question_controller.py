from flask import Blueprint, request, jsonify
from app.service.question_service import QuestionService

question_bp = Blueprint('question', __name__)


@question_bp.route('/', methods=['GET'])
def get_questions():
    questions = QuestionService.get_all_questions()

    return jsonify([{"id": question.id, "content": question.content} for question in questions])


@question_bp.route('/', methods=['POST'])
def add_question():
    data = request.get_json()
    content = data.get('content')

    if not content:
        return jsonify({"error: Content is required"}), 400

    question = QuestionService.create_question(content)

    return jsonify({"id": question.id, "content": question.content}), 201


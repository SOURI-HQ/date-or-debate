from app.extensions import db


class Question(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"<Question {self.content}>"
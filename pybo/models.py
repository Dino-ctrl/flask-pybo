from sqlalchemy.orm import backref
from sqlalchemy.testing.pickleable import User

from pybo import db


question_voter = db.Table('question_voter',
                          db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
                          db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
                          )

answer_voter = db.Table('answer_voter',
                        db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
                        db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
                        )

# 모든 모델의 기본 클래스 db.Model 상속 받음. 이 때 db는 __init__.py 파일에서 생성한 SQLAlchemy 객체
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))
# nullable 옵션은 속성에 빈 값 허용여부 결정. False면 빈값 허용 안함
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))


# 답변 모델 생성
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id' , ondelete='CASCADE'))
    question = db.relationship(Question, backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))
# 어떤 속성을 기존 모델과 연결하려면 db.ForeignKey 사용

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False) # 같은 값 지정 불가
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('comment_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime())
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), nullable=True)
    question = db.relationship('Question', backref=db.backref('comment_set'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), nullable=True)
    answer = db.relationship('Answer', backref=db.backref('comment_set'))



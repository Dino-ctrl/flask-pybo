from flask import Flask
# 플라스크 애플리케이션을 생성하는 코드 __name__이라는 변수에는 모듈명이 담김.
# app = Flask(__name__)
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config
from sqlalchemy import MetaData


naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


# app.route는 특정 주소에 접속하면 바로 다음 줄에 있는 함수를 호출하는 플라스크의 데코레이터
# @app.route('/')

### 함수명으로 create_app 대신 다른 이름을 사용하면 작동하지 않음. create_app은 플라스크 내부에서 정의된 함수명임
def create_app():
    # 변수를 선언하는 건 함수 밖에서 선언하고, 초기화만 함수 내부에서 수행
    # app.config 환경 변수를 부르기 위해 app.config.from_object(config) 추가
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM 적용하기
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views, question_views, answer_views, auth_views, comment_views, vote_views
    app.register_blueprint(main_views.bp) # 블루프린트 객체 bp 등록
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(comment_views.bp)
    app.register_blueprint(vote_views.bp)


    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    # ✅ Markdown 필터 등록
    from markdown import markdown
    from markupsafe import Markup

    @app.template_filter('markdown')
    def markdown_filter(text):
        return Markup(markdown(text, extensions=['fenced_code', 'nl2br']))
    return app



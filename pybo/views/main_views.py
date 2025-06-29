from flask import Blueprint, url_for
from werkzeug.utils import redirect


bp = Blueprint('main', __name__, url_prefix='/')
@bp.route('/hello')
def hello_pybo():
    return 'Hello Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
# 인덱스 함수를 question._list에 해당하는 URL로 리다이렉트 할 수 있도록 코드 수정
# redirect 함수는 입력받은 URL로 리다이렉트 해주고, url_for 함수는 라우트가 설정된 함수명으로 URL를 역으로 찾아줌


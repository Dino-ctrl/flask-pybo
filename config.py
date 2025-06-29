import os
# ORM를 쓰려면 설정 파일을 추가해야 함.
from flask_sqlalchemy import SQLAlchemy

BASE_DIR = os.path.dirname(__file__)
# BASE_DIR의 경로는 프로젝트의 루트 디렉토리 : C:\projects\myproject

# 이건 접속 주소. pybo.db라는 데이터베이스 파일을 프로젝트의 루트 디렉터리에 저장하려는 것
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# 이건 이벤트를 처리하는 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"


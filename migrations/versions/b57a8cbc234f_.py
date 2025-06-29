"""empty message

Revision ID: b57a8cbc234f
Revises: ccbf590cb3e3
Create Date: 2025-06-28 00:45:46.550337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b57a8cbc234f'
down_revision = 'ccbf590cb3e3'
branch_labels = None
depends_on = None


def upgrade():
    # 기존 테이블 삭제
    op.drop_table('question_voter')

    # 수정된 컬럼명으로 테이블 생성
    op.create_table(
        'question_voter',
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
        sa.Column('question_id', sa.Integer, sa.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True),
    )

def downgrade():
    # 다운그레이드는 기존 테이블 컬럼명 형태로 재생성
    op.drop_table('question_voter')
    op.create_table(
        'question_voter',
        sa.Column('user.id', sa.Integer, sa.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
        sa.Column('question.id', sa.Integer, sa.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True),
    )

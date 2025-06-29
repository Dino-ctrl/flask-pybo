"""Fix voter tables

Revision ID: ccbf590cb3e3
Revises: 8bf5f620a5b1
Create Date: 2025-06-28 00:36:24.285887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccbf590cb3e3'
down_revision = '8bf5f620a5b1'
branch_labels = None
depends_on = None


def upgrade():
    # 만약 불필요한 임시 테이블이 있다면 삭제
    op.drop_table('_alembic_tmp_answer_voter')

    # answer_voter 테이블 변경 예시 - 컬럼 추가나 삭제 없다면 주석 처리 혹은 삭제
    # with op.batch_alter_table('answer_voter', schema=None) as batch_op:
    #     batch_op.add_column(sa.Column('answer_id', sa.Integer(), nullable=False))
    #     batch_op.create_foreign_key(batch_op.f('fk_answer_voter_answer_id_answer'), 'answer', ['answer_id'], ['id'], ondelete='CASCADE')
    #     batch_op.drop_column('id')  # 이 부분은 틀림, id 컬럼 없음

    # question_voter 테이블 변경 예시 - 마찬가지로 컬럼 추가나 삭제 없으면 주석 처리
    # with op.batch_alter_table('question_voter', schema=None) as batch_op:
    #     batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
    #     batch_op.add_column(sa.Column('question_id', sa.Integer(), nullable=False))
    #     batch_op.create_foreign_key(batch_op.f('fk_question_voter_question_id_question'), 'question', ['question_id'], ['id'], ondelete='CASCADE')
    #     batch_op.create_foreign_key(batch_op.f('fk_question_voter_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')
    #     batch_op.drop_column('id')  # 틀림, id 없음
    #     batch_op.drop_column('id')

def downgrade():
    # 만약 위에서 아무 것도 변경하지 않았다면 downgrade도 빈 함수나 pass
    pass

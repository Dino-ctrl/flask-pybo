"""empty message

Revision ID: 8f10d6f6bc8f
Revises: b57a8cbc234f
Create Date: 2025-06-28 00:49:00.571114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f10d6f6bc8f'
down_revision = 'b57a8cbc234f'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('answer_voter')
    op.create_table(
        'answer_voter',
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
        sa.Column('answer_id', sa.Integer, sa.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True),
    )

def downgrade():
    op.drop_table('answer_voter')
    op.create_table(
        'answer_voter',
        sa.Column('user.id', sa.Integer, sa.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
        sa.Column('answer.id', sa.Integer, sa.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True),
    )

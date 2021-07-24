"""set table

Revision ID: 4e8062a270cc
Revises: e22a2e72d92f
Create Date: 2021-07-24 20:48:04.192947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e8062a270cc'
down_revision = 'e22a2e72d92f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('set',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('exercise', sa.String(length=120), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('repetitions', sa.Integer(), nullable=True),
    sa.Column('rate_of_perceived_exertion', sa.Integer(), nullable=True),
    sa.Column('reps_in_reserve', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_set_exercise'), 'set', ['exercise'], unique=False)
    op.create_index(op.f('ix_set_timestamp'), 'set', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_set_timestamp'), table_name='set')
    op.drop_index(op.f('ix_set_exercise'), table_name='set')
    op.drop_table('set')
    # ### end Alembic commands ###

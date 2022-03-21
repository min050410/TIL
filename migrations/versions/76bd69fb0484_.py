"""empty message

Revision ID: 76bd69fb0484
Revises: 57f27b781a9f
Create Date: 2021-09-16 13:11:34.905728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76bd69fb0484'
down_revision = '57f27b781a9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###

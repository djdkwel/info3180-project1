"""empty message

Revision ID: dfc0ee78359c
Revises: 
Create Date: 2019-03-14 15:52:38.865132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfc0ee78359c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=80), nullable=True),
    sa.Column('lastname', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('gender', sa.String(length=80), nullable=True),
    sa.Column('biography', sa.String(length=255), nullable=True),
    sa.Column('filename', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profiles')
    # ### end Alembic commands ###

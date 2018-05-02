"""initial migration

Revision ID: 4c6cd7da7f62
Revises: 38c4e85512a9
Create Date: 2018-04-09 21:43:35.690638

"""

# revision identifiers, used by Alembic.
revision = '4c6cd7da7f62'
down_revision = '38c4e85512a9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###

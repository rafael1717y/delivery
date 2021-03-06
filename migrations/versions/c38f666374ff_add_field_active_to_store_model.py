"""add field active to Store model

Revision ID: c38f666374ff
Revises: 4ae739dc66b3
Create Date: 2022-03-30 07:22:03.997494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c38f666374ff'
down_revision = '4ae739dc66b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('store', 'active')
    # ### end Alembic commands ###

"""empty message

Revision ID: 179062d306de
Revises: 727db206c6c2
Create Date: 2022-08-03 20:26:57.776068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '179062d306de'
down_revision = '727db206c6c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemon')
    # ### end Alembic commands ###

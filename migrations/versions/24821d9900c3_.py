"""empty message

Revision ID: 24821d9900c3
Revises: 1520f30f64d9
Create Date: 2022-08-04 19:53:15.787748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24821d9900c3'
down_revision = '1520f30f64d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_poke')
    op.add_column('user', sa.Column('pokemon', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'pokemon', ['pokemon'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'pokemon')
    op.create_table('user_poke',
    sa.Column('pokemon_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.id'], name='user_poke_pokemon_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='user_poke_user_id_fkey')
    )
    # ### end Alembic commands ###

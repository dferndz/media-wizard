"""empty message

Revision ID: a9b2a7bc7f4e
Revises: 
Create Date: 2024-06-30 11:51:03.392038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9b2a7bc7f4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('media_request',
    sa.Column('request_id', sa.Integer(), nullable=False),
    sa.Column('tmdb_id', sa.String(length=255), nullable=True),
    sa.Column('request_type', sa.String(length=140), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('request_id', name=op.f('pk_media_request'))
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=140), nullable=True),
    sa.Column('password', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user'))
    )
    op.create_table('tv_request_season',
    sa.Column('season_request_id', sa.Integer(), nullable=False),
    sa.Column('media_request_id', sa.Integer(), nullable=True),
    sa.Column('season_number', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['media_request_id'], ['media_request.request_id'], name=op.f('fk_tv_request_season_media_request_id_media_request'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('season_request_id', name=op.f('pk_tv_request_season'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tv_request_season')
    op.drop_table('user')
    op.drop_table('media_request')
    # ### end Alembic commands ###

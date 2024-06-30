"""empty message

Revision ID: 5349080b5834
Revises: a9b2a7bc7f4e
Create Date: 2024-06-30 12:04:19.280804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5349080b5834'
down_revision = 'a9b2a7bc7f4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tv_request_season', schema=None) as batch_op:
        batch_op.drop_constraint('fk_tv_request_season_media_request_id_media_request', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_tv_request_season_media_request_id_media_request'), 'media_request', ['media_request_id'], ['request_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tv_request_season', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_tv_request_season_media_request_id_media_request'), type_='foreignkey')
        batch_op.create_foreign_key('fk_tv_request_season_media_request_id_media_request', 'media_request', ['media_request_id'], ['request_id'], ondelete='CASCADE')

    # ### end Alembic commands ###

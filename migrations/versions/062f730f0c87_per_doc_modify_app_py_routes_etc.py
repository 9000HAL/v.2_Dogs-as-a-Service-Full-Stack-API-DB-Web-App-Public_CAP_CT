"""per doc. modify app.py routes etc

Revision ID: 062f730f0c87
Revises: a27be5af00ac
Create Date: 2023-09-15 14:53:32.013276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '062f730f0c87'
down_revision = 'a27be5af00ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=128), nullable=False))
#changed to FALSE per documentation here above......?????
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###

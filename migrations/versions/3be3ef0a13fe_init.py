"""Init

Revision ID: 3be3ef0a13fe
Revises: 31b43b7b8bc5
Create Date: 2023-05-04 19:25:20.758119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3be3ef0a13fe'
down_revision = '31b43b7b8bc5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_contacts_email'), 'contacts', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contacts_email'), table_name='contacts')
    # ### end Alembic commands ###

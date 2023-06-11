"""add content column to posts table

Revision ID: 84a76b170383
Revises: dab6d3a62100
Create Date: 2023-06-10 19:35:16.915187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84a76b170383'
down_revision = 'dab6d3a62100'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass

"""add last few column to posts table

Revision ID: cd89ce933e42
Revises: 719e1a7fa306
Create Date: 2023-06-10 23:03:14.075695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd89ce933e42'
down_revision = '719e1a7fa306'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='True'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass

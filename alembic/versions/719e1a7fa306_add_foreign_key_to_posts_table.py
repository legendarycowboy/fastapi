"""add foreign-key to posts table

Revision ID: 719e1a7fa306
Revises: f5a24032f7cd
Create Date: 2023-06-10 22:38:19.385929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '719e1a7fa306'
down_revision = 'f5a24032f7cd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users",
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_namr = "posts")
    op.drop_column('posts', 'owner_id')
    pass

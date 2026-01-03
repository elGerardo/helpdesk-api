"""create folders table

Revision ID: 010
Revises: 009
Create Date: 2026-01-03 00:00:10

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '010'
down_revision: Union[str, Sequence[str], None] = '009'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create folders table."""
    op.create_table(
        'folders',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('tenant_id', sa.BigInteger(), nullable=False),
        sa.Column('workspace_id', sa.BigInteger(), nullable=False),
        sa.Column('folder_id', sa.BigInteger(), nullable=True),
        sa.Column('folder_name', sa.String(255), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], name='folders_tenant_id_foreign'),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'], name='folders_workspace_id_foreign'),
        sa.ForeignKeyConstraint(['folder_id'], ['folders.id'], name='folders_folder_id_foreign')
    )


def downgrade() -> None:
    """Drop folders table."""
    op.drop_table('folders')

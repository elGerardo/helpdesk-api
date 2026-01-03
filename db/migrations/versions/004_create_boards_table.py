"""create boards table

Revision ID: 004
Revises: 003
Create Date: 2026-01-03 00:00:04

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '004'
down_revision: Union[str, Sequence[str], None] = '003'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create boards table."""
    op.create_table(
        'boards',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('tenant_id', sa.BigInteger(), nullable=False),
        sa.Column('workspace_id', sa.BigInteger(), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('nomenclature', sa.String(255), nullable=False),
        sa.Column('description', sa.String(255), nullable=True),
        sa.Column('logo', sa.String(255), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], name='boards_tenant_id_foreign'),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'], name='boards_workspace_id_foreign')
    )


def downgrade() -> None:
    """Drop boards table."""
    op.drop_table('boards')

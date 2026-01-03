"""create forms table

Revision ID: 005
Revises: 004
Create Date: 2026-01-03 00:00:05

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '005'
down_revision: Union[str, Sequence[str], None] = '004'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create forms table."""
    op.create_table(
        'forms',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('tenant_id', sa.BigInteger(), nullable=False),
        sa.Column('form_id', sa.BigInteger(), nullable=False),
        sa.Column('board_id', sa.BigInteger(), nullable=False),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('nomenclature', sa.String(255), nullable=False),
        sa.Column('description', sa.String(255), nullable=True),
        sa.Column('status', sa.String(255), nullable=False, server_default='DRAFT'),
        sa.Column('version', sa.BigInteger(), nullable=False, server_default='1'),
        sa.Column('created_by', sa.BigInteger(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['board_id'], ['boards.id'], name='forms_board_id_foreign'),
        sa.ForeignKeyConstraint(['form_id'], ['forms.id'], name='forms_form_id_foreign')
    )
    
    # Add comment for status column
    op.execute("COMMENT ON COLUMN forms.status IS 'DRAFT | PUBLISHED'")


def downgrade() -> None:
    """Drop forms table."""
    op.drop_table('forms')

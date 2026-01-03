"""create form_fields table

Revision ID: 608f030f0185
Revises: bd50cd8baafe
Create Date: 2026-01-03 02:08:58.971768

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '608f030f0185'
down_revision: Union[str, Sequence[str], None] = 'bd50cd8baafe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create form_fields table."""
    op.create_table(
        'form_fields',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('form_id', sa.BigInteger(), nullable=True),
        sa.Column('ticket_id', sa.BigInteger(), nullable=True),
        sa.Column('label', sa.String(255), nullable=False),
        sa.Column('placeholder', sa.BigInteger(), nullable=False),
        sa.Column('type', sa.String(255), nullable=False, comment='TEXT | TEXT_AREA | NUMBER | LIST | CHECKBOX | DATE | TIME | RADIO | IMAGE | RANGE'),
        sa.Column('required', sa.Boolean(), nullable=False, server_default='0'),
        sa.Column('min', sa.BigInteger(), nullable=True),
        sa.Column('max', sa.BigInteger(), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['form_id'], ['forms.id']),
        sa.ForeignKeyConstraint(['ticket_id'], ['tickets.id'])
    )


def downgrade() -> None:
    """Drop form_fields table."""
    op.drop_table('form_fields')

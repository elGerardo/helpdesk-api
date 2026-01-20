"""create form_fields table

Revision ID: 008
Revises: 007
Create Date: 2026-01-03 00:00:08

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '008'
down_revision: Union[str, Sequence[str], None] = '007'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create form_fields table."""
    op.create_table(
        'form_fields',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('tenant_id', sa.BigInteger(), nullable=False),
        sa.Column('form_id', sa.BigInteger(), nullable=True),
        sa.Column('ticket_id', sa.BigInteger(), nullable=True),
        sa.Column('label', sa.String(255), nullable=False),
        sa.Column('placeholder', sa.String(255), nullable=False),
        sa.Column('type', sa.String(255), nullable=False),
        sa.Column('required', sa.Boolean(), nullable=False, server_default='false'),
        sa.Column('min', sa.BigInteger(), nullable=True),
        sa.Column('max', sa.BigInteger(), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], name='form_fields_tenant_id_foreign'),
        sa.ForeignKeyConstraint(['form_id'], ['forms.id'], name='form_fields_form_id_foreign'),
        sa.ForeignKeyConstraint(['ticket_id'], ['tickets.id'], name='form_fields_ticket_id_foreign')
    )
    
    # Add comment for type column
    op.execute("COMMENT ON COLUMN form_fields.type IS 'TEXT | TEXT_AREA | NUMBER | LIST | CHECKBOX | DATE | TIME | RADIO | IMAGE | RANGE'")


def downgrade() -> None:
    """Drop form_fields table."""
    op.drop_table('form_fields')

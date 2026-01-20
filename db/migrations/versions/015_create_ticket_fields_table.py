"""create ticket_fields table

Revision ID: 015
Revises: 014
Create Date: 2026-01-20 00:00:15

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '015'
down_revision: Union[str, Sequence[str], None] = '014'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create ticket_fields junction table."""
    op.create_table(
        'ticket_fields',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('tenant_id', sa.BigInteger(), nullable=False),
        sa.Column('ticket_id', sa.BigInteger(), nullable=False),
        sa.Column('form_field_id', sa.BigInteger(), nullable=False),
        sa.Column('value', sa.String(255), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], name='ticket_fields_tenant_id_foreign'),
        sa.ForeignKeyConstraint(['ticket_id'], ['tickets.id'], name='ticket_fields_ticket_id_foreign'),
        sa.ForeignKeyConstraint(['form_field_id'], ['form_fields.id'], name='ticket_fields_form_field_id_foreign')
    )


def downgrade() -> None:
    """Drop ticket_fields table."""
    op.drop_table('ticket_fields')

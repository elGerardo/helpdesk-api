"""add tenant foreign keys

Revision ID: 012
Revises: 011
Create Date: 2026-01-03 00:00:12

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '012'
down_revision: Union[str, Sequence[str], None] = '011'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Add circular foreign key constraints."""
    # Add tenants owner foreign key
    op.create_foreign_key(
        'tenants_owner_id_foreign',
        'tenants', 'users',
        ['owner_id'], ['id']
    )
    # Add users tenant foreign key
    op.create_foreign_key(
        'users_tenant_id_foreign',
        'users', 'tenants',
        ['tenant_id'], ['id']
    )


def downgrade() -> None:
    """Drop circular foreign key constraints."""
    op.drop_constraint('users_tenant_id_foreign', 'users', type_='foreignkey')
    op.drop_constraint('tenants_owner_id_foreign', 'tenants', type_='foreignkey')

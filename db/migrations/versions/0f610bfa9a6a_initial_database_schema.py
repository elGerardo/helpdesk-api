"""initial database schema

Revision ID: 0f610bfa9a6a
Revises: 042d79c95ff7
Create Date: 2026-01-03 02:06:54.531840

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f610bfa9a6a'
down_revision: Union[str, Sequence[str], None] = '042d79c95ff7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

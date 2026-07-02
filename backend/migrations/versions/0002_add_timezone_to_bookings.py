"""Add timezone support to bookings timestamps

Revision ID: 0002
Revises: 0001
Create Date: 2026-07-01
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "0002"
down_revision: Union[str, None] = "0001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("bookings") as batch_op:
        batch_op.alter_column(
            "start_time",
            type_=sa.DateTime(timezone=True),
            existing_type=sa.DateTime(),
            nullable=False,
        )
        batch_op.alter_column(
            "end_time",
            type_=sa.DateTime(timezone=True),
            existing_type=sa.DateTime(),
            nullable=False,
        )


def downgrade() -> None:
    with op.batch_alter_table("bookings") as batch_op:
        batch_op.alter_column(
            "start_time",
            type_=sa.DateTime(),
            existing_type=sa.DateTime(timezone=True),
            nullable=False,
        )
        batch_op.alter_column(
            "end_time",
            type_=sa.DateTime(),
            existing_type=sa.DateTime(timezone=True),
            nullable=False,
        )

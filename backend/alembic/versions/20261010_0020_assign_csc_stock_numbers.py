"""Assign each vehicle a unique CSC stock number.

Revision ID: 20261010_0020
Revises: 20261009_0019
Create Date: 2026-10-10
"""

import secrets

from alembic import op
import sqlalchemy as sa


revision = "20261010_0020"
down_revision = "20261009_0019"
branch_labels = None
depends_on = None


def _new_stock_number(used: set[str]) -> str:
    while True:
        candidate = f"CSC{secrets.randbelow(100_000):05d}"
        if candidate not in used:
            used.add(candidate)
            return candidate


def upgrade():
    connection = op.get_bind()
    op.create_table(
        "_stock_number_backup_20261010_0020",
        sa.Column("vehicle_id", sa.String(), primary_key=True),
        sa.Column("stock_number", sa.String(), nullable=True),
    )
    connection.execute(
        sa.text(
            "INSERT INTO _stock_number_backup_20261010_0020 (vehicle_id, stock_number) "
            "SELECT id, stock_number FROM vehicles"
        )
    )

    vehicles = sa.table(
        "vehicles",
        sa.column("id", sa.String()),
        sa.column("stock_number", sa.String()),
    )
    rows = connection.execute(sa.select(vehicles.c.id, vehicles.c.stock_number)).all()
    used: set[str] = set()
    for vehicle_id, _ in rows:
        connection.execute(
            vehicles.update()
            .where(vehicles.c.id == vehicle_id)
            .values(stock_number=_new_stock_number(used))
        )


def downgrade():
    connection = op.get_bind()
    backup = sa.table(
        "_stock_number_backup_20261010_0020",
        sa.column("vehicle_id", sa.String()),
        sa.column("stock_number", sa.String()),
    )
    vehicles = sa.table(
        "vehicles",
        sa.column("id", sa.String()),
        sa.column("stock_number", sa.String()),
    )
    for vehicle_id, stock_number in connection.execute(
        sa.select(backup.c.vehicle_id, backup.c.stock_number)
    ):
        connection.execute(
            vehicles.update()
            .where(vehicles.c.id == vehicle_id)
            .values(stock_number=stock_number)
        )
    op.drop_table("_stock_number_backup_20261010_0020")

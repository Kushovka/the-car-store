"""Align vehicle prices with the spreadsheet Our Price column.

Revision ID: 20261009_0018
Revises: 20261009_0017
Create Date: 2026-10-09
"""

from alembic import op
import sqlalchemy as sa

revision = "20261009_0018"
down_revision = "20261009_0017"
branch_labels = None
depends_on = None

VEHICLE_PRICES = {
    '2021-lexus-lx570-inspiration-series': 49999,
    '2025-mercedes-benz-gle63-s-amg-coupe': 78499,
    '2025-bmw-m4-competition-xdrive': 63999,
    '2025-bmw-m3-competition-xdrive': 59999,
    '2025-bmw-x5-xdrive40i-silver-anniversary': 42999,
    '2020-bmw-m760i-xdrive': 40999,
    '2024-bmw-m4-competition-xdrive-convertible': 56999,
    '2024-gmc-sierra-2500-at4': 51999,
    '2025-chevrolet-corvette-z06-convertible-2lz': 86999,
    '2022-gmc-sierra-1500-elevation': 29999,
    '2021-gmc-sierra-1500-denali': 26999,
    '2025-cadillac-ct5-v-blackwing': 82999,
    '2023-cadillac-ct5-v-blackwing-edition': 63999,
    '2023-cadillac-escalade-sport-platinum-onyx': 64999,
    '2024-cadillac-escalade-v': 94999,
    '2020-mercedes-benz-g63-amg-4matic': 94999,
    '2022-cadillac-escalade-premium-luxury-4wd': 47999,
    '2026-tesla-model-y-launch-edition': 0,
    '2025-tesla-model-y-performance': 0,
    '2024-tesla-cybertruck-cyberbeast-foundation': 0,
    '2024-tesla-cybertruck-foundation-series': 0,
    '2025-chevrolet-corvette-e-ray-convertible-3lz': 0,
}

PREVIOUS_PRICES = {
    '2021-lexus-lx570-inspiration-series': 26999,
    '2025-mercedes-benz-gle63-s-amg-coupe': 29999,
    '2025-bmw-m4-competition-xdrive': 36888,
    '2025-bmw-m3-competition-xdrive': 36888,
    '2025-bmw-x5-xdrive40i-silver-anniversary': 36888,
    '2020-bmw-m760i-xdrive': 36888,
    '2024-bmw-m4-competition-xdrive-convertible': 36888,
    '2024-gmc-sierra-2500-at4': 74999,
    '2025-chevrolet-corvette-z06-convertible-2lz': 34999,
    '2022-gmc-sierra-1500-elevation': 74999,
    '2021-gmc-sierra-1500-denali': 74999,
    '2025-cadillac-ct5-v-blackwing': 27500,
    '2023-cadillac-ct5-v-blackwing-edition': 27500,
    '2022-cadillac-escalade-premium-luxury-4wd': 47999,
    '2023-cadillac-escalade-sport-platinum-onyx': 27500,
    '2024-cadillac-escalade-v': 27500,
    '2020-mercedes-benz-g63-amg-4matic': 29999,
    '2026-tesla-model-y-launch-edition': 0,
    '2025-tesla-model-y-performance': 0,
    '2024-tesla-cybertruck-cyberbeast-foundation': 0,
    '2024-tesla-cybertruck-foundation-series': 0,
    '2025-chevrolet-corvette-e-ray-convertible-3lz': 89999,
}


def upgrade():
    vehicles = sa.table("vehicles", sa.column("slug", sa.String), sa.column("price", sa.Integer))
    connection = op.get_bind()
    for slug, price in VEHICLE_PRICES.items():
        connection.execute(vehicles.update().where(vehicles.c.slug == slug).values(price=price))


def downgrade():
    vehicles = sa.table("vehicles", sa.column("slug", sa.String), sa.column("price", sa.Integer))
    connection = op.get_bind()
    for slug, price in PREVIOUS_PRICES.items():
        connection.execute(vehicles.update().where(vehicles.c.slug == slug).values(price=price))
